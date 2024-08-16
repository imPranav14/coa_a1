import numpy as np
import time

def matrix_multiply_integer(N):
    A = np.ones((N, N), dtype=int)
    B = np.ones((N, N), dtype=int)
    C = np.zeros((N, N), dtype=int)

    start_time = time.time()

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]

    end_time = time.time()
    print(f"Time taken for Integer matrix multiplication of size {N}x{N}: {end_time - start_time:.6f} seconds")

def matrix_multiply_double(N):
    A = np.ones((N, N), dtype=float)
    B = np.ones((N, N), dtype=float)
    C = np.zeros((N, N), dtype=float)

    start_time = time.time()

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]

    end_time = time.time()
    print(f"Time taken for Double matrix multiplication of size {N}x{N}: {end_time - start_time:.6f} seconds")


sizes = [64,128,256,512,1024]
for N in sizes:
    matrix_multiply_double(N)


