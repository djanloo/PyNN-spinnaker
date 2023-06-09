"""Small test for SpikeSourcePoisson
"""
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from pyNN.random import NumpyRNG, RandomDistribution
from pyNN.utility import SimulationProgressBar
from pyNN.utility.plotting import plot_spiketrains
import pyNN.spiNNaker as sim
from time import perf_counter

simulation_time = 10
excitatory_strength = 0.05
inhibitory_strength = 1.0
connection_probability = 0.05

dt = 0.05
N = 1000

sim.setup(timestep=dt)
print("setup complete")

# Neurons
bombing_population = sim.Population(1, sim.SpikeSourcePoisson(rate=500))
target_population = sim.Population(N, sim.IF_cond_exp())
calming_population = sim.Population(N//4, sim.IF_cond_exp())

print("population complete")

# Connections
bombing_connections = sim.Projection(   bombing_population, target_population, 
                                sim.AllToAllConnector(), 
                                sim.StaticSynapse(weight=0.05, delay=0.5), 
                                receptor_type='excitatory')
print("connections 1/4")
self_connections = sim.Projection(target_population, target_population,
                                  sim.FixedProbabilityConnector(connection_probability),
                                  sim.StaticSynapse(weight=excitatory_strength/N/connection_probability, delay=0.5))
print("connections 2/4")
calming_connections = sim.Projection(calming_population, target_population,
                                     sim.AllToAllConnector(),
                                     sim.StaticSynapse(weight=inhibitory_strength/N, delay=0.8))
print("connections 3/4")

calm_stimulating = sim.Projection(   target_population, calming_population,
                                     sim.AllToAllConnector(),
                                     sim.StaticSynapse(weight=excitatory_strength/N, delay=0.05))
print("connections done")

# Define recording variables
target_population.record(("v", "spikes"))

# Starts the simulation
start = perf_counter()
print("starting")
sim.run(simulation_time, callbacks=[SimulationProgressBar(100*dt, simulation_time)])
runtime = perf_counter() - start
print(f"run time: {runtime}")

# Plots the data
block = target_population.get_data()
print(f"{len(block.segments)} segments of block found")

fig, (axspike, axv) = plt.subplots(2,1, sharex=True)
for signal in block.segments[0].analogsignals:
    axv.plot(signal.times, signal.magnitude)
plot_spiketrains(axspike,block.segments[0].spiketrains )
axspike.set_title(f"Runtime: {runtime:.3f} s")
fig.savefig(f"results_{sim.__name__}.png")