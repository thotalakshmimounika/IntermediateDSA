# Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.

# For this problem, return the indices of maximum continuous series of 1s in order.

# If there are multiple possible solutions, return the sequence which has the minimum start index.



# Problem Constraints
# 0 <= B <= 105

# 1 <= size(A) <= 105

# 0 <= A[i] <= 1



# Input Format
# First argument is an binary array A.

# Second argument is an integer B.



# Output Format
# Return an array of integers denoting the indices(0-based) of 1's in the maximum continuous series.



# Example Input
# Input 1:

#  A = [1 1 0 1 1 0 0 1 1 1 ]
#  B = 1
# Input 2:

#  A = [1, 0, 0, 0, 1, 0, 1]
#  B = 2


# Example Output
# Output 1:

#  [0, 1, 2, 3, 4]
# Output 2:

#  [3, 4, 5, 6]


# Example Explanation
# Explanation 1:

#  Flipping 0 present at index 2 gives us the longest continous series of 1's i.e subarray [0:4].
# Explanation 2:

#  Flipping 0 present at index 3 and index 5 gives us the longest continous series of 1's i.e subarray [3:6].

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, a,b):
        j=0
        n=len(a)
        cnt,res,zero=0,0,0
        low,high=0,0
        ans=0
        for i in range(n):
            if a[i]==1:
                cnt+=1
            elif a[i]==0:
                cnt+=1
                zero+=1
                while(zero>b):
                    if a[j]==0:
                        zero-=1
                    j+=1
            if res<cnt and ans <(i-j+1):
                ans=max(ans,i-j+1)
                low=max(low,j)
                high=max(i,high)
                res=cnt
        m=[]
        for k in range(low,high+1):
            m.append(k)
        return m





                    


