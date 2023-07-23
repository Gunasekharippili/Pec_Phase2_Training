
A = [
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]

a = len(A)
b = len(A[0])
stack = []
for i in range(a):
    for j in range(b):
        if A[i][j] == 1:
            stack.append(A[i][j])
        else:
            stack.pop()
print(stack)
