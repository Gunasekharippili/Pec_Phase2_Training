def bubble_sort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if swap == False:
            break
    return arr

arr = [2,44,22,4,67,43,44,9,57,24]
print(bubble_sort(arr))

def bubble_sort_1(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-1-i):
            if arr[j][1] > arr[j+1][1]:
                swap = True
                arr[j][1], arr[j+1][1] = arr[j+1][1], arr[j][1]

        if swap == False:
            break
    return arr
arr1 = [[1,2],[3,4],[5,6],[7,8]]
print(bubble_sort_1(arr1))