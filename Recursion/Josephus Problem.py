def jos(n,k):
    if n==1:
        return 0
    else:
        return (jos(n-1,k)+k)%n
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        return jos(a,b)+1
    
obj=Solution()
print(obj.solve(10,4))
