# You are given the head of a linked list A and an integer B. You need to find the B-th element of the linked list.

# Note : Follow 0-based indexing for the node numbering.



# Problem Constraints
# 1 <= size of linked list <= 105

# 1 <= value of nodes <= 109

# 0 <= B < size of linked list



# Input Format
# The first argument A is the head of a linked list.

# The second arguement B is an integer.



# Output Format
# Return an integer.



# Example Input
# Input 1:
# A = 1 -> 2 -> 3
# B = 0
# Input 2:
# A = 4 -> 3 -> 2 -> 1
# B = 1


# Example Output
# Output 1:
# 1
# Output 2:
# 3


# Example Explanation
# For Input 1:
# The 0-th element of the linked list is 1.
# For Input 2:
# The 1-st element of the linked list is 3.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, a,b):
        temp=a
        i=0
        while(i<=b):
            if i==b:
                return temp.val
            temp=temp.next
            i+=1