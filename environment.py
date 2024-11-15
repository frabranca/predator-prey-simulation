from agents import Predator, Prey
import numpy as np
import random
from probabilities import *

class Environment:
    def __init__(self, config):
        # Read configuration
        self.config = config
        self.width = self.config['simulation']['width']
        self.height = self.config['simulation']['height']

        # Preys:
        # Parameters
        self.preys_count = self.config['preys']['count']
        self.preys_breed_age = self.config['preys']['breed_age']
        self.preys_max_age = self.config['preys']['max_age']

        # Probabilities:
        mean = self.config['preys']['breed_prob_mean']
        std = self.config['preys']['breed_prob_std']
        self.preys_breed_prob = generate_distribution(self.config['preys']['breed_prob_mean'], 
                                                      self.config['preys']['breed_prob_std'],
                                                      self.preys_count)

        # Predators:
        # Parameters
        self.preds_count = self.config['predators']['count']
        self.preds_breed_age = self.config['predators']['breed_age']
        self.preds_hunting_range = self.config['predators']['hunting_range']
        self.preds_max_starve_time = self.config['predators']['max_starve_time']
        self.preds_max_age = self.config['predators']['max_age']

        # Probabilities:
        self.preds_breed_prob = generate_distribution(self.config['predators']['breed_prob_mean'], 
                                                      self.config['predators']['breed_prob_std'], 
                                                      self.preds_count)

        self.preds_hunt_prob = generate_distribution(self.config['predators']['hunt_prob_mean'], 
                                                     self.config['predators']['hunt_prob_std'], 
                                                     self.preds_count)
        
        # Genearate space
        self.space = [[None for _ in range(self.width)] for _ in range(self.height)]

        # Randomly populate the environment with preys and predators
        self.populate()
    
    def populate(self):
        # Place preys randomly
        if self.preys_count > 0:
            for i in range(self.preys_count):
                x, y = self.random_empty_cell()
                self.space[x][y] = Prey(x, y, self.space, self.preys_max_age, self.preys_breed_prob[i], self.preys_breed_age)
        
        # Place predators randomly
        if self.preds_count > 0:
            for i in range(self.preds_count):
                x, y = self.random_empty_cell()
                self.space[x][y] = Predator(x, y, self.space, self.preds_max_age, self.preds_breed_prob[i], self.preds_breed_age, 
                                            self.preds_max_starve_time, self.preds_hunt_prob[i], 
                                            self.preds_hunting_range)
            
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
        # Perform one simulation step: move, hunt, breed
        for row in self.space:
            for cell in row:
                if isinstance(cell, Prey):
                    if cell.is_alive:
                        self.space[cell.x][cell.y] = None
                        cell.move()    # Prey moves
                        self.space[cell.x][cell.y] = cell
                        cell.breed()  # Prey breeds if possible
                    else:
                        self.space[cell.x][cell.y] = None

                elif isinstance(cell, Predator):
                    if cell.is_alive:
                        self.space[cell.x][cell.y] = None
                        cell.move()    # Predator moves
                        self.space[cell.x][cell.y] = cell
                        cell.breed()  # Predator breeds if possible
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