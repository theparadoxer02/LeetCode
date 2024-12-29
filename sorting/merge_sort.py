def merge_sort(llist):
    N = len(llist)
    if N <= 1:
        return llist

    mid = len(llist) // 2

    left_list = llist[:mid]
    right_list = llist[mid:]

    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)

    return merge(sorted_left_list, sorted_right_list)


def merge(list1, list2):
    final_list = []

    M = len(list1)
    N = len(list2)
    i = j = 0

    while i < M and j < N:
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else:
            final_list.append(list2[j])
            j += 1

    final_list.extend(list1[i:])
    final_list.extend(list2[j:])

    return final_list


input_list = [1, 10, 9, 5, 6, 5, 9]
result = merge_sort(input_list)
print(result)
