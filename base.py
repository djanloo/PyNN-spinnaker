import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from pyNN.random import NumpyRNG, RandomDistribution
from pyNN.utility import SimulationProgressBar
from pyNN.utility.plotting import plot_spiketrains
import pyNN.spiNNaker as sim

module_dict=dict()
def module_explorer(object, iter):
    global module_dict
    try:
        obj_name= object.__name__
        try:
            desc = object.__dict__
            if iter > 0:
                if len(desc) > 0 and not obj_name.startswith("?"):
                    module_dict[object.__name__] =[sub_obj for sub_obj in list(desc.keys()) if not sub_obj.startswith("?")]#{sub_obj:{"weight":1/iter} for sub_obj in desc.keys() if not sub_obj.startswith("?")}#
                for sub_obj in desc.values():
                    module_explorer(sub_obj, iter-1)
        except Exception as e:
            pass
    except Exception:
        pass
    print(iter, end=" ")
module_explorer(sim, 2)
with open("sim_description.txt", "w") as f:
    for key in module_dict.keys():
        f.write(f"{key}\n\t{str(module_dict[key])}\n")



simulation_time = 100
dt = 0.1
sim.setup(timestep=dt)

# Neurons
single_neuron = sim.IF_cond_exp()
population = sim.Population(10, single_neuron)
population.record(("v", "spikes"))

# Connections
synapse = sim.StaticSynapse(weight=0.015, 
                            delay=0.5)

random_conn = sim.FixedProbabilityConnector(0.3)

connections = dict(self_connections = sim.Projection(population, population, 
                                                    random_conn, synapse, 
                                                    receptor_type='excitatory'))

# Injection
current = sim.DCSource(amplitude=5.0, start=0.0, stop=50.0)
# current = sim.NoisyCurrentSource(mean=5.5, stdev=1.0, start=0.0, stop=450.0, dt=dt)
current.inject_into(population[0:2])

sim.run(simulation_time, callbacks=[SimulationProgressBar(100*dt, simulation_time)])
print()

# Plot data
block = population.get_data()
print(f"{len(block.segments)} segments of block found")

fig, (axspike, axv) = plt.subplots(2,1, sharex=True)
for signal in block.segments[0].analogsignals:
    axv.plot(signal.times, signal.magnitude)
plot_spiketrains(axspike,block.segments[0].spiketrains )
fig.savefig(f"results_{sim.__name__}.png")