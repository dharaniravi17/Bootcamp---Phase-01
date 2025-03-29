import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = [x for x in data if x < lower_bound or x > upper_bound]
print(f"Interquartile Range (IQR) and Outliers \n")
print(f"Data: {data}")
print(f"Q1: {Q1}, Q3: {Q3}")
print(f"IQR: {IQR}")
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
print(f"Outliers: {outliers if outliers else 'No outliers detected'}")
plt.figure(figsize=(6, 4))
sns.boxplot(data=data, color="skyblue")

plt.title("Box Plot of Given Data")
plt.xlabel("Dataset")
plt.show()
