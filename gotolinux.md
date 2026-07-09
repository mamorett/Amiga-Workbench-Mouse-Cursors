# Plan: Convert Windows 10 Cursors to KDE 5.x/6.x & macOS Mousecape

This document contains a step-by-step plan and executable instructions to convert all Amiga Workbench Windows 10 cursors in this repository to Linux/KDE and macOS compatible formats, packaging them cleanly as `.tar.gz` and `.cape` files in the `dist/` directory to avoid Git symlink clutter.

A pre-configured python utility [convert.py](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/convert.py) has been created to automate the conversion and packaging of all themes.

---

## 📋 Table of Contents
1. [Overview of Cursor Themes to Convert](#1-overview-of-cursor-themes-to-convert)
2. [Prerequisites](#2-prerequisites)
3. [Conversion & Packaging Script Walkthrough](#3-conversion--packaging-script-walkthrough)
4. [Execution Steps](#4-execution-steps)
5. [Installation Instructions for Linux/KDE](#5-installation-instructions-for-linuxkde)
6. [Installation Instructions for macOS (Mousecape)](#6-installation-instructions-for-macos-mousecape)
7. [Applying the Theme](#7-applying-the-theme)

---

## 1. Overview of Cursor Themes to Convert

The repository contains six folders containing Windows 10 cursor definitions (`.cur` files and `install.inf`):
- [WB1.0-Mini](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.0-Mini) (Scheme Name: `Amiga WB1.0 Mini`)
- [WB1.0-Normal](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.0-Normal) (Scheme Name: `Amiga WB1.0`)
- [WB1.3-Mini](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.3-Mini) (Scheme Name: `Amiga WB1.3 Mini`)
- [WB1.3-Normal](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB1.3-Normal) (Scheme Name: `Amiga WB1.3`)
- [WB2.0-Mini](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB2.0-Mini) (Scheme Name: `Amiga WB2.0 Mini`)
- [WB2.0-Normal](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/WB2.0-Normal) (Scheme Name: `Amiga WB2.0`)

The target output is a set of `.tar.gz` (for Linux) and `.cape` (for macOS) archives in the `dist/` directory, ready to be distributed or extracted.

---

## 2. Prerequisites

### Linux/KDE
We use `win2xcur` to convert Windows `.cur` format to X11/KDE Xcursor format.
```bash
python3 -m venv venv
source venv/bin/activate
pip install win2xcur
```

### macOS
We use `capeify` to convert Windows `.cur` format to Mousecape `.cape` format.
```bash
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/mmemoo/capeify.git --ignore-requires-python
```
> [!NOTE]
> `capeify` requires `imagemagick` to extract frames and convert images. Install it via Homebrew (`brew install imagemagick`) or your package manager.

---

## 3. Conversion & Packaging Script Walkthrough

The [convert.py](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/convert.py) script automates the following actions:
1. **Parses the Windows `install.inf`** file to extract the official `SCHEME_NAME` for each theme.
2. **Derives a safe theme folder name** (e.g., `Amiga-WB1.0-Normal`).
3. **Generates Linux/KDE Cursors:**
   - Creates directory layouts, converts cursors, and generates the `index.theme` files.
   - Packages each theme directory into a `.tar.gz` archive in the `dist/` folder.
4. **Generates macOS Mousecape Cursors:**
   - Invokes `capeify` to automatically convert `.cur`/`.inf` configurations into a standard `.cape` theme file located in the `dist/` folder.
5. **Cleans up** temporary uncompressed files to keep the repository clean.

---

## 4. Execution Steps

Run the conversion and packaging script from the repository root:
```bash
python3 convert.py
```

Upon successful completion, a new folder `dist/` will be generated containing the packaged themes:
- `dist/Amiga-WB1.0.tar.gz` & `dist/Amiga-WB1.0.cape`
- `dist/Amiga-WB1.0-Mini.tar.gz` & `dist/Amiga-WB1.0-Mini.cape`
- `dist/Amiga-WB1.3.tar.gz` & `dist/Amiga-WB1.3.cape`
- `dist/Amiga-WB1.3-Mini.tar.gz` & `dist/Amiga-WB1.3-Mini.cape`
- `dist/Amiga-WB2.0.tar.gz` & `dist/Amiga-WB2.0.cape`
- `dist/Amiga-WB2.0-Mini.tar.gz` & `dist/Amiga-WB2.0-Mini.cape`

---

## 5. Installation Instructions for Linux/KDE

To install a cursor theme, simply create the user-level local icons folder (`~/.icons/`) if it does not exist, and extract the desired `.tar.gz` archive directly into it:

```bash
# Create the local icons directory if it doesn't exist
mkdir -p ~/.icons/

# Extract the desired theme (e.g. Amiga-WB1.0) into the ~/.icons/ directory
tar -xzf dist/Amiga-WB1.0.tar.gz -C ~/.icons/
```

---

## 6. Installation Instructions for macOS (Mousecape)

1. Download and install **Mousecape** (v0.2.8 or newer) from its official repository: [Mousecape GitHub](https://github.com/alexzielenski/Mousecape).
2. Open Mousecape.
3. Import the desired theme by dragging and dropping any `.cape` file (e.g., `dist/Amiga-WB1.0.cape`) from the `dist/` directory directly into the Mousecape window, or via **File > Import Cape...**.

---

## 7. Applying the Theme

### Applying in KDE Plasma (Linux)
* **GUI:** Open **System Settings > Appearance > Cursors** and select your preferred Amiga cursor theme.
* **CLI:** Use the KDE Plasma theme applicator:
  ```bash
  plasma-apply-cursortheme "Amiga WB1.0"
  ```

### Applying in Mousecape (macOS)
1. In Mousecape, select the imported Amiga theme from the list.
2. Right-click the theme and select **Apply** (or double-click the theme).
3. *Note: If cursors do not refresh instantly, you can toggle them off and on or restart your session.*
