import numpy as np
import matplotlib.pyplot as plt

# Define the mean (mu) and standard deviation (sigma) for the Normal distribution
mu = 0.7  # Mean (centered around 0.5 for the range [0, 1])
sigma = 0.1  # Standard deviation

# Sample size
sample_size = 20

# Generate samples from a Normal distribution
samples = np.random.normal(mu, sigma, sample_size)

# Clamp the values to be between 0 and 1
clamped_samples = np.clip(samples, 0, 1)

# Plot the distribution
plt.hist(clamped_samples, bins=5, density=True, alpha=0.6, color='g')

# Plot the PDF of the Normal distribution (before clamping)
x = np.linspace(0, 1, 1000)
normal_pdf = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
plt.plot(x, normal_pdf, 'r-', lw=2)

plt.title(f"Normal Distribution (clamped) with mu={mu} and sigma={sigma}")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
