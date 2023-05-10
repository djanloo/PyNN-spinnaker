"""A very rude correction script for neo spiketrains"""
import numpy as np
import os

# Gets the folder of packages
FOLDER = "/"+np.__file__.strip("numpy/__init__.py")
FILE = os.path.join(FOLDER, "neo/core/spiketrain.py")

# Opens neo.core.spiketrain
with open(FILE, "r") as f:
    file_string = f.read()

# Corrects the error
modified = file_string.replace("np.float", "float")

with open(FILE, "w") as f:
    f.write(modified)

# Check for neo import
try:
    import neo
except AttributeError:
    print("Correction of neo didn't go well. quitting.")
    exit()

## Sets up pyNN.spinnaker
os.system("python3 -m spynnaker8.setup_pynn")