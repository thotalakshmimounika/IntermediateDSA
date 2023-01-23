#You have given a string A having Uppercase English letters.You have to find how many times subsequence "AG" is there in the given string.NOTE Return the answer modulo 109 + 7 as the answer can be very large.
a = "ABCGAG"
n=len(a)
print(n)
acount=0
ans=0
for i in range(n):
    if a[i]=='A':
        acount+=1
    if a[i]=='G':
        ans=ans+acount
print(ans)