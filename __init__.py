import hou # type: ignore
import os
import re

def get_latest_version():
    filepath = hou.hipFile.path()
    
    wip_folder = os.path.dirname(os.path.dirname(filepath))
    version_pattern = re.compile(r'_v(\d+)$', re.IGNORECASE)
    
    max_version = 0
    
    for app_folder in os.listdir(wip_folder):
        app_folder_path = os.path.join(wip_folder, app_folder)
        
        if not os.path.isdir(app_folder_path):
            continue
        
        for app in os.listdir(os.path.join(wip_folder, app_folder)):
            name, ext = os.path.splitext(app)
            match = version_pattern.search(name)
            if match:
                ver = int(match.group(1))
                if ver > max_version:
                    max_version = ver
            # check for _v***
            # return the newest version
            
    return max_version

def save_version():
    filepath = hou.hipFile.path()
    base_path, ext = os.path.splitext(filepath)
    base_name = os.path.basename(base_path).split("_v")[0]
    
    latest_version = get_latest_version()
    next_version = latest_version + 1
        
    new_base = os.path.join(os.path.dirname(base_path), f"{base_name}_v{next_version:03d}")
    new_filepath = f"{new_base}{ext}"
    hou.hipFile.save(file_name=new_filepath)