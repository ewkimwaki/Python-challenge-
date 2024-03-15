def digit_sum(num):
    return sum(int(digit) for digit in str(abs(num)))  # Always use the absolute value

def solution(A):
    digit_sums = {}
    max_sum = -1

    for num in A:
        current_sum = digit_sum(num)

        if current_sum in digit_sums:
            pair_sum = digit_sums[current_sum] + num
            max_sum = max(max_sum, pair_sum)
        else:
            digit_sums[current_sum] = max(digit_sums.get(current_sum, float('-inf')), num)

    return max_sum

# Test examples
print(f'Test 1: {solution([51, 71, 17, 42])}')
print(f'Test 2: {solution([42, 33, 60])}')
print(f'Test 3: {solution([51, 32, 43])}')
