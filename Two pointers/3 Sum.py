# Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers.

# Assume that there will only be one solution.



# Problem Constraints
# -108 <= B <= 108
# 1 <= N <= 104
# -108 <= A[i] <= 108


# Input Format
# First argument is an integer array A of size N.

# Second argument is an integer B denoting the sum you need to get close to.



# Output Format
# Return a single integer denoting the sum of three integers which is closest to B.



# Example Input
# Input 1:

# A = [-1, 2, 1, -4]
# B = 1
# Input 2:

 
# A = [1, 2, 3]
# B = 6


# Example Output
# Output 1:

# 2
# Output 2:

# 6


# Example Explanation
# Explanation 1:

#  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
# Explanation 2:

#  Take all elements to get exactly 6.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, a,b):
        a.sort()
        n=len(a)
        dif=float('inf')
        for i in range(n-1):
            j=i+1
            k=n-1
            while(j<k):
                s=a[i]+a[j]+a[k]
                if s==b:
                    return a[i]+a[j]+a[k]
                if abs(s-b)<dif:
                    dif=abs(s-b)
                    ans =s
                elif a[i]+a[j]+a[k]>b:
                    k-=1
                else:
                    j+=1
        return ans
            
#Time complexity - O(nlogn +n)
#Space compexity - O(1)