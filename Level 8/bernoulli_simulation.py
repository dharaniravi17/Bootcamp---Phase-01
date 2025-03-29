import numpy as np
trials = np.random.binomial(n=1, p=0.3, size=1000)
simulated_p = np.mean(trials)
print(f"Simulated Probability: {simulated_p:.3f}")
print("Matches theoretical P = 0.3 for Bernoulli trial." if abs(simulated_p - 0.3) < 0.02 else "Deviation from expected value.")
