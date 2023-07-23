arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 0
high = len(arr)-1
key = 10
found = False
while low <= high:
    mid = (low+high)//2
    if key == arr[mid]:
        print("found at:", mid)
        found = True
        break
    elif key < arr[mid]:
        high = mid-1
    elif key > arr[mid]:
        low = mid+1
if not found:
    print("Not found")
