import os
import pathlib

path = pathlib.Path(__file__).resolve()
parent_path = pathlib.Path(__file__).parent.resolve()
parent_parent_path = pathlib.Path(__file__).parent.parent.resolve()

print("Path: ", path)
print("Parent directory path: ", parent_path)