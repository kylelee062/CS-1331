def get_mode(num_list):
    counter = 0
    num = num_list[0]

    for i in num_list:
        occuring = num_list.count(i)
        if occuring > counter:
            counter = occuring
            num = i

    return num

def get_longest_run_length(num):
    count = 1
    max_count = 1

    for i in range(1, len(num)):
        if num[i] == num[i-1]:
            count += 1
        else:
            count = 1

        max_count = max(max_count, count)

    return max_count

my_list = [1,2,3,4,4,2,2,2]
mode = get_mode(my_list)
longest = get_longest_run_length(my_list)
print(mode)
print(longest)