import numpy as np
import scipy.stats as stats
height = np.array([160, 170, 180, 175])
weight = np.array([60, 70, 75, 65])
pearson_corr, _ = stats.pearsonr(height, weight)
spearman_corr, _ = stats.spearmanr(height, weight)
print(f"Pearson Correlation: {pearson_corr:.2f}")
print(f"Spearman Correlation: {spearman_corr:.2f}")

if pearson_corr > spearman_corr:
    print("Pearson is higher due to a more linear relationship.")
else:
    print("Spearman is higher, indicating a stronger rank-based correlation.")
