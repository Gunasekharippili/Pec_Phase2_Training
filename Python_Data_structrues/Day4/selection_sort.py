def selection(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

def selection_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i, len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def selection_abc(arr):
    pass

arr = [2,44,22,4,67,43,44,9,57,24]
print(arr)
print(selection_sort(arr))
selection(arr)
print(arr)