import statistics
import math
data = [2, 4, 6, 8, 10]
mean_value = sum(data) / len(data)
variance_value = sum((x - mean_value) ** 2 for x in data) / len(data)
std_dev_value = math.sqrt(variance_value)
print(" Measures of Dispersion \n")
print(f"Dataset: {data}")
print(f"Mean: {mean_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value:.3f}")
print("\n Interpretation ")
print("Variance measures how spread out the values are.")
print("Standard deviation shows the average deviation from the mean.")
