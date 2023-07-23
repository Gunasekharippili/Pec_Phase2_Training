# def binary_search(arr, low, high, key):
#     if low <= high:
#         mid = (low+high)//2
#         if key == arr[mid]:
#             print("found at:", mid)
#         elif key < arr[mid]:
#             high = mid-1
#             return binary_search(arr, low, high, key)
#         elif key > arr[mid]:
#             low = mid+1
#             return binary_search(arr, low, high, key)
#     else:
#         print("Element not found")
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# low = 0
# high = len(arr)-1
# key = int(input())
# binary_search(arr, low, high, key)


def binary_search(arr, x):
    """Finds the index/indices of the element x in the list arr using binary search."""
    left = 0
    right = len(arr) - 1
    indices = []

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            # If we found the element at mid index, add the index to the list of indices
            indices.append(mid)

            # Check if the element is present to the left of mid index
            i = mid - 1
            while i >= left and arr[i] == x:
                indices.append(i)
                i -= 1

            # Check if the element is present to the right of mid index
            i = mid + 1
            while i <= right and arr[i] == x:
                indices.append(i)
                i += 1

            return indices

        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return None

arr = [1,2,2,3,4,4]
x = 4

indices = binary_search(arr, x)
if indices is None:
    print(f"{x} not found in the list.")
else:
    print(f"{x} found at indices: {indices}")
