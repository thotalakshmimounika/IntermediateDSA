
        def countfactors(a):
            c=0
            for i in range(1,int(a**(0.5))+1):
                if a%i==0:
                    if i==a/i:
                        c+=1
                    else:
                        c+=2
            return c
        a.sort()
        a.sort(key=countfactors)
        return a