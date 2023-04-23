# Given a binary string A of size N. There are Q queries given by the array B of size Q*2.

# Each query has 2 integers :-

# First integer denotes the type of query. Type of query can be either 1 or 2.

# Second integer denotes index x.

# If type = 1, flip the value at index x.

# If type = 2, find the index of nearest 1 from index x. If there are multiple indices, return the one with lower value. If there is no such index, return -1.

# Note :- We use 1-based indexing



# Problem Constraints
# 1 <= N <= 105

# 1 <= Q <= 105

# 1 <= B[i][0] <= 2

# 1 <= B[i][1] <= N



# Input Format
# First argument A is a string.

# Second argument B is a 2D array of integers describing the queries.



# Output Format
# Return an array of integers denoting the answers to each query of type 2.



# Example Input
# Input 1:
# A = "10010"
# B = [[1, 2]
#      [2, 3]]
# Input 2:
# A = "010000100"
# B = [[2, 5]
#      [1, 7]
#      [2, 9]]


# Example Output
# Output 1:
# [2]
# Output 2:
# [7, 2]


# Example Explanation
# For Input 1:
# After first query, A = "11010".
# For second query, X = 3. Both index 2 and index 4 are at the same 
# distance but we choose the lower index.
# For Input 2:
# For first query, the index 2 is at a distance 3 and index 7 is at a distance 2. So we choose
# index 7.
# After second query, A = "010000000"
# For third query, the only index with '1' is 2.

def nearestOne(s,k):
    if len(s)==0:
        return -1
    if k in s:
        return k+1
    c=float('inf')
    res=-1
    for i in s:
        if abs(i-k)<c:
            c=abs(i-k)
            res=i
        elif abs(i-k)==c:
            res=min(res,i)
    return res+1
class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, a,b):
        a=[int(i) for i in a]
        n=len(a)
        s=set()
        ans=[]
        for i in range(n):
            if a[i]==1:
                s.add(i)
        for i in range(len(b)):
            l=b[i][0]
            k=b[i][1]-1
            if l==1:
                if a[k]==1:
                    s.remove(k)
                else:
                    s.add(k)
                a[k]=1-a[k]
            else:
                ans.append(nearestOne(s,k))
        return ans
#Tc - (O(N+Q)*logn)
#Sc- O(N)