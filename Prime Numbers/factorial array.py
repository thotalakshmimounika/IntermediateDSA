a=[ 251, 923, 561, 230, 100, 399, 542, 198, 548, 892, 721, 781, 174, 809, 9, 232, 165, 861, 36, 837, 377, 313, 475, 269, 210, 530, 940, 570, 24, 434, 764, 275, 709, 325, 505, 161, 724, 47, 359, 625, 291, 81, 406, 465, 242, 767, 698, 408, 629, 86, 597, 358, 399, 72, 979, 962, 603, 919, 884, 627, 353, 1, 254, 414, 678, 111, 575, 755, 511, 287, 380, 802, 720, 138, 620, 314, 905, 670, 74, 886, 756, 671, 244, 508, 744, 224, 822, 347, 495, 706, 326, 201, 707, 580, 615, 386, 43, 543, 141, 554 ]
a.sort() 
print(a)
l=max(a)
p=[True]*(l+1)
p[0],p[1]=False,False
print(p,l)

for i in range(2,int(l**0.5)+1):
    if p[i]:
        for j in range(i*i,l+1,i):
            p[j]=False
print(p)
primes_before = [0] * (l + 1)

for i in range(2, l + 1):
    if p[i]:
        primes_before[i] = primes_before[i - 1] + 1
    else:
        primes_before[i] = primes_before[i - 1]
print(primes_before)


d={}
for i in a:
    if primes_before[i] in d:
        d[primes_before[i]]+=1
    else:
        d[primes_before[i]]=1
print(d)
ans=0
mod=10**9+7
for k, v in d.items():
    ans += (pow(2, v, mod)-1) % mod # contribution technique to find subsequences
    ans = ans % mod
print(ans)