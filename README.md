# Predator - Prey Simulation
This repository contains a simulation of an _ecosystem_, where agents (predators and prey) interact within a grid-based environment. \\
The goal of the simulation is to explore population dynamics, agent behaviors, and the emergent patterns arising from simple rules. \\
Instead of using the classic [Lotka-Volterra](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) differential equations, \\
this model simulates the behaviour of each agent using _object-oriented programming_ and observes the population dynamics over time.

[video](videos_and_graphs/experiment_11-15-18-18-29.mp4)

## Changeable Parameters
The user-specified parameters can be found in the `config.yaml`. 

- `steps`: number of times the simulation is run;
- `(width, height)`: dimensions of the environment;
- `preys-count`: initial number of preys in the environment;
- `predators-count`: initial number of predators in the environment;
- `breed_age`: minimum age to start breeding;
- `maximum age`: maximum allowed age before dying of natural causes;
- `breed_prob`: probability to breed at every step (defined as mean and std);
- `hunt_prob`: probability to hunt at every step (defined as mean and std and only for predators);
- `hunting_range`: maximum observable space for every predator, measured in number of nearby cells;
- `max_starve_time`: maximum time a predator can stay without eating.

Changing this parameters will affect the population dynamics and it can be done to explore different scenarios. 

## Use Cases:
- Study population dynamics and predator-prey interactions.
- Explore the effects of probabilistic parameters on ecosystem stability.
- Visualize emergent behavior in agent-based systems.
