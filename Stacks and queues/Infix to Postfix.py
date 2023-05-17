# Given string A denoting an infix expression. Convert the infix expression into a postfix expression.

# String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.

# Find and return the postfix expression of A.

# NOTE:

# ^ has the highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.


# Problem Constraints
# 1 <= length of the string <= 500000



# Input Format
# The only argument given is string A.



# Output Format
# Return a string denoting the postfix conversion of A.



# Example Input
# Input 1:

#  A = "x^y/(a*z)+b"
# Input 2:

#  A = "a+b*(c^d-e)^(f+g*h)-i"


# Example Output
# Output 1:

#  "xy^az*/b+"
# Output 2:

#  "abcd^e-fgh*+^*+i-"


# Example Explanation
# Explanation 1:

#  Ouput dentotes the postfix expression of the given input.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        operators={'^':3,'*':2,'/':2,'+':1,'-':1}
        stack=[]
        postfix=""
        for i in range(len(a)):
            curr=a[i]
            if curr.islower():
                postfix+=a[i]
            elif curr in operators:
                if len(stack)==0:
                    stack.append(curr)
                else:
                    while(len(stack)!=0 and stack[-1]!='(' and operators.get(curr)<=operators.get(stack[-1])):
                        postfix+=stack[-1]
                        stack.pop()
                    stack.append(curr)
            elif curr=='(' or curr==')':
                if curr==')':
                    while(len(stack)!=0 and stack[-1]!='('):
                        if stack[-1] in operators:
                            postfix+=stack[-1]
                            stack.pop()
                    stack.pop()
                else:
                    stack.append(curr)
        while stack:
            postfix+=stack[-1]
            stack.pop()
        return postfix
        
                


