#Given an array A of N integers. Also given are two integers B and C. Reverse the array A in the given range [B, C]
a= [1, 2, 3, 4]
b= 2
c= 3
if b==0:
    print((a[b:c+1][::-1])+a[c+1:])
else:
    print((a[:b])+(a[b:c + 1][::-1]) + a[c + 1:])