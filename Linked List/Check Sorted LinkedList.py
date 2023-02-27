# You are given the head of a linked list A. Check if the data inside it exists in non-decreasing order.



# Problem Constraints
# 1 <= size of linked list <= 105
# 1 <= value of nodes <= 109



# Input Format
# The first argument A is the head of a linked list.



# Output Format
# Return 1 if the data of nodes is non-decreasing and 0 otherwise



# Example Input
# Input 1:
# A = 1 -> 2 -> 3 -> 3
# Input 2:
# A = 4 -> 3 -> 2 -> 1


# Example Output
# Output 1:
# 1
# Output 2:
# 0


# Example Explanation
# For Input 1:
# The data of nodes follow a non-decreasing order.
# For Input 2:
# The data of nodes are not in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, a):
        temp=a
        i=0
        while(temp.next!=None):
            if temp.val>temp.next.val:
                return 0
            temp=temp.next
        return 1
            

