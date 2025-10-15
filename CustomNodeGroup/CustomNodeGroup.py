import bpy

class NODE_PT_MAINPANEL(bpy.types.Panel):
    bl_label = "Custom Node Group"
    bl_idname = "NODE_PT_MAINPANEL"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'New Tab'

    def draw(self, context):
        self.layout.operator('node.test_operator')

def create_test_group(context, group_name):
    # Ensure Compositor nodes are enabled
    context.scene.use_nodes = True

    # Create a Compositor node group
    test_group = bpy.data.node_groups.new(group_name, 'CompositorNodeTree')

    # Group I/O nodes in the group
    group_in  = test_group.nodes.new('NodeGroupInput')
    group_out = test_group.nodes.new('NodeGroupOutput')
    group_in.location  = (-200, 0)
    group_out.location = (400, 0)

    # Define interface sockets (Blender 4.x)
    io = test_group.interface
    io.new_socket("Factor Value", in_out='INPUT',  socket_type='NodeSocketFloat')
    io.new_socket("Color Input",  in_out='INPUT',  socket_type='NodeSocketColor')
    io.new_socket("Output",       in_out='OUTPUT', socket_type='NodeSocketColor')

    # Internal nodes
    mask_node = test_group.nodes.new(type='CompositorNodeBoxMask')
    mask_node.location = (0, 0)
    mask_node.rotation = 1.0

    mix_node = test_group.nodes.new(type='CompositorNodeMixRGB')
    mix_node.location = (200, 0)
    mix_node.use_clamp = True
    mix_node.blend_type = 'OVERLAY'

    # Links
    link = test_group.links.new
    link(mask_node.outputs[0], mix_node.inputs[1])   # Mask -> Mix Color1
    link(group_in.outputs[0],  mix_node.inputs[0])   # Factor -> Fac
    link(group_in.outputs[1],  mix_node.inputs[2])   # Color  -> Color2
    link(mix_node.outputs[0],  group_out.inputs[0])  # Mix -> Output

    return test_group

class NODE_OT_TEST(bpy.types.Operator):
    bl_label = "Add Custom Node Group"
    bl_idname = "node.test_operator"

    def execute(self, context):
        custom_node_name = "Test Node"
        my_group = create_test_group(context, custom_node_name)

        # Add the group as a node in the current scene compositor tree
        ntree = context.scene.node_tree
        test_node = ntree.nodes.new('CompositorNodeGroup')
        test_node.node_tree = my_group
        test_node.use_custom_color = True
        test_node.color = (0.5, 0.4, 0.3)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(NODE_PT_MAINPANEL)
    bpy.utils.register_class(NODE_OT_TEST)

def unregister():
    bpy.utils.unregister_class(NODE_PT_MAINPANEL)
    bpy.utils.unregister_class(NODE_OT_TEST)

if __name__ == "__main__":
    register()