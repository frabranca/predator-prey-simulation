from agents import Predator, Prey
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Environment:
    def __init__(self, width, height, prey_count, predator_count, max_starve_time, hunt_prob, hunting_range, max_age, reproduce_prob, reproduce_age):
        self.width = width
        self.height = height
        self.space = [[None for _ in range(width)] for _ in range(height)]
        # Randomly populate the environment with preys and predators
        self.populate(prey_count, predator_count, max_starve_time, hunt_prob, hunting_range, max_age, reproduce_prob, reproduce_age)
    
    def populate(self, prey_count, predator_count, max_starve_time, hunt_prob, hunting_range, max_age, reproduce_prob, reproduce_age):
        # Place preys randomly
        if prey_count > 0:
            for _ in range(prey_count):
                x, y = self.random_empty_cell()
                self.space[x][y] = Prey(x, y, self.space, reproduce_prob, reproduce_age)
        
        # Place predators randomly
        if predator_count > 0:
            for _ in range(predator_count):
                x, y = self.random_empty_cell()
                self.space[x][y] = Predator(x, y, self.space, max_starve_time, hunt_prob, hunting_range, max_age, reproduce_prob, reproduce_age)
            
    def random_empty_cell(self):
        # Get a random empty cell in the space
        while True:
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.space[x][y] is None:
                return x, y
            
    def age_up(self):
        # Increase the age of all organisms
        for row in self.space:
            for cell in row:
                if cell is not None:
                    cell.age_up()
    
    def step(self):
        # Perform one simulation step: move, hunt, reproduce
        for row in self.space:
            for cell in row:
                if isinstance(cell, Prey):
                    if cell.is_alive:
                        self.space[cell.x][cell.y] = None
                        cell.move()    # Prey moves
                        self.space[cell.x][cell.y] = cell
                        cell.reproduce()  # Prey reproduces if possible
                    else:
                        self.space[cell.x][cell.y] = None

                elif isinstance(cell, Predator):
                    if cell.is_alive:
                        self.space[cell.x][cell.y] = None
                        cell.move()    # Predator moves
                        self.space[cell.x][cell.y] = cell
                        cell.reproduce()  # Predator reproduces if possible
                    else:
                        self.space[cell.x][cell.y] = None
            
        # print('Preys alive:', preys_alive)
        # print('Predators alive:', predators_alive)

    def get_space(self):
        # Convert the environment into a numerical grid for plotting
        space_state = np.zeros((self.height, self.width))
        for i in range(self.height):
            for j in range(self.width):
                if isinstance(self.space[i][j], Prey):
                    space_state[i, j] = 1
                elif isinstance(self.space[i][j], Predator):
                    space_state[i, j] = 2
        return space_state

# Running the simulation
# Set up environment parameters
steps = 50
width = 20
height = 20
prey_count = 15
predator_count = 5
max_starve_time = 8
hunt_prob = 0.6
hunting_range = 1
max_age = 10
reproduce_prob = 0.5
reproduce_age = 3

# Create the environment
env = Environment(width, height, prey_count, predator_count, max_starve_time, hunt_prob, hunting_range, max_age, reproduce_prob, reproduce_age)
history = []
for i in range(steps):
    # print()
    # print('Step:', i, '---------------------')
    history.append(env.get_space())
    env.step()
    env.age_up()
    

# problems: 
# agents do not move in the space properly -> too many predators

