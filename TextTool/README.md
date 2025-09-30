# Text Tool (Blender Add-on)

Create text objects quickly from the 3D Viewport sidebar, with options for scale, centering, and extrusion.

## Features
- Enter custom text
- Set overall scale
- Optional center alignment (X/Y)
- Optional extrusion with adjustable amount

## Installation
1. **Download/clone** this repo.
2. In Blender: `Edit > Preferences > Add-ons > Install...`
3. Select the **TextTool** folder (it must contain `__init__.py`).
4. Enable **Text Tool**.

## Usage
- Open the **3D Viewport**.
- Open the **Sidebar (N)** → **Text Tool** tab.
- Click **Add Text**, fill the dialog (Text, Scale, Center Origin, Extrude, Extrude Amount), then **OK**.

## Requirements
- Blender 4.5.x (tested on 4.5.3)

## Notes
- Category is “Add Mesh” for visibility, even though Blender creates a FONT curve object.
- If you prefer a minimal install as a single file, rename `__init__.py` and install that file directly.
