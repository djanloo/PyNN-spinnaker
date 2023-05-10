# PyNN-spinnaker
Settings and tests for Spinnaker on PyNN

## Installation
I'm using Ubuntu Ubuntu 22.04.2 LTS and I had a few problems while installing sPyNNaker using [this guide](http://spinnakermanchester.github.io/spynnaker/6.0.0/PyNNOnSpinnakerInstall.html) for spinnaker 6.0.0.

### neo `np.float`
sPyNNaker 6.0.0 requires neo < 0.10.0, that has a `numpy` compatibility issue (`np.float` is used yet deprecated).

Solved editing the `neo.core.spiketrains` module and replacing `np.float` with `float`


