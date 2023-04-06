# Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. Return sum % (109 + 7) as an output.



# Problem Constraints
# 1 <= length of the array A <= 105

# 1 <= A[i] <= 103



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return a single integer denoting sum % (109 + 7).



# Example Input
# Input 1:

#  A = [1, 2, 3]
# Input 2:

#  A = [17, 100, 11]


# Example Output
# Output 1:

#  5
# Output 2:

#  61


# Example Explanation
# Explanation 1:

#  (1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2) + (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        M=10**9+7
        contrib=[0]*1001
        #since 1 <= A[i] <= 10**3 : max value=1000

        for i in A: # made an index array with count details
            contrib[i]+=1# for every elemnt in A , we have their count or contribution

        ans=0
        for i in range(1,1001):
            for j in range(1,1001):              
                ans+=((i%j)*contrib[i]*contrib[j])%M

# here i and j are elemnts in A and contrib[] array gives their count in A
                ans=ans%M

        return ans    




