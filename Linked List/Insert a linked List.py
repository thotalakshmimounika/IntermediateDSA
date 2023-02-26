# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None
a = 1,2
b = 3
c= 1
x=ListNode(b)
head=a
tail=a
l=1
while(tail.next!=None):
    l+=1
    tail=tail.next
if c>=l:
    tail.next=x
    tail=x
elif c<=0:
    x.next=head
    head=x
else:
    i=0
    temp=head
    while(i<=c-1 and temp.next!=None):
        temp=temp.next
        i+=1
    x.next=temp.next
    temp.next=x
    print(head)

