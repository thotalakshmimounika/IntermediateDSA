a=[16,3,3,6,7,8,17,13,7]

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        ans=1
        c=1
        for i in range(1,len(a)):
            if a[i]>a[i-1]:
                c+=1
            else:
                c=1
            ans=max(ans,c)
        return ans