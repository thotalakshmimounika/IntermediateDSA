# Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return the modified linked list.



# Problem Constraints
# 1 <= |A| <= 103

# B always divides A



# Input Format
# The first argument of input contains a pointer to the head of the linked list.

# The second arugment of input contains the integer, B.



# Output Format
# Return a pointer to the head of the modified linked list.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5, 6]
#  B = 2
# Input 2:

#  A = [1, 2, 3, 4, 5, 6]
#  B = 3


# Example Output
# Output 1:

#  [2, 1, 4, 3, 6, 5]
# Output 2:

#  [3, 2, 1, 6, 5, 4]


# Example Explanation
# Explanation 1:

#  For the first example, the list can be reversed in groups of 2.
#     [[1, 2], [3, 4], [5, 6]]
#  After reversing the K-linked list
#     [[2, 1], [4, 3], [6, 5]]
# Explanation 2:

#  For the second example, the list can be reversed in groups of 3.
#     [[1, 2, 3], [4, 5, 6]]
#  After reversing the K-linked list
#     [[3, 2, 1], [6, 5, 4]]

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, a,b):
        dummy=ListNode(None)
        head=a
        dummy.next=head
        prev,curr,nex=dummy,dummy,dummy
        c=0
        while(curr.next!=None):
            curr=curr.next
            c+=1
        if c%b==0:
            while(c>0):
                curr=prev.next
                nex=curr.next
                for i in range(1,b):
                    curr.next=nex.next
                    nex.next=prev.next
                    prev.next=nex
                    nex=curr.next
                prev=curr
                c=c-b
            return dummy.next
        return 