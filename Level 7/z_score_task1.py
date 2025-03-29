import numpy as np
data = np.array([2, 3, 4, 5, 6, 7])
mean = np.mean(data)
std_dev = np.std(data, ddof=0)
z_scores = (data - mean) / std_dev
print(" Z-Score Calculation \n")
print(f"Dataset: {data}")
print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}\n")
print("Z-Scores:")
for i, (val, z) in enumerate(zip(data, z_scores)):
    print(f"x = {val}, Z-score = {z:.2f}")
z_5 = (5 - mean) / std_dev
print(f"\n### Interpretation ###")
print(f"The Z-score for x = 5 is {z_5:.2f}, meaning it’s {z_5:.2f} standard deviations above the mean.")
