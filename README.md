# Blender CLI Exporter

This is a little script to help batch exporting models from .blend files to other formats. You can use this script as a part of your asset pipeline.

All objects are exported to different files. Filename is same as the object's name in blender.

This script is currently compatible with Blender v2.77a.

## Usage

Example:

```
blender -b blendfile.blend --python export.py -- -t fbx -p ../models
```

### Arguments

- Export type `-t`
  - Currently supported: `g3dj, g3db, obj, fbx, dae`
- Filepath `-p`
- File extension `-e`
  - If not defined, export type is used.

### Notes
- If using `-p`, make sure that the folder is created.
- When exporting `g3dj` or `g3db` blender extension [libgdx_blender_g3d_exporter](https://github.com/Dancovich/libgdx_blender_g3d_exporter) by Dancovich needs to be installed.
- When exporting `g3dj` or `g3db` models will need to have at least one material attached.
