# Find the Bth smallest element in given array A .

# NOTE: Users should try to solve it in less than equal to B swaps.



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= B <= min(|A|, 500)

# 1 <= A[i] <= 109



# Input Format
# The first argument is an integer array A.

# The second argument is integer B.



# Output Format
# Return the Bth smallest element in given array.



# Example Input
# Input 1:

# A = [2, 1, 4, 3, 2]
# B = 3
# Input 2:

# A = [1, 2]
# B = 2


# Example Output
# Output 1:

#  2
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  3rd element after sorting is 2.
# Explanation 2:

#  2nd element after sorting is 2.z

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, a,b):
        a=list(a)
        for i in range(0,b):
            min_ind=i
            min_val=a[i]
            for j in range(i,len(a)):
                if a[j]<min_val:
                    min_val=a[j]
                    min_ind=j
            temp=a[i]
            a[i]=min_val
            a[min_ind]=temp
        return a[b-1]
