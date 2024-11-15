import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation import history as frames

# Initialize the plot
fig, ax = plt.subplots()
im = ax.imshow(frames[0], cmap='viridis', interpolation='none', vmin=0, vmax=2, aspect='equal')

# Set up gridlines
ax.set_xticks(np.arange(-0.5, frames[0].shape[1], 1), minor=True)  # Tick at every cell edge
ax.set_yticks(np.arange(-0.5, frames[0].shape[0], 1), minor=True)  # Tick at every cell edge
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)
ax.tick_params(which='minor', bottom=False, left=False)

# Title
title = ax.set_title("Frame 0")  # Initialize the title

# Update function
total_preys_count = []
total_predators_count = []

def update(frame_index):
    # update number of preys and predators
    preys_alive = np.sum(frames[frame_index] == 1)
    predators_alive = np.sum(frames[frame_index] == 2)
    total_preys_count.append(preys_alive)
    total_predators_count.append(predators_alive)

    # update frame
    im.set_array(frames[frame_index])  # Update the image
    title.set_text(f"Step {frame_index}")  # Update the title with frame number
    print('N. preys=', preys_alive, 'N. predators=', predators_alive)
    return [im]

# Create the animation
ani = FuncAnimation(fig, update, frames=len(frames), interval=200, blit=False, repeat=False)

# Show the animation
plt.show()

plt.figure()
plt.plot(total_preys_count, label='Preys')
plt.plot(total_predators_count, label='Predators')
plt.legend()
plt.grid()
plt.show()
