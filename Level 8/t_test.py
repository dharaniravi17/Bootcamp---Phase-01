import numpy as np
import scipy.stats as stats
pop_mean = 100  
sample_size = 30
sample_std = 20  
alpha = 0.05  
np.random.seed(42) 
sample_data = np.random.normal(140, 20, sample_size)
t_score, p_value = stats.ttest_1samp(sample_data, pop_mean)
decision = "Reject H₀: Medication increases IQ" if p_value < alpha else "Fail to Reject H₀"

print(f"T-score: {t_score:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Decision: {decision}")
