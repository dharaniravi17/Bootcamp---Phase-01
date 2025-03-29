import numpy as np
import statsmodels.stats.weightstats as st
pop_mean = 100  
pop_std = 15   
sample_size = 30
alpha = 0.05    
np.random.seed(42) 
sample_data = np.random.normal(140, 15, sample_size)
z_score, p_value = st.ztest(sample_data, value=pop_mean, alternative='larger')
decision = "Reject H₀: Medication affects IQ" if p_value < alpha else "Fail to Reject H₀"

print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Decision: {decision}")
