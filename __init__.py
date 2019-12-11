import bpy

bl_info = {
    "name":"Add_empty_mesh",
    "author": "iCyP",
    "version": (0, 1),
    "blender": (2, 81, 0),
    "location": "3D View->Tools",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"
}


class ICYP_OT_make_empty_mesh(bpy.types.Operator):
    bl_idname = "mesh.empty_mesh"
    bl_label = "Add empty mesh"
    bl_description = "Add empty mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self,context):
        m = bpy.data.meshes.new("empty_mesh")
        o = bpy.data.objects.new("empty_mesh",m)
        context.scene.collection.objects.link(o)
        o.location = context.scene.cursor.location
        context.view_layer.objects.active = o
        ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

def icyp_empty_mesh_menu(self, context):
    self.layout.menu(ICYP_OT_make_empty_mesh.bl_idname,
                     text="EMPTY MESH", icon="PLUGIN")    
                     
cls = [ICYP_OT_make_empty_mesh]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.append(icyp_empty_mesh_menu)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.remove(icyp_empty_mesh_menu)

