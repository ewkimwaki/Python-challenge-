def solution(A):
    n = len(A) #calaculates the number of items in the array
    total_bricks = sum(A) #adds values of the items
    
    #checks if it will be possible to perform our function of distributing equally
    if total_bricks % n != 0: 
        return -1
    
    overflow_bricks = total_bricks // n
    moves = 0
    for i in range(n):
        to_be_removed = A[i] - overflow_bricks

        if to_be_removed > 0:
            A[i] -= to_be_removed
            A[i + 1] += to_be_removed
            moves += to_be_removed
        elif to_be_removed < 0:
            A[i] -= to_be_removed
            A[i + 1] += to_be_removed
            moves -= to_be_removed

    return moves

# Test examples
print(f'Test 1: {solution([7, 15, 10, 8])}') 
print(f'Test 2: {solution([11, 10, 8, 12, 8, 10, 11])}') 
print(f'Test 3: {solution([7, 14, 10])}')
