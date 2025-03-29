from scipy.stats import norm
mean = 4
std_dev = 1
x_value = 4.25
z_score = (x_value - mean) / std_dev
percentage_above = norm.sf(z_score) * 100 
print(f"Gaussian Distribution Area \n")
print(f"Mean: {mean}, Standard Deviation: {std_dev}")
print(f"Z-score for x = {x_value}: {z_score:.2f}")
print(f"Percentage of scores above {x_value}: {percentage_above:.2f}%")
