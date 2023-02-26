# You are given A which is the head of a linked list. Also given is the value B and position C. Complete the function that should insert a new node with the said value at the given position.

# Notes:

# In case the position is more than length of linked list, simply insert the new node at the tail only.
# In case the pos is 0 or less, simply insert the new node at head only.
# Follow 0-based indexing for the node numbering.


# Problem Constraints
# 1 <= size of linked list <= 105

# 1 <= value of nodes <= 109

# 1 <= B <= 109

# 0 <= C <= 105



# Input Format
# The first argument A is the head of a linked list.

# The second argument B is an integer which denotes the value of the new node

# The third argument C is an integer which denotes the position of the new node



# Output Format
# Return the head of the linked list


# Example Input
# Input 1:
# A = 1 -> 2
# B = 3
# C = 0
# Input 2:
# A = 1 -> 2
# B = 3
# C = 1


# Example Output
# Output 1:
# 3 -> 1 -> 2
# Output 2:
# 1 -> 3 -> 2


# Example Explanation
# For Input 1:
# The new node is add to the head of the linked list
# For Input 2:
# The new node is added after the first node of the linked list

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A,B,C):
        head = A
        tail = A
        length = 1
        newNode = ListNode(B)
        while tail.next != None:
            length += 1
            tail = tail.next
        if C >= length:
            tail.next = newNode
            tail = newNode
        elif C <= 0:
            newNode.next = head
            head = newNode
        else:
            currNode = A
            currPos = 0
            while currPos <= C-1:
                if currPos == C-1:
                    newNode.next = currNode.next
                    currNode.next = newNode
                currPos += 1
                currNode = currNode.next
        return head