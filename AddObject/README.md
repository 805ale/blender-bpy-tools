# AddObject – Blender Python Add-on

A simple **bpy** add-on that adds a custom panel to the 3D View (N-panel) with quick buttons to create objects and two child panels for common actions.

## ✨ Features (v1.0)
- Main **Test Panel** with buttons:
  - Add **Cube**, **UV Sphere**, **Text**
- **Panel A – Scale**
  - `transform.resize` operator
  - Direct control of the active object’s **scale** property
- **Panel B – Specials**
  - **Shade Smooth** button
  - Quick access to **Subdivision** and **Modifier** operators
- Proper `bl_info` + installable as an add-on

<<<<<<< HEAD
## 📦 Installation
1. Download `AddObjectScript.py`.
2. Blender → **Edit ▸ Preferences ▸ Add-ons ▸ Install…**
3. Select `AddObjectScript.py`, then enable **Object Adder**.
4. Open the 3D View **N-panel** → tab **“My 1st Addon”**.
=======
## Screenshot
<img width="2557" height="1022" alt="panel" src="https://github.com/user-attachments/assets/ec6d787e-a13e-40b1-a1f0-4d45696f0b93" />
>>>>>>> adf3572f816323afcdd0eb3ad35db764e143983e

## 🖼 Preview

<<<<<<< HEAD


## 📝 Notes / What I learned
- Defining `bpy.types.Panel` with `bl_space_type='VIEW_3D'`, `bl_region_type='UI'`, custom `bl_category`.
- Creating **nested panels** via `bl_parent_id`.
- Calling built-in operators from UI rows (`mesh.primitive_cube_add`, `object.text_add`, `object.shade_smooth`).
- Register/unregister patterns and `bl_info` for installable add-ons.

## ⚠️ Known gotchas
- The **Scale** section needs an **active object**; otherwise the property won’t show.
- Some operators (e.g., `object.subdivision_set`, `object.modifier_add`) depend on context/selection.

## 🗺 Roadmap
- Popup dialog to set initial transform values on creation.
- Batch options (add multiple objects at once).
- Clean operator wrappers instead of calling built-ins directly.

## 🙏 Credit
Based on **Darkfall – Blender Python: Scripting Series**.
=======
## What I Learned
- How to create a custom Panel with `bpy.types.Panel`.
- How to register/unregister classes in Blender.
- How to link built-in operators to custom buttons.
>>>>>>> adf3572f816323afcdd0eb3ad35db764e143983e
