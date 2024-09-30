file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == target:
            print(f"Target = {target}, Found at index = {mid}, Number of iterations = {iterations}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Target = {target}, Not found, Number of iterations = {iterations}")
    return -1

target = input('Enter search key: ').lower()
while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()