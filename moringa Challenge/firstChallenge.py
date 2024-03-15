def solution(A):
    n = len(A)  # Calculates the number of items in the array
    total_bricks = sum(A)  # Adds values of the items

    # Checks if it will be possible to perform our function of distributing equally
    if total_bricks % n != 0:
        return -1

    overflow_bricks = total_bricks // n
    moves = 0
    for i in range(n - 1):  # Iterate up to n - 1
        to_be_removed = A[i] - overflow_bricks

        A[i] -= to_be_removed
        A[i + 1] += to_be_removed
        moves += abs(to_be_removed)  # Use absolute value to calculate moves

    return moves

# Test examples
print(f'Test 1: {solution([7, 15, 10, 8])}')
print(f'Test 2: {solution([11, 10, 8, 12, 8, 10, 11])}')
print(f'Test 3: {solution([7, 14, 10])}')

