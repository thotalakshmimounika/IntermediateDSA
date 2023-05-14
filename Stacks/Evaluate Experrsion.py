# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each string may be an integer or an operator.



# Problem Constraints
# 1 <= N <= 105



# Input Format
# The only argument given is string array A.



# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.



# Example Input
# Input 1:
#     A =   ["2", "1", "+", "3", "*"]
# Input 2:
#     A = ["4", "13", "5", "/", "+"]


# Example Output
# Output 1:
#     9
# Output 2:
#     6


# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     13 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, a):
        stack=[]
        tos1,tos2=-2,-1
        for i in range(len(a)):
            if a[i]!="+" and a[i]!="-" and a[i]!="/" and a[i]!="*":
                stack.append(a[i])
                tos2+=1
                tos1+=1
            else:
                if a[i]=="+":
                    ans=int(stack[tos1])+int(stack[tos2])
                elif a[i]=="-":
                    ans=int(stack[tos1])-int(stack[tos2])
                elif a[i]=='*':
                    ans=int(stack[tos1])*int(stack[tos2])
                elif a[i]=='/':
                    ans=int(stack[tos1])//int(stack[tos2])
                stack.pop()
                stack.pop()
                stack.append(str(ans))
                tos1-=1
                tos2-=1
        return int(stack[0])

