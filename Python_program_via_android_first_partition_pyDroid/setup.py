import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
setup(  name = "limit",
        version = "0.1",
        description = "My limit application",
        #options = {"build_exe": build_exe_options},
        executables = [Executable("limit.py", base=base)])