#A wire connects N light bulbs.Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
a = [0, 1, 0, 1]
ans=c=0
for i in a:
    if i==0:
        c+=1
    elif i!=0 and c>=1:
        ans+=2
        c=0
if c>0:
    print(ans+1   ) 
else:
    print(ans)
            
            
        
