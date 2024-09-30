def smart_binary_search(arr, target):
    #ascending order
    is_ascending = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_ascending = False
            break

    #descending order
    is_descending = True
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            is_descending = False
            break

    if is_ascending:
        outcome = True
    elif is_descending:
        outcome = False
    #conditions not met
    else:
        return "Invalid Input! Please sort the array first!"
    
    first, last = 0, len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        elif (arr[mid] < target and outcome) or (arr[mid] > target and not outcome):
            first = mid + 1
        else:
            last = mid - 1

    return -1

input_array = [25,22,15,12,9,8,7,5,2,1]
search_key = 71
result = smart_binary_search(input_array, search_key)

print(result)
