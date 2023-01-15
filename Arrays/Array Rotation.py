#Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.

a= [ 1, 1, 4, 9, 4, 7, 1 ]
b= 9

a=a[::-1]
print(a)
print(a[:b][::-1]+(a[b:][::-1]))