# Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.

# Note: The answer might not fit in an integer, so return your answer % 1000003



# Problem Constraints
# 1 <= |A| <= 1000



# Input Format
# First argument is a string A.



# Output Format
# Return an integer denoting the rank of the given string.



# Example Input
# Input 1:

# A = "acb"
# Input 2:

# A = "a"


# Example Output
# Output 1:

# 2
# Output 2:

# 1


# Example Explanation
# Explanation 1:

# Given A = "acb".
# The order permutations with letters 'a', 'c', and 'b' : 
# abc
# acb
# bac
# bca
# cab
# cba
# So, the rank of A is 2.
# Explanation 2:

# Given A = "a".
# Rank is clearly 1.
m=1000003
def fact(n):
	if n==1 or n==0:
		return 1
	else:
		return (fact(n-1)*n)%m

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, a):
		n=len(a)
		ans=1
		m=1000003
		for i in range(n):
			c=0
			for j in range(i+1,n):
				if a[j]<a[i]:
					c+=1
			ans+=(c*(fact(n-i-1)))%m
		return ans%m
			

#Time complexity - O(N2)- N will be 26 only
#space complexity - O(1)