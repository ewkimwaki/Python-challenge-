def solution(N):
    if N % 2 != 0:
        N -= 1

    half_N = N // 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    result = ''.join([alphabet[i % 26] for i in range(half_N)])

    result += result

    return result

# Test examples
print(f'Test 1: {solution(3)}') 
print(f'Test 2: {solution(5)}')
print(f'Test 3: {solution(30)}')
