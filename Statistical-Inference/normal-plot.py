import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('laptop_prices.csv')  

# Step 2: Select the column 'Ram'
ram_column = df['Weight']

# Step 3: Define the sample size
sample_size = 100
num_samples = 1000  # Number of times we sample

# Step 4: Calculate sample means
sample_means = [ram_column.sample(n=sample_size, replace=True).mean() for _ in range(num_samples)]

# Step 5: Calculate the mean and standard deviation of the sample means
mean_of_sample_means = np.mean(sample_means)
std_dev_of_sample_means = np.std(sample_means)

# Step 6: Print the results
# print(f"Mean of all sample means: {mean_of_sample_means}")
# print(f"Standard deviation of all sample means: {std_dev_of_sample_means}")

# Step 7: Plot a normal distribution based on the sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='g', label='Sample Means')

# Plotting the normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-0.5 * ((x - mean_of_sample_means) / std_dev_of_sample_means)**2) / (std_dev_of_sample_means * np.sqrt(2 * np.pi))

plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution')
title = "Normal Distribution of Sample Means (n=30)"
plt.title(title)
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.legend()

# Step 8: Show the plot
plt.show()
