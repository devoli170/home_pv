from sys import path as sys_path
import os.path as path
from os import getcwd
sys_path.insert(0,path.abspath(path.join(getcwd() ,"../..")))
__all__ = ["main.py", "Pin.py", "StromSteuerung.py"]