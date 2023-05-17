# Given a linked list A, remove the B-th node from the end of the list and return its head. For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5. NOTE: If B is greater than the size of the list, remove the first node of the list. NOTE: Try doing it using constant additional space.


# Problem Constraints
# 1 <= |A| <= 106


# Input Format
# The first argument of input contains a pointer to the head of the linked list. The second argument of input contains the integer B.


# Output Format
# Return the head of the linked list after deleting the B-th element from the end.


# Example Input
# Input 1:
# A = 1->2->3->4->5
# B = 2
# Input 2:
# A = 1
# B = 1


# Example Output
# Output 1:
# 1->2->3->5
# Output 2:
  


# Example Explanation
# Explanation 1:
# In the first example, 4 is the second last element.
# Explanation 2:
# In the second example, 1 is the first and the last element.

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        head = A
        length = 1
        if head == None or head.next == None:
            return None
        while head.next != None:
            head = head.next
            length += 1
        if B >= length:
            A = A.next
            return A
        else:
            toremove = length - B + 1
            temp = A
            count = 1
            prev = A
            while count < toremove:
                prev = temp
                temp = temp.next
                count += 1
            if temp.next != None:
                prev.next = temp.next
            else:
                prev.next = None
        return A
       

