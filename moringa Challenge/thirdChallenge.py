def solution(N):
    if N % 2 != 0:
        N -= 1

    half_N = N // 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create a string with all letters in alphabetical order
    all_letters = ''.join(alphabet)

    # Repeat the string to get the desired length
    result = all_letters * (half_N // 26)

    # Add any remaining letters to the result
    result += all_letters[:half_N % 26]

    return result

# Test examples
print(f'Test 1: {solution(3)}')
print(f'Test 2: {solution(5)}')
print(f'Test 3: {solution(30)}')
