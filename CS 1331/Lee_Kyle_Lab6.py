def find_second_largest(numbers):
    largest = -1
    second_largest = -1

    for num in numbers:
        if num >= largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return second_largest



def right_triangle(n):
    # Base case: stop recursion when n becomes 0
    if n > 0:
        print("*" * n)
        # Recursive call with n-1 to decrease the size of the triangle
        right_triangle(n - 1)


def three_sum(numbers, n):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                # Corrected the condition and access to list elements
                if numbers[i] + numbers[j] + numbers[k] == n:
                    return True
    return False

# ------- HELPER CODE: DO NOT MODIFY -------

print(find_second_largest([1,3,5,6,7,8]))  # Expected output: 7

right_triangle(4)  # Expected output: same as docstring

print(three_sum([5,6,7,8,9], 4))  # Expected output: False
print(three_sum([5,6,7,8,9], 21))  # Expected output: True
print(three_sum([5,6,7,8,9], 15))  # Expected output: False