# arr = [i for i in range(1, 11)]
# k = 8
# for i in range(len(arr)):
#     if k == arr[i]:
#         print(arr)
#         print("found at", i)
#         break
# else:
#     print("Not found")
def linear_search(lst, x):
    indices = []
    for i in range(len(lst)):
        if lst[i] == x:
            indices.append(i)
    return indices

# Example usage
my_list = [4, 5, 6, 7, 8, 9, 6, 7, 6, 10]
element = 6
indices = linear_search(my_list, element)

print(indices)