"""Builds from repos for sPyNNaker (cuurrent version is 1!6.0.1 at 12/05/23).

Basically follow the instructions at:

http://spinnakermanchester.github.io/spynnaker/6.0.0/PyNNOnSpinnakerInstall.html

with some fixes for the order of installation and Pynn/spinnaker setups.
Since it dowloads from repos it may take a while to complete the installation.

In case something goes wrong delete all the directories generated.

Since the version management is still work in progress, during installation may be raised warnings
like:

    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    spynnaker 1!6.0.1 requires lazyarray<=0.4.0,>=0.2.9, but you have lazyarray 0.5.2 which is incompatible.
    spynnaker 1!6.0.1 requires neo<0.10.0,>=0.5.2, but you have neo 0.12.0 which is incompatible.
    spynnaker 1!6.0.1 requires pynn<0.10.0,>=0.9.1, but you have pynn 0.10.2.dev0 which is incompatible.

These can be ignored.
"""
import os
from rich import print

dirs = ["PyNN", "SpiNNUtils", "SpiNNMachine", 
            "PACMAN", "SpiNNMan", "DataSpecification", 
            "spalloc","spalloc_server", "SpiNNFrontEndCommon", 
            "sPyNNaker"]


# IMPORTANT NOTE: order of repos is freaking important
repos = [   "git@github.com:NeuralEnsemble/PyNN.git",
            "git@github.com:SpiNNakerManchester/SpiNNUtils.git",
            "git@github.com:SpiNNakerManchester/SpiNNMachine.git",
            "git@github.com:SpiNNakerManchester/PACMAN.git",
            "git@github.com:SpiNNakerManchester/SpiNNMan.git",
            "git@github.com:SpiNNakerManchester/DataSpecification.git",
            "git@github.com:SpiNNakerManchester/spalloc.git",
            "git@github.com:SpiNNakerManchester/spalloc_server.git",
            "git@github.com:SpiNNakerManchester/SpiNNFrontEndCommon.git",
            "git@github.com:SpiNNakerManchester/sPyNNaker.git"]

repomap = {d:r for d,r in zip(dirs, repos)}


# Installs pyNN and manchester stuff from repos
for directory in dirs:
    print(f"[green]Installing {directory}[/green]")
    # Downloads it if it has not been done previously
    if not os.path.exists(directory):
        os.system(f"git clone {repomap[directory]}")

    # Installs
    os.chdir(directory)
    os.system("pip install .")
    os.chdir("..")
print("[blue]Installation complete[/blue]")
print("[green]Setting up pyNN for spinnaker[\green]")
try:
    os.system("python -m spynnaker.pyNN.setup_pynn")
except Exception as e:
    print("[red]Something went wrong[/red]")
    print(e)
else:
    print("[green]Done[/green]")