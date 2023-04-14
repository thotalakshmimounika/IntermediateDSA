# Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

# Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= A[i] <= 10^9

# 1 <= B <= 10^9



# Input Format
# The first argument given is the integer array A.

# The second argument given is integer B.



# Output Format
# Return the number of pairs for which sum is equal to B modulo (10^9+7).



# Example Input
# Input 1:

# A = [1, 1, 1]
# B = 2
# Input 2:

 
# A = [1, 1]
# B = 2


# Example Output
# Output 1:

#  3
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Any two pairs sum up to 2.
# Explanation 2:

#  only pair (1, 2) sums up to 2.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        n=len(a)
        i=0
        j=n-1
        c,ans=0,0
        m=(10**9)+7
        while(i<j):
            if a[i]+a[j]==b:
                if a[i]==a[j]:
                    c=(j-i+1)
                    ans+=(c*(c-1))//2
                    if c==n:
                        return ans%m
                    i+=1
                    j-=1
                else:
                    leftcnt,left=0,a[i]
                    while(left==a[i]):
                        leftcnt+=1
                        i+=1
                    rightcnt,right=0,a[j]
                    while(right==a[j]):
                        rightcnt+=1
                        j-=1
                    ans=(ans%m+(leftcnt*rightcnt)%m)%m
            elif a[i]+a[j]>b:
                j-=1
            else:
                i+=1
        return ans%m
#Time complexity - O(N)
#space complexity - O(1)