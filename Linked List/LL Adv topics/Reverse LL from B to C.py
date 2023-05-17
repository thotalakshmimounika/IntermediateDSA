# Reverse a linked list A from position B to C.

# NOTE: Do it in-place and in one-pass.



# Problem Constraints
# 1 <= |A| <= 106

# 1 <= B <= C <= |A|



# Input Format
# The first argument contains a pointer to the head of the given linked list, A.

# The second arugment contains an integer, B.

# The third argument contains an integer C.



# Output Format
# Return a pointer to the head of the modified linked list.



# Example Input
# Input 1:

#  A = 1 -> 2 -> 3 -> 4 -> 5
#  B = 2
#  C = 4

# Input 2:

#  A = 1 -> 2 -> 3 -> 4 -> 5
#  B = 1
#  C = 5


# Example Output
# Output 1:

#  1 -> 4 -> 3 -> 2 -> 5
# Output 2:

#  5 -> 4 -> 3 -> 2 -> 1


# Example Explanation
# Explanation 1:

#  In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
#  Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 
# Explanation 2:

#  In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5  
#  Thus, the output is 5 -> 4 -> 3 -> 2 -> 1 

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, a, b,c):
        def reversell(k):
            head2=k
            curr=head2
            prev=None
            while(curr!=None):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            head2=prev
            return head2
        head=a
        if (head==None or head.next==None):
            return head
        count=0
        first,fro,to,second=None,None,None,None
        while(a!=None):
            count+=1
            if count<b:
                first=a
            if count==b:
                fro=a
            if count==c:
                to=a
                break
            a=a.next
        second=to.next
        to.next=None
        z=reversell(fro)
        if first!=None:
            first.next=z
        else:
            head=z
        m=head
        while(m.next!=None):
            m=m.next
        m.next=second
        return head

        






        








