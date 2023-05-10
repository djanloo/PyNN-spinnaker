"""A very rude correction script for neo spiketrains"""
import os

dirs = ["PyNN", "SpiNNUtils", "SpiNNMachine", "SpiNNMan", 
            "PACMAN", "SpiNNMan", "DataSpecification", 
            "spalloc","spalloc_server", "SpiNNFrontEndCommon", 
            "sPyNNaker"]

pyNN_repo = "git@github.com:NeuralEnsemble/PyNN.git"

# IMPORTANT NOTE: order of repos is freaking important
spinnaker_git_repos = [ "git@github.com:SpiNNakerManchester/SpiNNUtils.git",
                        "git@github.com:SpiNNakerManchester/SpiNNMachine.git",
                        "git@github.com:SpiNNakerManchester/PACMAN.git",
                        "git@github.com:SpiNNakerManchester/SpiNNMan.git",
                        "git@github.com:SpiNNakerManchester/DataSpecification.git",
                        "git@github.com:SpiNNakerManchester/spalloc.git",
                        "git@github.com:SpiNNakerManchester/spalloc_server.git",
                        "git@github.com:SpiNNakerManchester/SpiNNFrontEndCommon.git",
                        "git@github.com:SpiNNakerManchester/sPyNNaker.git"]



repos = [pyNN_repo] + spinnaker_git_repos
repomap = {d:r for d,r in zip(dirs, repos)}


# Installs pyNN and manchester stuff from repos
for directory in dirs:

    # Downloads it if it has not been done previously
    if not os.path.exists(directory):
        os.system(f"git clone {repomap[directory]}")

    # Installs
    os.chdir(directory)
    os.system("pip install .")
    os.chdir("..")

os.system("python -m spynnaker.pyNN.setup_pynn")

exit()
import numpy as np

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

# # Corrects neuron
# try:
#     import neuron
#     try:
#         import pyNN.neuron
#     except OSError and TypeError:
#         NEURON_FOLDER = os.path.join(FOLDER, "pyNN/neuron/nmodl")
#         print()
#         print("Correcting neuron")
#         print(NEURON_FOLDER)
#         print()
#         os.chdir(NEURON_FOLDER)
#         os.system("nrnivmodl")
# except ImportError as e:
#     print("neuron is not installed: correction not applied")

print("Correction went fine")
