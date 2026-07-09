#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

def convert_theme(dir_path: Path, output_base: Path):
    print(f"Processing directory: {dir_path}")
    inf_files = list(dir_path.glob("*.inf"))
    if not inf_files:
        print(f"Warning: No .inf file found in {dir_path}")
        return
    
    inf_file = inf_files[0]
    print(f"Found INF file: {inf_file}")
    
    # Read and parse the INF file (handling encoding and line endings)
    content = ""
    for encoding in ["utf-8", "windows-1252", "utf-16"]:
        try:
            with open(inf_file, "r", encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
            
    if not content:
        print(f"Error: Could not read INF file {inf_file}")
        return

    # Extract SCHEME_NAME
    # e.g., SCHEME_NAME = "Amiga WB1.0"
    scheme_match = re.search(r'SCHEME_NAME\s*=\s*"([^"]+)"', content, re.IGNORECASE)
    if not scheme_match:
        # Fall back to directory name
        scheme_name = dir_path.name.replace("-", " ")
    else:
        scheme_name = scheme_match.group(1).strip()
        
    print(f"Extracted Scheme Name: {scheme_name}")
    
    # Create safe folder name
    # e.g., "Amiga WB1.0 Mini" -> "Amiga-WB1.0-Mini"
    folder_name = scheme_name.replace(" ", "-")
    theme_dir = output_base / folder_name
    cursors_dir = theme_dir / "cursors"
    
    # Create directories
    cursors_dir.mkdir(parents=True, exist_ok=True)
    
    # Run win2xcurtheme
    print(f"Converting cursors using win2xcurtheme...")
    try:
        cmd = ["win2xcurtheme", str(inf_file), "-o", str(cursors_dir)]
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("\nError: 'win2xcurtheme' is not installed or not in PATH.")
        print("Please run: pip install win2xcur")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error converting theme: {e}")
        return
        
    # Create index.theme file
    index_theme_path = theme_dir / "index.theme"
    print(f"Generating index.theme: {index_theme_path}")
    index_theme_content = f"""[Icon Theme]
Name={scheme_name}
Comment={scheme_name} Cursor Theme (converted from Windows)
Inherits=breeze,Adwaita
"""
    with open(index_theme_path, "w", encoding="utf-8") as f:
        f.write(index_theme_content)
        
    print(f"Successfully converted theme to: {theme_dir}\n")

def package_theme(theme_dir: Path, dist_base: Path):
    tar_path = dist_base / f"{theme_dir.name}.tar.gz"
    print(f"Packaging theme '{theme_dir.name}' into: {tar_path}")
    with tarfile.open(tar_path, "w:gz") as tar:
        tar.add(theme_dir, arcname=theme_dir.name)

def main():
    workspace = Path("/gorgon/dev/Amiga-Workbench-Mouse-Cursors")
    output_base = workspace / "kde-themes"
    dist_base = workspace / "dist"
    
    # Clean output directories if they exist
    if output_base.exists():
        shutil.rmtree(output_base)
    output_base.mkdir(parents=True, exist_ok=True)
    
    if dist_base.exists():
        shutil.rmtree(dist_base)
    dist_base.mkdir(parents=True, exist_ok=True)
    
    directories = [
        "WB1.0-Mini",
        "WB1.0-Normal",
        "WB1.3-Mini",
        "WB1.3-Normal",
        "WB2.0-Mini",
        "WB2.0-Normal"
    ]
    
    for d in directories:
        dir_path = workspace / d
        if dir_path.is_dir():
            convert_theme(dir_path, output_base)
            
    print("Packaging converted themes into archives...")
    for theme_dir in output_base.iterdir():
        if theme_dir.is_dir():
            package_theme(theme_dir, dist_base)
            
    print(f"\nAll themes successfully packaged! Archives are located in: {dist_base}")
    print("\nTo extract and install a theme locally, run:")
    print("mkdir -p ~/.icons/")
    print(f"tar -xzf dist/Amiga-WB1.0.tar.gz -C ~/.icons/")

if __name__ == "__main__":
    main()
