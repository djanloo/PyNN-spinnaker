"""A very rude correction script for neo spiketrains"""
import numpy as np
import os

FOLDER = "/"+np.__file__.strip("numpy/__init__.py")
FILE = os.path.join(FOLDER, "neo/core/spiketrain.py")

with open(FILE, "r") as f:
    file_string = f.read()

modified = file_string.replace("np.float", "float")

with open(FILE, "w") as f:
    f.write(modified)
    
try:
    import neo
except AttributeError:
    print("correction of neo didn't go well. quitting.")
    exit()