import numpy as np
import copy

def check_consistency(A, B):
    AB = copy.deepcopy(A)  # Create a deep copy of A to avoid modifying the original matrix
    for i in range(len(A)):
        AB[i].append(B[i][0])  # Create augmented matrix [A | B]

    rank_A = np.linalg.matrix_rank(A)  # Rank of coefficient matrix
    rank_AB = np.linalg.matrix_rank(AB)  # Rank of augmented matrix
    num_var = len(A[0])  # Number of variables (columns in A)

    print(f"Rank(A) = {rank_A}, Rank([A | B]) = {rank_AB}, Variables = {num_var}")

    if rank_A == rank_AB:
        if rank_A == num_var:
            return "System is consistent with a unique solution."
        else:
            return "System is consistent with infinitely many solutions."
    else:
        return "System is inconsistent (no solution)."
    
matrixA = [[1,2,3],[4,5,6],[7,8,9]]
matrixB = [[10],[41],[12]]
result = check_consistency(matrixA, matrixB)
print(result)

