import pandas as pd
import numpy as np
import scipy.stats as stats

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('laptop_prices.csv')  

# Step 2: Select the column 'Ram'
ram_column = df['Ram']

# Step 3: Define the sample size and the confidence level
sample_size = 30
confidence_level = 0.95

# Step 4: Take a random sample of size 30
sample = ram_column.sample(n=sample_size, replace=True)

# Step 5: Calculate the sample mean and standard deviation
sample_mean = sample.mean()
sample_std = sample.std(ddof=1)  # Sample standard deviation (ddof=1 for unbiased estimate)

# Step 6: Calculate the standard error of the mean (SEM)
standard_error = sample_std / np.sqrt(sample_size)

# Step 7: Calculate the critical value (Z or t-score depending on sample size)
# For a small sample size, we use the t-distribution
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1)

# Step 8: Calculate the margin of error
margin_of_error = critical_value * standard_error

# Step 9: Calculate the confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Step 10: Print the results
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Confidence Interval (95%): ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
