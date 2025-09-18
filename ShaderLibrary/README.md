# ShaderLibrary – Blender Python Add-on (Shader Editor)

A **bpy** add-on for the **Shader Editor** that adds a panel with buttons to quickly create preset node setups (e.g., **Diamond**, metals, etc.).  
It demonstrates **custom operators** that build nodes and wire them together, then assign a new material to the active object.

> Inspired by Darkfall’s “Shader Library” tutorial (Blender Python Scripting Series).

---

## ✨ Features (v1)
- **Shader Library panel** in the Shader Editor (N-panel)
- **Custom Operator(s)** that:
  - Create a new material (e.g., `Diamond`)
  - Add required shader nodes programmatically
  - Position (`.location`) and **link** nodes
  - Assign the material to the active object
- Extensible: duplicate an operator as a template to add more shader presets

---

## 📦 Installation
1. Download `shader_library.py`.
2. Blender → **Edit ▸ Preferences ▸ Add-ons ▸ Install…**
3. Select `shader_library.py`, enable the add-on.
4. Open the **Shader Editor** → **N-panel** → look for the *Shader Library* tab/panel.

> Ensure you have an **active object** with a material slot to receive the created material.

---

## 🖼 Preview
*(Screenshots live in `/renders`)*

- Panel in Shader Editor  
  ![panel](renders/panel.png)
- Diamond nodes auto-created & linked  
  ![diamond_nodes](renders/diamond_nodes.png)

---

## 🧠 How It Works (High-level)
- **Panel**: `bpy.types.Panel` in `NODE_EDITOR` / `UI` region
- **Operator**: `bpy.types.Operator` builds nodes via `node_tree.nodes.new(...)`
- **Links**: `node_tree.links.new(output_socket, input_socket)`
- **Layout**: `node.location = (x, y)` for readable placement
- **Assign Material**: create (or reuse) a material and set it on the active object

---

## 📝 What I Learned (Notes)
- Creating **custom operators** vs. calling built-in ones
- Managing **node trees**: create, position, and link nodes programmatically
- Assigning newly created materials to the active object
- Panel/Operator **register/unregister** patterns

---

## ⚠️ Known gotchas
- Must be in the **Shader Editor** to see the panel (`NODE_EDITOR` space type).
- Requires an **active object**; otherwise assignment may fail.
- Some node names/sockets differ between Blender versions—tested on Blender **4.5.3**.

---

## 🗺 Roadmap
- Add more presets (Gold, Silver, Copper) with PBR-style parameters
- Popup dialog for parameters (e.g., IOR, roughness, color)
- Save/load custom presets to JSON

---

## 🙏 Credit
- Darkfall – Blender Python “Shader Library” tutorial