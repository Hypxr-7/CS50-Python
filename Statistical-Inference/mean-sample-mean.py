import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('laptop_prices.csv') 

# Step 2: Select the column 'Ram'
ram_column = df['Ram']

# Step 3: Calculate the sample means for sample size of 3
sample_size = 30
sample_means = [ram_column.sample(n=sample_size).mean() for _ in range(len(ram_column) // sample_size)]

population_mean = ram_column.mean()

# Step 4: Calculate the mean of all sample means
mean_of_sample_means = sum(sample_means) / len(sample_means)

print(f"The mean of all sample means for sample size {sample_size} is: {mean_of_sample_means}")
print(f"Population Mean: {population_mean}")
