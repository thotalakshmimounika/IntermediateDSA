a = [1, 2, 3]
n=len(a)
allsum=0
#for i in range(n):
  #  s=0
 #   for j in range(i,n):
 #       s+=a[j]
#       allsum+=s 
# print(allsum)

n=len(a)
allsum=0
# check how many times the ith element is repeating in an subaaray and sum them
for i in range(n):
    allsum+=a[i]*(i+1)*(n-i)
print(allsum)
