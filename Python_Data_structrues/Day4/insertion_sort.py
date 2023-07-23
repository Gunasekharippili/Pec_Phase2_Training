def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
    return arr




arr = [2,44,22,4,67,43,44,9,57,24]
print(insertion_sort(arr))