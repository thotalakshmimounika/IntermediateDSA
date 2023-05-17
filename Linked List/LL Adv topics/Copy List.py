# You are given a linked list A
# Each node in the linked list contains two pointers: a next pointer and a random pointer
# The next pointer points to the next node in the list
# The random pointer can point to any node in the list, or it can be NULL
# Your task is to create a deep copy of the linked list A
# The copied list should be a completely separate linked list from the original list, but with the same node values and random pointer connections as the original list
# You should create a new linked list B, where each node in B has the same value as the corresponding node in A
# The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)


# Problem Constraints
# 0 <= |A| <= 106



# Input Format
# The first argument of input contains a pointer to the head of linked list A.



# Output Format
# Return a pointer to the head of the required linked list.



# Example Input
# Given list
#    1 -> 2 -> 3
# with random pointers going from
#   1 -> 3
#   2 -> 1
#   3 -> 1
  


# Example Output
#    1 -> 2 -> 3
# with random pointers going from
#   1 -> 3
#   2 -> 1
#   3 -> 1

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def init(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        #Add new nodes between original
        t = head
        while(t):
            temp = t.next
            x = RandomListNode(t.label)
            t.next = x
            x.next = temp
            t = temp

        #Assign random pointer of new nodes
        t = head
        while(t):
            if t.random:
                t.next.random = t.random.next
            t = t.next.next
       
        new_head = head.next

        #Separate original LL and new LL
        t=head
        while(t):
            temp = t.next.next
            if temp:
                t.next.next = temp.next
                t.next = temp
            else:
                t.next.next = None
                t.next = None
            t = temp

        return new_head