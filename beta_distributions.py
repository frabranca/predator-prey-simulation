import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Define the alpha and beta parameters (shape parameters)
alpha = 2  # Shape parameter alpha
beta_param = 3  # Shape parameter beta

# Sample size
sample_size = 40

# Generate samples from the Beta distribution
samples = beta.rvs(alpha, beta_param, size=sample_size)
print(samples)
# Plot the distribution
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

# Plot the Beta distribution's probability density function
x = np.linspace(0, 1, 1000)
plt.plot(x, beta.pdf(x, alpha, beta_param), 'r-', lw=2)

plt.title(f"Beta Distribution with alpha={alpha} and beta={beta_param}")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()