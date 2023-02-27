# Given heads of two linked lists A and B, check if they are identical i.e. each of their corresponding nodes should contain the same data. The two given linked lists may or may not be of the same length.


# Problem Constraints
# 1 <= size of linked lists <= 105

# 1 <= value of each node <= 109



# Input Format
# You are given the head of two linked lists A and B.


# Output Format
# Return 1 if both the linked lists are identical and 0 otherwise


# Example Input
# Input 1:
# A = 1 -> 2 -> 3
# B = 1 -> 2 -> 3
# Input 2:
# A = 4 -> 3 -> 2 -> 1
# B = 4 -> 2 -> 3 -> 1


# Example Output
# Output 1:
# 1
# Output 2:
# 0


# Example Explanation
# For Input 1:
# Both the linked lists are identical
# For Input 2:
# The value in the second node of both the linked lists
# are different.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return an integer
    def solve(self, A, B):
        t1=A
        t2=B
        while(t1!=None and t2!=None):
            if t1.val!=t2.val:
                return 0
            t1=t1.next
            t2=t2.next
        return 1
