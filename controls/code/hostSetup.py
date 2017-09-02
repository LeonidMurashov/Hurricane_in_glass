import sys
from cx_Freeze import setup, Executable

opt = {"packages":["os"], "excludes":[]}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"
elif sys.platform == 'win64':
    base = "Win64GUI"

setup(
        name = "AtomicHost",
        version = "0.1",
        description = "Host for Atomic",
        options = {"build_exe" : opt},
        executables = [Executable("rpiReciev.py", base)]
        )
