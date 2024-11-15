import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from environment import Environment
from datetime import datetime
import yaml

# Load the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Running the simulation
# Set up environment parameters
steps = config['simulation']['steps']

# Create the environment
env = Environment(config)
history = []
for i in range(steps):
    # print()
    # print('Step:', i, '---------------------')
    history.append(env.get_space())
    env.step()
    env.age_up()

# Get the current date
current_date = datetime.now().strftime("%m-%d-%H-%M-%S")

# Initialize the plot
fig, ax = plt.subplots()
im = ax.imshow(history[0], cmap='viridis', interpolation='none', vmin=0, vmax=2, aspect='equal')

# Set up gridlines
ax.set_xticks(np.arange(-0.5, history[0].shape[1], 1), minor=True)  # Tick at every cell edge
ax.set_yticks(np.arange(-0.5, history[0].shape[0], 1), minor=True)  # Tick at every cell edge
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)
ax.tick_params(which='minor', bottom=False, left=False)

# Title
title = ax.set_title("Step 0")  # Initialize the title

# Update function
total_preys_count = []
total_predators_count = []

def update(frame_index):
    # update number of preys and predators
    preys_alive = np.sum(history[frame_index] == 1)
    predators_alive = np.sum(history[frame_index] == 2)
    total_preys_count.append(preys_alive)
    total_predators_count.append(predators_alive)

    # update frame
    im.set_array(history[frame_index])  # Update the image
    title.set_text(f"Step {frame_index}")  # Update the title with frame number
    print('N. preys=', preys_alive, 'N. predators=', predators_alive)
    return [im]

# Create the animation
ani = FuncAnimation(fig, update, frames=len(history), interval=200, blit=False, repeat=False)

output_filename = f"videos_and_graphs/experiment_{current_date}.mp4"
ani.save(output_filename, writer="ffmpeg", fps=10)

plt.figure()
plt.plot(total_preys_count, label='Preys', color='black')
plt.plot(total_predators_count, label='Predators', color='red')
plt.legend()
plt.grid()
plt.savefig(output_filename[:-4] + '.png')
