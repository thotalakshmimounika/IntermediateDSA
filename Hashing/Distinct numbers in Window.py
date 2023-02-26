# You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

# Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

# NOTE: if B > N, return an empty array.



# Input Format
# First argument is an integer array A
# Second argument is an integer B.



# Output Format
# Return an integer array.



# Example Input
# Input 1:

#  A = [1, 2, 1, 3, 4, 3]
#  B = 3
# Input 2:

#  A = [1, 1, 2, 2]
#  B = 1


# Example Output
# Output 1:

#  [2, 3, 3, 2]
# Output 2:

#  [1, 1, 1, 1]


# Example Explanation
# Explanation 1:

#  A=[1, 2, 1, 3, 4, 3] and B = 3
#  All windows of size B are
#  [1, 2, 1]
#  [2, 1, 3]
#  [1, 3, 4]
#  [3, 4, 3]
#  So, we return an array [2, 3, 3, 2].
# Explanation 2:

#  Window size is 1, so the output array is [1, 1, 1, 1].

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, a,b):
        n=len(a)
        d={}
        ans=[]
        for i in range(b):
            if a[i] in d:
                d[a[i]]+=1
            else:
                d[a[i]]=1
        ans.append(len(d))
        s=1
        e=b
        while(s<n and e<n):
            d[a[s-1]]-=1
            if d[a[s-1]]==0:
                d.pop(a[s-1])
            if a[e] in d:
                d[a[e]]+=1
            else:
                d[a[e]]=1
            ans.append(len(d))
            s+=1
            e+=1
        return ans
                
#time complexity - it depends on b size - worstcase - O(N^2)
#space complexity - O(N)