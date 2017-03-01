from distutils.core import setup
import py2exe
from glob import glob
data_files = [("Microsoft.VC100.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 10.0\VC\redist\x86\Microsoft.VC100.CRT\*.*'))]

setup( data_files=data_files,
       console = ['setup_loc.py'])
