import numpy as np
num_rolls = 1000
rolls = np.random.randint(1, 7, num_rolls)
count_1_or_3 = np.sum((rolls == 1) | (rolls == 3))
P_simulated = count_1_or_3 / num_rolls
P_theoretical = (1/6) + (1/6)
print(f"### Probability Simulation: Rolling a Die 1000 Times ###\n")
print(f"Total Rolls: {num_rolls}")
print(f"Times 1 or 3 appeared: {count_1_or_3}")
print(f"Simulated Probability P(1 or 3): {P_simulated:.4f}")
print(f"Theoretical Probability P(1 or 3): {P_theoretical:.4f}")
print("\nTheoretical probability is 1/3 (0.3333), close to the simulation.")
