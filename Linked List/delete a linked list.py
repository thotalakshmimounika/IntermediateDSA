# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    
    def solve(self, a,b):
        temp=a
        l=1
        while(temp.next!=None):
            l+=1
            temp=temp.next
        if b==0:
            a=a.next
        elif b==l:
            h=a
            if h==None: return
            if h.next==None:
                h=None
            while(h.next.next!=None):
                h=h.next
            h.next=None
        else:
            cn=a
            i=0
            while(i<=b-1):
                if i==b-1:
                    cn.next=cn.next.next
                cn=cn.next
                i+=1
            return a