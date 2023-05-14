# Given a stack of integers A, sort it using another stack.

# Return the array of integers after sorting the stack using another stack.



# Problem Constraints
# 1 <= |A| <= 5000

# 0 <= A[i] <= 109



# Input Format
# The only argument is a stack given as an integer array A.



# Output Format
# Return the array of integers after sorting the stack using another stack.



# Example Input
# Input 1:

#  A = [5, 4, 3, 2, 1]
# Input 2:

#  A = [5, 17, 100, 11]


# Example Output
# Output 1:

#  [1, 2, 3, 4, 5]
# Output 2:

#  [5, 11, 17, 100]


# Example Explanation
# Explanation 1:

#  Just sort the given numbers.
# Explanation 2:

#  Just sort the given numbers.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, a):
        n=len(a)
        stack=[]
        while(len(a)!=0):
            x=a.pop()
            while(len(stack)!=0 and stack[-1]>x):
                l=stack.pop()
                a.append(l)
            if len(stack)==0:
                stack.append(x)
            else:
                stack.append(x)
        return stack

            
