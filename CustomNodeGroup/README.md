# 🧩 Custom Node Group – Blender Add-on

A simple Blender add-on that creates a **custom compositor node group** programmatically using Python.  
This project was made as part of my Blender scripting learning journey.

---

## ✨ Features

- Adds a new **UI panel** in the **Compositor Node Editor** under the “New Tab” sidebar.  
- Provides a button to **generate a custom node group** automatically.
- The generated node group includes:
  - Group input and output nodes.
  - A **Box Mask** node.
  - A **Mix RGB** node with overlay blend mode.
- Automatically connects all nodes together for quick testing.

---

## 🧠 How It Works

When you click **“Add Custom Node Group”** in the panel:
1. The script ensures compositor nodes are enabled.
2. It creates a new node group (`CompositorNodeTree`).
3. Adds sockets and internal nodes.
4. Links them automatically.
5. Inserts the node group into your current compositor node tree.

---

## 🧰 Installation

1. Download or clone this repository:
   ```bash
   git clone https://github.com/yourusername/CustomNodeGroup.git