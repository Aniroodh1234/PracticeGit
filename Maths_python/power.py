import numpy as np

def rayleigh_power_method(A, x0, tol=1e-6, max_iter=1000):
    x = x0 / np.linalg.norm(x0)  # Normalize the initial vector
    lambda_old = 0  # Initial eigenvalue guess

    for _ in range(max_iter):
        Ax = np.dot(A, x)
        lambda_new = np.dot(x.T, Ax) / np.dot(x.T, x)  # Rayleigh quotient

        x_new = Ax / np.linalg.norm(Ax)  # Normalize the new vector

        if np.abs(lambda_new - lambda_old) < tol:
            break  # Stop if the eigenvalue has converged

        x = x_new
        lambda_old = lambda_new

    return lambda_new, x  # Return the eigenvalue and eigenvector
# Define a square matrix
A = np.array([[2, 1],
            [3, 3]])
x0 = np.array([1, 1])
eigenvalue, eigenvector = rayleigh_power_method(A, x0)
print("Dominant Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)