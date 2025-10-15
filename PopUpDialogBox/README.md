# 🧊 Add Cube Dialog Box – Blender Operator Script

A simple Blender Python script that demonstrates how to create a **custom operator** with an **interactive dialog box**.  
When executed, it opens a small window where you can enter a cube name and set its scale before adding it to the scene.

---

## ✨ Features

- Opens a **custom dialog box** using `invoke_props_dialog()`.
- Lets you:
  - Enter a **name** for your cube.
  - Adjust the **X, Y, Z scale** interactively.
- Automatically adds a cube to the scene with the chosen settings.
- Fully undoable (`bl_options = {'REGISTER', 'UNDO'}`).

---

## 🧠 How It Works

When the operator runs (`bpy.ops.wm.myop('INVOKE_DEFAULT')`):
1. Blender displays a small pop-up dialog with:
   - A text box for the cube’s name.
   - A 3-component scale vector.
2. After confirming, it:
   - Adds a cube to the scene.
   - Sets its name and scale according to your input.

---

## 🧰 Installation & Usage

1. Save the script as `AddCubeDialogBox.py`.

2. In Blender, open **Scripting → Text Editor** and **load the script**.

3. Press **Run Script**.

4. The dialog will automatically appear (because of the `bpy.ops.wm.myop('INVOKE_DEFAULT')` line).

   Alternatively, after registering, you can run it manually from the Python console:
   ```python
   bpy.ops.wm.myop('INVOKE_DEFAULT')