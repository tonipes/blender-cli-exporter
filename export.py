import sys
import bpy
import os

# Format for filename
FILENAME = "{obj_name}.{file_ext}"

# Exporter functions
EXPORT_FUNC = {
    'g3dj': bpy.ops.export_json_g3d.g3dj,
    'g3db': bpy.ops.export_json_g3d.g3db,
    'obj': bpy.ops.export_scene.obj,
    'fbx': bpy.ops.export_scene.fbx,
    'dae': bpy.ops.wm.collada_export,
}

# Keyword arguments for different exporters
KWARGS = {
    'g3dj': {'useSelection': True},
    'g3db': {'useSelection': True},
    'dae': {'selected': True},
}
DEFAULT_KWARGS = {'use_selection': True}

def has_arg(argv, name):
    return name in argv

def get_arg(argv, name):
    return argv[argv.index(name) + 1] if has_arg(argv, name) else None

def main():
    argv = sys.argv

    # We only use arguments after "--"
    i = argv.index("--") if "--" in argv else None
    argv = argv[argv.index("--") + 1:] if i else None

    # Get arguments
    file_type = get_arg(argv, "-t")
    file_path = get_arg(argv, "-p")
    file_path = file_path if file_path else ""
    file_ext = get_arg(argv, "-e")
    file_ext = file_ext if file_ext else file_type

    export(file_type, file_path, file_ext)

def export(file_type, file_path, file_ext):
    # Set object mode and deselect all objects
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    # Iterate through all objects
    for obj in bpy.data.objects:
        obj.select = True

        path = os.path.join(file_path, FILENAME.format(
            obj_name=obj.name,
            file_ext=file_ext
        ))
        kwargs = KWARGS[file_type] if file_type in KWARGS else DEFAULT_KWARGS

        print("Exporting {}".format(path))

        # Export with current obj selected
        EXPORT_FUNC[file_type](
            filepath=path,
            **kwargs
        )

        obj.select = False

main()