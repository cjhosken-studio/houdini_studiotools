name = "houdini_studiotools"
version = "1.0.0"

requires = [
    "python-3.11",
    "houdini"
]

build_command = "python {root}/build.py {install}"

def commands():
    env.PYTHONPATH.prepend("{root}/python")
    env.HOUDINI_TOOLBAR_PATH.append("{root}/houdini/toolbar:&")
    env.HOUDINI_OTLSCAN_PATH.append("{root}/houdini/otls:&")
    env.HOUDINI_MENU_PATH.append("{root}/houdini:&")