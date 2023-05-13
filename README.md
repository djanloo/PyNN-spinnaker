# PyNN-spinnaker
Settings and tests for Spinnaker on PyNN

## Installation
A python3.8 installation is required:

```
sudo apt install python3.8 python3.8-dev python3.8-tk
```

To install with pipenv (highly recommended) run:

```
pipenv install
pipenv shell
python build_from_source.py
```

In case python alias is not set run `python3 build_from_source.py` instead of the last line.

## Send to server

To send on spinnaker:

- insert in `send.py` your EBRAINS username, password & collab id
- run `python send.py <file>`
- wait :)

## Description

- `build_from_source.py` downloads latest version of used repos and installs them
- `simulation.py` is the (dummy) file to send as a simulation to spinnaker
- `send.py` sends and fetches the job results

## Log of errors (for memory purpose only)
I'm using Ubuntu Ubuntu 22.04.2 LTS and I had a few problems while installing sPyNNaker using [this guide](http://spinnakermanchester.github.io/spynnaker/6.0.0/PyNNOnSpinnakerInstall.html) for spinnaker 6.0.0.

### neo `np.float`
sPyNNaker 6.0.0 requires neo < 0.10.0, that has a `numpy` compatibility issue (`np.float` is used yet deprecated).

Solved editing the `neo.core.spiketrains` module and replacing `np.float` with `float`

### spinnaker setup script
The script to setup PyNN to work on spinnaker is

`python -m spynnaker.pyNN.setup_pynn`

and not 

`python -m spynnaker8.setup_pynn`

as explained in the installation guide.

### connection from config file (?)

As it seems to be stated [here](https://groups.google.com/g/spinnakerusers/c/ySTiD4WCktU), the execution of code on Manchester's machine is recommended through the _batch submission system_. I am not completely sure of the impossibility to run just simply with a remote configuration:


```
[Machine]

machineName = _name_
version = _v_

spalloc_server = spinnaker.cs.man.ac.uk
spalloc_port = 22244
spalloc_user = _user_
```

even if I continue to get [SpinnmanIOException](https://spinnman.readthedocs.io/en/latest/spinnman/?highlight=ioexception#spinnman.exceptions.SpinnmanIOException).