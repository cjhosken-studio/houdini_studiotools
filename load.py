import hou
import os
import sys

# Get the target file path from the command line
if len(sys.argv) < 2:
    raise ValueError("Missing target Houdini file path")

hip_path = sys.argv[1]

# Ensure directory exists
os.makedirs(os.path.dirname(hip_path), exist_ok=True)

# Create new Houdini scene
hou.hipFile.clear(suppress_save_prompt=True)

# Optionally create a geo node
geo = hou.node("/obj").createNode("geo", "my_geo_node")

# Save the new file
hou.hipFile.save(hip_path)

print(f"Created new Houdini file at: {hip_path}")