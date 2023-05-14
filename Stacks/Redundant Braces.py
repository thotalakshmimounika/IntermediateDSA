a= "a+b"
stack=[]
tos=-1
for i in range(len(a)):
    if a[i]=='(' or a[i]=='+' or a[i]=='-' or a[i]=='/' or a[i]=='*':
        stack.append(a[i])
        tos+=1
    elif a[i].islower():
        continue
    else:
        if stack[tos]=='(':
            print(1)
        while(stack[tos]!='('):
            stack.pop()
            tos-=1 
        stack.pop()
        tos-=1
print(0)


