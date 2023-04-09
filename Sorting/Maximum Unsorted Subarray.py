# Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.



# Problem Constraints
# 1 <= N <= 1000000
# 1 <= A[i] <= 1000000



# Input Format
# First and only argument is an array of non-negative integers of size N.



# Output Format
# Return an array of length two where the first element denotes the starting index(0-based) and the second element denotes the ending index(0-based) of the sub-array. If the array is already sorted, return an array containing only one element i.e. -1.



# Example Input
# Input 1:

# A = [1, 3, 2, 4, 5]
# Input 2:

# A = [1, 2, 3, 4, 5]


# Example Output
# Output 1:

# [1, 2]
# Output 2:

# [-1]


# Example Explanation
# Explanation 1:

# If we sort the sub-array A1, A2, then the whole array A gets sorted.
# Explanation 2:

# A is already sorted.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, a):
        n=len(a)
        p1=0
        p2=n-1

        for i in range(1,n):
            if a[i]<a[i-1]:
                p1=i-1
                break
        for i in range(n-1,0,-1):
            if a[i]<a[i-1]:
                p2=i
                break
        if p1==0 and p2==n-1:
            return [-1]
        minele=a[p1]
        maxele=a[p1]
        for i in range(p1+1,p2+1):
            minele=min(a[i],minele)
            maxele=max(a[i],maxele)
        x1,x2=0,0
        for i in range(n):
            if a[i]>minele:
                x1=i
                break
        for i in range(n-1,-1,-1):
            if a[i]<maxele:
                x2=i
                break
        return [x1,x2]

        


