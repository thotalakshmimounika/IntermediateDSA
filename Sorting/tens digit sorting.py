import functools
class Solution:
        A = [2, 24, 22, 19]
        def comp(a,b):
            ta=(a//10)%10
            tb=(b//10)%10

            if ta<tb:
                return 1
            if a>b and ta==tb:
                return 1
            else:
                return -1
        A=sorted(A,key=functools.cmp_to_key(comp),reverse=True)
        print(A)