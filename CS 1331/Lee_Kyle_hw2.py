import time

# Function to calculate the number of paths from the top-left to the bottom-right of a grid
def num_paths(m, n):
    # Base case: If either dimension is 1, there is only one path
    if m == 1 or n == 1:
        return 1
    # Recursive case: Sum of paths from the top and left cells
    return num_paths(m - 1, n) + num_paths(m, n - 1)

# Function with memoization to store and reuse previously calculated values
def num_paths_memo(m, n, memo={}):
    # Base case: If either dimension is 1, there is only one path
    if m == 1 or n == 1:
        return 1
    # Check if the result for the current dimensions is already memoized
    if (m, n) in memo:
        return memo[(m, n)]
    # Recursive case: Sum of paths from the top and left cells with memoization
    paths = num_paths_memo(m - 1, n, memo) + num_paths_memo(m, n - 1, memo)
    # Memoize the result for the current dimensions
    memo[(m, n)] = paths
    return paths

# Driver code - you do not need to make any changes after this line.
# However, submit a screenshot of the output to report the execution time/elapsed time.

# Calculate and prints the number of paths without memoization
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

# Calculate and prints the number of paths with memoization
start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

# Prints the elapsed time for both cases
print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")
