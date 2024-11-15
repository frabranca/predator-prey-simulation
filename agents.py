import random

class Prey:
    def __init__(self, x, y, space, reproduce_prob, reproduce_age=5):
        self.x = x
        self.y = y
        self.space = space
        self.age = 0
        self.reproduce_prob = reproduce_prob
        self.reproduce_age = reproduce_age
        self.is_alive = True
    
    def age_up(self):
        self.age += 1

    def check_neighbors(self):
        # Check if which neighboring cells are empty and return them in a list
        neighbors = []
        
        # Check nearby cells (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = self.x + dx, self.y + dy
            
            # Check if the new position is within space bounds and free
            if 0 <= nx < len(self.space) and 0 <= ny < len(self.space[0]):
                if self.space[nx][ny] is None:  # Empty cell
                    neighbors.append((nx, ny))
        
        return neighbors
    
    def move(self):
        neighbors = self.check_neighbors()
        # If there are available neighboring cells, move randomly to one
        if neighbors:
            self.x, self.y = random.choice(neighbors)
    
    def reproduce(self):
        if self.age >= self.reproduce_age:
            if random.random() < self.reproduce_prob:
                neighbors = self.check_neighbors()
                if neighbors:
                    x_free, y_free = random.choice(neighbors)
                    self.space[x_free][y_free] = Prey(x_free, y_free, self.space, self.reproduce_prob, self.reproduce_age)
    
class Predator:
    def __init__(self, x, y, space, max_starve_time, hunt_prob, hunting_range, max_age, reproduce_prob, reproduce_age=5):
        self.x = x
        self.y = y
        self.space = space
        self.age = 0
        self.hunger = 0
        self.max_starve_time = max_starve_time
        self.hunt_prob = hunt_prob
        self.hunting_range = hunting_range
        self.max_age = max_age
        self.reproduce_prob = reproduce_prob
        self.reproduce_age = reproduce_age
        self.is_alive = True
    
    def age_up(self):
        self.age += 1
        # Predator dies if it exceeds max age
        if self.age >= self.max_age:
            self.is_alive = False
        
        # Predator dies of it cannot find food
        if self.hunger >= self.max_starve_time:
            self.is_alive = False
    
    def check_neighbors(self):
        empty_cells = []
        nearby_preys = []

        # Define the range of cells to check based on the hunting range
        for dx in range(-self.hunting_range, self.hunting_range + 1):
            for dy in range(-self.hunting_range, self.hunting_range + 1):
                # Skip the predator's current position
                if dx == 0 and dy == 0:
                    continue
                
                nx, ny = self.x + dx, self.y + dy
                
                # Check if the cell is within bounds
                if 0 <= nx < len(self.space) and 0 <= ny < len(self.space[0]):
                    # If it's empty, add to empty_cells
                    if self.space[nx][ny] is None:
                        empty_cells.append((nx, ny)) # append empty cells coordinates

                    # If it's a prey, add to nearby_preys
                    elif isinstance(self.space[nx][ny], Prey):
                        nearby_preys.append(self.space[nx][ny]) # append prey objects

        # Return prey cells if hunting, otherwise empty cells
        return empty_cells, nearby_preys

    def move(self):
        # Get a list of available cells (empty or prey)
        empty_cells, nearby_preys = self.check_neighbors()

        # If there are available cells, move randomly to one
        if random.random() < self.hunt_prob and nearby_preys:
            # predator decides to move and hunt
            hunted_prey = random.choice(nearby_preys)
            hunted_prey.is_alive = False
            # location remains the same as the predator is hunting
        else:
            # predator decides to move to empty cell
            if empty_cells:
                x_free, y_free = random.choice(empty_cells)
                self.x = x_free
                self.y = y_free

            # hunger increases
            self.hunger += 1

    def reproduce(self):
        if self.age >= self.reproduce_age:
            if random.random() < self.reproduce_prob:
                # New borns do not hunt straight out of the womb so they just go to empty cells
                empty_cells, nearby_preys = self.check_neighbors()
                if empty_cells:
                    x_free, y_free = random.choice(empty_cells)
                    self.space[x_free][y_free] = Predator(x_free, y_free, self.space, self.max_starve_time, 
                                                                self.hunt_prob, self.hunting_range, self.max_age,
                                                                self.reproduce_prob, self.reproduce_age)
