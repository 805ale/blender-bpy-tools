bl_info = {
    "name": "Text Tool",
    "author": "805ale",
    "version": (1, 0),
    "blender": (4, 5, 3),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy


class OBJECT_PT_TextTool(bpy.types.Panel):
    bl_label = "Text Tool"
    bl_idname = "OBJECT_PT_TextTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Text Tool'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("wm.textop", text = "Add Text")
        
        
        
class WM_OT_textOp(bpy.types.Operator):
    bl_label = "Text Tool Operator"
    bl_idname = "wm.textop"
    
    text: bpy. props.StringProperty(name = "Enter Text:")
    scale: bpy.props.FloatProperty(name = "Scale:", default = 1)
    center: bpy.props.BoolProperty(name = "Center Origin", default = False)
    extrude: bpy.props.BoolProperty(name = "Extrude", default = False)
    extrude_amount: bpy.props.FloatProperty(name = "Extrude Amount:", default = 0.06)


    def execute(self, context):
        
        t = self.text
        s = self.scale
        c = self.center
        e = self.extrude
        ea = self.extrude_amount
        
        bpy.ops.object.text_add(enter_editmode = True, location = (0, 0, 0))
        bpy.ops.font.delete(type = 'PREVIOUS_WORD')
        bpy.ops.font.text_insert (text = t)
        bpy.ops.object.editmode_toggle()
    
        
        if e == True:
            bpy.context.object.data.extrude = ea
        
        
        if c == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'
        
        
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


        
        
def register():
    bpy.utils.register_class(OBJECT_PT_TextTool)
    bpy.utils.register_class(WM_OT_textOp)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_PT_TextTool)
    bpy.utils.unregister_class(WM_OT_textOp)
    
    
if __name__ == "__main__":
    register()