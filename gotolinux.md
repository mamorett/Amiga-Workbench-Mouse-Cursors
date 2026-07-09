# Plan: Convert Windows 10 Cursors to KDE 5.x & 6.x

This document contains a step-by-step plan and executable instructions to convert all Amiga Workbench Windows 10 cursors in this repository to Linux/KDE compatible formats, package them as clean `.tar.gz` archives to avoid Git symlink clutter, and install them on KDE Plasma 5.x and 6.x.

A pre-configured python utility [convert.py](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/convert.py) has been created to automate the conversion and packaging of all themes.

---

## 📋 Table of Contents
1. [Overview of Cursor Themes to Convert](#1-overview-of-cursor-themes-to-convert)
2. [Prerequisites](#2-prerequisites)
3. [Conversion & Packaging Script Walkthrough](#3-conversion--packaging-script-walkthrough)
4. [Execution Steps](#4-execution-steps)
5. [Installation Instructions for KDE](#5-installation-instructions-for-kde)
6. [Applying the Theme in KDE](#6-applying-the-theme-in-kde)

---

## 1. Overview of Cursor Themes to Convert

The repository contains six folders containing Windows 10 cursor definitions (`.cur` files and `install.inf`):
- [WB1.0-Mini](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.0-Mini) (Scheme Name: `Amiga WB1.0 Mini`)
- [WB1.0-Normal](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.0-Normal) (Scheme Name: `Amiga WB1.0`)
- [WB1.3-Mini](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.3-Mini) (Scheme Name: `Amiga WB1.3 Mini`)
- [WB1.3-Normal](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.3-Normal) (Scheme Name: `Amiga WB1.3`)
- [WB2.0-Mini](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB2.0-Mini) (Scheme Name: `Amiga WB2.0 Mini`)
- [WB2.0-Normal](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB2.0-Normal) (Scheme Name: `Amiga WB2.0`)

The target output is a set of `.tar.gz` archives in the `dist/` directory, ready to be distributed or extracted.

---

## 2. Prerequisites

We use `win2xcur` to convert Windows `.cur` format to X11/KDE Xcursor format.

### Step 2.1: Create a Python Virtual Environment
To avoid conflicting with system-wide packages, create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2.2: Install `win2xcur`
Install the conversion utility using `pip`:
```bash
pip install win2xcur
```

---

## 3. Conversion & Packaging Script Walkthrough

The [convert.py](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/convert.py) script automates the following actions:
1. **Parses the Windows `install.inf`** file to extract the official `SCHEME_NAME` for each theme.
2. **Derives a safe theme folder name** (e.g., `Amiga-WB1.0-Normal`).
3. **Creates the standard directory layout** required by X11/KDE:
   ```
   Theme-Name/
   ├── index.theme
   └── cursors/
   ```
4. **Invokes `win2xcurtheme`** to convert `.cur` files to Xcursor format and establish required Freedesktop cursor symlinks.
5. **Generates the `index.theme`** file containing theme metadata and fallback inheritance:
   ```ini
   [Icon Theme]
   Name=Amiga WB1.0
   Comment=Amiga WB1.0 Cursor Theme (converted from Windows)
   Inherits=breeze,Adwaita
   ```
6. **Packages each theme** directory into a `.tar.gz` archive in the `dist/` folder using Python's `tarfile` module. This preserves the cursor symlinks perfectly without cluttering Git.

---

## 4. Execution Steps

Run the conversion and packaging script from the repository root:
```bash
python3 convert.py
```

Upon successful completion, a new folder `dist/` will be generated containing the packaged themes:
- `dist/Amiga-WB1.0.tar.gz`
- `dist/Amiga-WB1.0-Mini.tar.gz`
- `dist/Amiga-WB1.3.tar.gz`
- `dist/Amiga-WB1.3-Mini.tar.gz`
- `dist/Amiga-WB2.0.tar.gz`
- `dist/Amiga-WB2.0-Mini.tar.gz`

---

## 5. Installation Instructions for KDE (Per-User)

To install a cursor theme, simply create the user-level local icons folder (`~/.icons/`) if it does not exist, and extract the desired `.tar.gz` archive directly into it:

```bash
# Create the local icons directory if it doesn't exist
mkdir -p ~/.icons/

# Extract the desired theme (e.g. Amiga-WB1.0) into the ~/.icons/ directory
tar -xzf dist/Amiga-WB1.0.tar.gz -C ~/.icons/
```

> [!NOTE]
> Extracting directly into `~/.icons/` requires no administrative (`sudo`/root) privileges, keeps Git staging clean, and is natively detected by KDE Plasma and `libXcursor` out-of-the-box.

---

## 6. Applying the Theme in KDE

Once extracted, you can apply the theme using the KDE GUI settings or the command line.

### Method 1: Via Graphical User Interface (System Settings)

#### For KDE Plasma 6.x
1. Open **System Settings**.
2. Navigate to **Colors & Themes** (or **Appearance**) > **Cursors**.
3. Select your preferred Amiga cursor theme (e.g., `Amiga WB1.0`).
4. Click **Apply**.

#### For KDE Plasma 5.x
1. Open **System Settings**.
2. Navigate to **Appearance** > **Cursors**.
3. Select your preferred Amiga cursor theme (e.g., `Amiga WB1.0`).
4. Click **Apply**.

### Method 2: Via Command Line Interface (CLI)

You can apply the theme directly using the `plasma-apply-cursortheme` tool:
```bash
# Apply a theme (use the exact Name string from index.theme)
plasma-apply-cursortheme "Amiga WB1.0"
```
To verify the active theme and see all available themes:
```bash
plasma-apply-cursortheme --list-themes
```
