import hou # type: ignore
import os
import re
import pathlib

def save_version():
    filepath = hou.hipFile.path()
    
    base_path, ext = os.path.splitext(filepath)
    
    version_match = re.search(r'(_v|_)(\d+)$', base_path)
    
    if version_match:
        version_num = int(version_match.group(2)) + 1
        prefix = version_match.group(1)
        new_base = re.sub(r'(_v|_)\d+$', f'{prefix}{version_num:03d}', base_path)
    else:
        new_base = f"{base_path}_v001"
    
    new_filepath = f"{new_base}{ext}"
    hou.hipFile.save(file_name=new_filepath)