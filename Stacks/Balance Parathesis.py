# Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

# Refer to the examples for more clarity.



# Problem Constraints
# 1 <= |A| <= 100



# Input Format
# The first and the only argument of input contains the string A having the parenthesis sequence.



# Output Format
# Return 0 if the parenthesis sequence is not balanced.

# Return 1 if the parenthesis sequence is balanced.



# Example Input
# Input 1:

#  A = {([])}
# Input 2:

#  A = (){
# Input 3:

#  A = ()[] 


# Example Output
# Output 1:

#  1 
# Output 2:

#  0 
# Output 3:

#  1 


# Example Explanation
# You can clearly see that the first and third case contain valid paranthesis.

# In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, a):
        stack=[]
        if a[0]=='{' or a[0]=='(' or a[0]=='[':
            stack.append(a[0])
            tos=0
        else:
            return 0
        for i in range(1,len(a)):
            if a[i]=='{' or a[i]=='(' or a[i]=='[':
                stack.append(a[i])
                tos+=1
            else:
                if a[i]=='}' and stack[tos]=='{' or a[i]==')' and stack[tos]=='(' or a[i]==']' and stack[tos]=='[':
                    stack.pop()
                    tos-=1
                else:
                    return 0
        if len(stack)==0:
            return 1
        return 0
#Time complexity - O(N)
#Space complexity - O(N)