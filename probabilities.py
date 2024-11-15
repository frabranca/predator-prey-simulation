from scipy.stats import beta
import numpy as np

def generate_distribution(mean, std, sample_size):
    samples = np.random.normal(mean, std, sample_size)
    # Clamp the values to be between 0 and 1
    clamped_samples = np.clip(samples, 0, 1)
    return clamped_samples

if __name__=='__main__':
    print(generate_distribution(0.7, 0.1, 20))
