#Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.class Solution:
    # @param A : list of integers
    # @return an integer
def solve(self, a):
        n=len(a)
        mi=a[0]
        ma=a[1]
        if n==1 or n==2:
            return n
        else:
            if a[0]>a[1]:
                ma=a[0]
                mi=a[1]
            for i in range(2,n):
                if a[i]>ma:
                    ma=a[i]
                elif a[i]<mi:
                    mi=a[i]
        if mi==ma:
            return 1
        ans =n
        imi=-1
        ima=-1
        for i in range(n):
            if a[i]==mi:
                imi=i
                if ima!=-1:
                    ans=min(ans,i-ima+1)
            elif a[i]==ma:
                ima=i
                if imi!=-1:
                    ans=min(ans,i-imi+1)
        return ans