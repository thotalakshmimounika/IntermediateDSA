# Given an integer array A of size N.

# If we store the sum of each triplet of the array A in a new list, then find the Bth smallest element among the list.

# NOTE: A triplet consists of three elements from the array. Let's say if A[i], A[j], A[k] are the elements of the triplet then i < j < k.



# Problem Constraints
# 3 <= N <= 500
# 1 <= A[i] <= 108
# 1 <= B <= (N*(N-1)*(N-2))/6



# Input Format
# The first argument is an integer array A.
# The second argument is an integer B.



# Output Format
# Return an integer denoting the Bth element of the list.



# Example Input
# Input 1:

#  A = [2, 4, 3, 2]
#  B = 3
# Input 2:

#  A = [1, 5, 7, 3, 2]
#  B = 9


# Example Output
# Output 1:

#  9 
# Output 2:

#  14


# Example Explanation
# Explanation 1:

#  All the triplets of the array A are:

#  (2, 4, 3) = 9
#  (2, 4, 2) = 8
#  (2, 3, 2) = 7
#  (4, 3, 2) = 9

#  So the 3rd smallest element is 9.

def countoflesserelemSum(a,mid,n):
    c=0
    for i in range(n-2):
        j,k=i+1,n-1
        while(j<k):
            if (a[i]+a[j]+a[k])<mid:
                c+=(k-j)
                j+=1
            else:
                k-=1
    return c
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        a.sort()
        n=len(a)
        left=3
        right=3000000000
        while(left<=right):
            mid=(left+right)//2
            x=countoflesserelemSum(a,mid,n)
            if x>=b:
                right=mid-1
            else:
                ans=mid
                left=mid+1
        return ans

