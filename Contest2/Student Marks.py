import functools
a=["f8","m9","o100","o4","c4","z2"]
print(a)
def comp(a,b):
    import functools
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def solve(self, a):
        def comp(a,b):
            if len(a)>=3 or len(b)>=3:
                if a[-3].isdigit() and b[-3].isdigit():
                    n1=int(a[-3:])
                    n2=int(b[-3:])
                    if n1>n2:
                        return -1
                    if n1==n2:
                        return 1
                    else:
                        return 1
                if a[-3].isdigit() and b[-2].isdigit():
                    n1=int(a[-3:])
                    n2=int(b[-2:])
                    if n1>n2:
                        return -1
                    if n1==n2:
                        return 1
                    else:
                        return 1
                if a[-2].isdigit() and b[-3].isdigit():
                    n1=int(a[-2:])
                    n2=int(b[-3:])
                    if n1>n2:
                        return -1
                    if n1==n2:
                        return 1
                    else:
                        return 1
                if a[-3].isdigit() and b[-1].isdigit():
                    n1=int(a[-3:])
                    n2=int(b[-1:])
                    if n1>n2:
                        return -1
                    if n1==n2:
                        return 1
                    else:
                        return 1
                if a[-1].isdigit() and b[-3].isdigit():
                    n1=int(a[-1:])
                    n2=int(b[-3:])
                    if n1>n2:
                        return -1
                    if n1==n2:
                        return 1
                    else:
                        return 1
            if a[-2].isdigit() and b[-2].isdigit():
                n1=int(a[-2:])
                n2=int(b[-2:])
                if n1>n2:
                    return -1
                if n1==n2:
                    return 1
                else:
                    return 1
            elif a[-2].isdigit() and b[-1].isdigit():
                n1=int(a[-2:])
                n2=int(b[-1])
                if n1>n2:
                    return -1
                if n1==n2:
                    return 1
                else:
                    return 1
            elif a[-1].isdigit() and b[-2].isdigit():
                n1=int(a[-1])
                n2=int(b[-2:])
                if n1>n2:
                    return -1
                if n1==n2:
                    return 1
                else:
                    return 1
            elif a[-1].isdigit() and b[-1].isdigit():
                n1=int(a[-1])
                n2=int(b[-1])
                if n1>n2:
                    return -1
                if n1==n2:
                    return 1
                else:
                    return 1
                
                
        a=sorted(a,key=functools.cmp_to_key(comp))
        return a
