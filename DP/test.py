s="y#fo##f"
t="y#f#o##f"
stack1 =[]
for i in s:
    if i =="#":
        if stack1:
            stack1.pop()
    else:
        stack1.append(i)
stack2 =[]
for i in t:
    if i == "#":
        if stack2:
            stack2.pop()
    else:
        stack2.append(i)
print((''.join(stack1))==(''.join(stack2)))
