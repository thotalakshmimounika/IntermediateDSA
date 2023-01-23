#You are given a string S, and you have to find all the amazing substrings of S.An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
a='ABECD'
n=len(a)
ans=0
for i in range(n):
    if a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U' or a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        ans=ans+n-i
print(ans%10003)

