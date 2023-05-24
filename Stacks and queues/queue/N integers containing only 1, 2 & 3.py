a=7
from collections import deque
q=deque()
q.append('1')
q.append('2')
q.append('3')
ans=['1','2','3']
c=3
while(True):
    num=q.popleft()
    q.append(num+'1')
    c+=1
    ans.append(num+'1')
    if c==a:
        break
    q.append(num+'2')
    c+=1
    ans.append(num+'2')
    if c==a:
        break
    q.append(num+'3')
    c+=1
    ans.append(num+'3')
    if c==a:
        break
print([int(x) for x in ans])



