bl_info = {
    "name" : "Object Adder",
    "author" : "805ale",
    "version" : (1, 0),
    "blender": (4, 5, 3),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
}


import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Add an Object", icon = 'MESH_CUBE')
        row = layout.row()
        row.operator("wm.myop", icon = 'MESH_CUBE', text = "Add Cube")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = 'SPHERE')
        row = layout.row()
        row.operator("object.text_add")
        
        layout.scale_y = 1.2
        
        
        
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        
        if obj:
            row = layout.row()
            row.label(text="Select an option to scale your object", icon='FONT_DATA')
            row = layout.row()
            row.operator("transform.resize")
            row = layout.row()
            layout.scale_y = 1.2

            col = layout.column()
            col.prop(obj, "scale")
        
        else:
            col = layout.column()
            col.label(text="⚠ No active object selected", icon='INFO')
        
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Select a Special Option", icon = 'COLOR_BLUE')
        
        row = layout.row()
        row.operator("object.shade_smooth", icon = 'MOD_SMOOTH', text = "Set Smooth Shading")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")
        layout.scale_y = 1.2
 
        
        
class WM_OT_myOp(bpy.types.Operator):
    """Open the Add Cube Dialog Box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.myop"
    bl_options = {'REGISTER', 'UNDO'}
    
    text: bpy.props.StringProperty(name = "Enter Text", default = "")
    
    scale: bpy.props.FloatVectorProperty(name = "Scale", default = (1, 1, 1))
    
    def execute(self, context):
        
        t = self.text
        s = self.scale
        
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.object
        obj.name = t
        obj.scale[0] = s[0]
        obj.scale[1] = s[1]
        obj.scale[2] = s[2]
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)
            
        
        
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    bpy.utils.register_class(WM_OT_myOp)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    bpy.utils.unregister_class(WM_OT_myOp)
    
    
if __name__ == "__main__":
    register()
