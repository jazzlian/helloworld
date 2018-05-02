import numpy as np

coefficients = np.array([ [4,5], [1,2] ])
dependents = np.array([20, 13])

answers = np.linalg.solve(coefficients, dependents)

print(answers)