# Given two string A and B of length N and M respectively consisting of lowercase letters. Find the number of occurrences of B in A.


# Problem Constraints
# 1 <= M <= N <= 105



# Input Format
# Two argument A and B are strings


# Output Format
# Return an integer denoting the number of occurrences of B in A


# Example Input
# Input 1:
# A = "acbac"
# B = "ac"
# Input 2:
# A = "aaaa"
# B = "aa"


# Example Output
# Output 1:
# 2
# Output 2:
# 3


# Example Explanation
# For Input 1:
# The string "ac" occurs twice in "acbac".
# For Input 2:
# The string "aa" occurs thrice in "aaaa".

def Power(x,y,m):# for calculation of power
    if y==0:
        return 1    
    z= Power(x,y>>1,m)        

    if y&1:    
        return (x*z*z)%m
    else:
        return (z*z)%m

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        m=len(b)
        mod=10**9+7
        c=0
        hb,ha=0,0
        x=29
        for i in range(m):
            hb=(hb+ord(b[i])*Power(x,i,mod))%mod
            ha=(ha+ord(a[i])*Power(x,i,mod))%mod
        if hb==ha:
            c+=1

        s=0
        e=m
        while(e<n):
            ha=(ha-ord(a[s])*Power(x,s,mod))%mod
            ha=(ha+ord(a[e])*Power(x,e,mod))%mod
            hb=(hb*x)%mod
            if ha==hb:
                c+=1
            e+=1
            s+=1

        return c

#Tc - O(NlogN)
#Sc-O(1)





