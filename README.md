# Amiga Workbench Mouse Cursors for Windows 10

### Workbench 2.0
|Normal|Mini|
|---|---|
|![WB2 0-Normal-preview](https://user-images.githubusercontent.com/45124675/90980081-d5d02d80-e561-11ea-8b6e-556cd39d76aa.png)|![WB2 0-Mini-preview](https://user-images.githubusercontent.com/45124675/90980086-dcf73b80-e561-11ea-9442-3da3feffd2a5.png)|

### Workbench 1.0
|Normal|Mini|
|---|---|
|![WB1 0-Normal-preview](https://user-images.githubusercontent.com/45124675/90980070-c6e97b00-e561-11ea-88f5-c89dfd6d4a3b.png)|![WB1 0-Mini-preview](https://user-images.githubusercontent.com/45124675/90980075-d072e300-e561-11ea-94a8-0750f8b259b8.png)|

### Workbench 1.3
|Normal|Mini|
|---|---|
|![WB1 3-Normal-preview](https://user-images.githubusercontent.com/45124675/130702076-6f161db0-55d7-43c0-a61d-a39e6edfd370.png)|![WB1 3-Mini-preview](https://user-images.githubusercontent.com/45124675/130702083-325bc9a6-5a01-4b74-b0ab-0ef88a7fb01f.png)|

---

## Linux/KDE & macOS Installation

You can convert and install these Windows 10 cursor schemes to Xcursor themes for KDE Plasma (Linux) and `.cape` themes for Mousecape (macOS).

A detailed setup plan is available in [gotolinux.md](file:///gorgon/dev/Amiga-Workbench-Mouse-Cursors/gotolinux.md).

### Quick Start:

1. **Install Prerequisites & Tools:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install win2xcur
   pip install git+https://github.com/mmemoo/capeify.git --ignore-requires-python
   ```

2. **Run Conversion & Packaging Utility:**
   ```bash
   python3 convert.py
   ```
   This generates `.tar.gz` and `.cape` files inside the `dist/` directory.

3. **Install Themes:**
   * **Linux/KDE:** Extract the desired `.tar.gz` theme package into your local `~/.icons/` directory:
     ```bash
     mkdir -p ~/.icons/
     tar -xzf dist/Amiga-WB1.0.tar.gz -C ~/.icons/
     ```
     Then apply it via **System Settings > Appearance > Cursors** or via CLI:
     ```bash
     plasma-apply-cursortheme "Amiga WB1.0"
     ```
   * **macOS (Mousecape):** Install [Mousecape](https://github.com/alexzielenski/Mousecape) and drag & drop the desired `.cape` file (e.g. `dist/Amiga-WB1.0.cape`) into the Mousecape window. Right-click the theme and select **Apply**.



