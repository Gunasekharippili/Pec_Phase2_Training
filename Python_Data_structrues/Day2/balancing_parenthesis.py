stack = []
s = input("enter string")
for i in s:
    if i == "(":
        stack.append(i)
    elif i == ")":
        stack.pop()
        break
else:
    print("Invalid string")
if len(stack) == 0:
    print("valid")
else:
    print("Invalid")
