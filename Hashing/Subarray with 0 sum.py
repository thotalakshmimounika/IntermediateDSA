# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.



# Problem Constraints
# 1 <= |A| <= 100000

# -10^9 <= A[i] <= 10^9



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return whether the given array contains a subarray with a sum equal to 0.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5]
# Input 2:

#  A = [-1, 1]
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        s=0
        k=set()
        for i in range(len(a)):
            s+=a[i]
            if s==0:
                return 1
            k.add(s) 
        if len(k)!=len(a):
            return 1
        return 0
#Time complexity - O(N)
#Space Complexity - O(N)
    

