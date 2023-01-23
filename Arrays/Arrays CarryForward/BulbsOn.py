# A wire connects N light bulbs.

# Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.

# Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

# You can press the same switch multiple times.

# Note: 0 represents the bulb is off and 1 represents the bulb is on.
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, a):
        n=len(a)
        count = 0
        for i in range(n):
            if (a[i] == 1 and count % 2 == 0):
                continue
            elif a[i]==0 and count%2!=0:
                continue
            elif a[i]==1 and count%2!=0:
                count+=1
            elif a[i]==0 and count%2==0:
                count+=1
        return count
#or

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, a):
        n=len(a)
        count = 0
        for i in range(n):
            if (a[i] == 1 and count % 2 == 0):
                continue
            elif a[i]==0 and count%2!=0:
                continue
            elif a[i]==1 and count%2!=0:
                count+=1
            elif a[i]==0 and count%2==0:
                count+=1
        return count