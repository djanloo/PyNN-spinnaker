# PyNN-spinnaker
Settings and tests for Spinnaker on PyNN

## Installation

To install with pipenv (higly recommended) run:

```
pipenv install
pipenv shell
python build_from_source.py
```

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
