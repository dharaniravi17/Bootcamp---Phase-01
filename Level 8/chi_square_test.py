import scipy.stats as stats
observed = [121, 288, 91]  
expected = [100, 150, 250]  
chi2_stat, p_value = stats.chisquare(observed, expected)
decision = "Reject H₀: Age distribution has changed" if p_value < 0.05 else "Fail to Reject H₀"
print(f"Chi-Square Statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.4f}")
print(f"Decision: {decision}")
