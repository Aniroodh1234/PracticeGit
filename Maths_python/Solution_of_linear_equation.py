import math

def gauss_seidel(A, b, initial_guess, tolerance, max_iterations):
    n = len(A)  # Number of equations
    x = initial_guess.copy()  # Initialize the solution vector

    for iteration in range(max_iterations):
        x_new = x.copy()  # Store updated values for this iteration
        print(f"Iteration {iteration + 1}:")
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))  # Use updated values for j < i
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))  # Use old values for j > i
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]  # Update the current variable
            
            print(f"x[{i}] = {x_new[i]:.6f}")
        
        # Calculate the error using Euclidean norm
        error = math.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n)))
        print(f"Error: {error:.6f}\n")
        
        # Check if the solution has converged
        if error < tolerance:
            print("Converged!")
            return x_new
        
        x = x_new  # Update for the next iteration

    print("Maximum iterations reached without convergence.")
    return x_new

# Function to get user input
def get_user_input():
    print("Enter the coefficient matrix A (row by row):")
    rows = int(input("Number of equations: "))
    A = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        A.append(row)

    print("Enter the constant terms vector b:")
    b = list(map(float, input().split()))

    print("Enter the initial guess for the solution (separated by spaces):")
    initial_guess = list(map(float, input().split()))

    print("Enter the tolerance for convergence (e.g., 0.0001):")
    tolerance = float(input())

    print("Enter the maximum number of iterations:")
    max_iterations = int(input())

    return A, b, initial_guess, tolerance, max_iterations

# Main Execution
A, b, initial_guess, tolerance, max_iterations = get_user_input()
solution = gauss_seidel(A, b, initial_guess, tolerance, max_iterations)
print("\nSolution:", solution)
