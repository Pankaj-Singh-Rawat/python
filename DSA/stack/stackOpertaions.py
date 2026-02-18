stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

stack.pop()
print(stack)

print(stack[-1])

isEmpty = not bool(stack)
print(isEmpty)

print(len(stack))