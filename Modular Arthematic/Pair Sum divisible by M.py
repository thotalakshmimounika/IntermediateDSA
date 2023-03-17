# a =[2,3,4,8,6,15,5,12,17,7,18,10,9,16,21]
# b=6
# Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

# Since the answer may be large, return the answer modulo (109 + 7).



# Problem Constraints
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 109
# 1 <= B <= 106



# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.



# Output Format
# Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5]
#  B = 2
# Input 2:

#  A = [5, 17, 100, 11]
#  B = 28


# Example Output
# Output 1:

#  4
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5). 
#  So total 4 pairs.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        d={}
        n=len(a)
        m=10**9+7
        for i in range(n):
            rem=a[i]%b
            if rem in d:
                d[rem]+=1
            else:
                d[rem]=1
        totalpairsSum=0
        if 0 in d:
            totalpairsSum+= (d[0]*(d[0]-1))//2
        if b%2==0:
            if b//2 in d:
                totalpairsSum+= (d[b//2]*(d[b//2]-1))//2
        for i in range(1,(b+1)//2):
            if i in d and b-i in d:
                totalpairsSum += d[i]*d[b-i]
        return totalpairsSum%m

#Time Complexity - O(N+M/2)~O(N)
#Space Complexity - O(N)
