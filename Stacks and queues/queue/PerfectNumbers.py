# Given an integer A, you have to find the Ath Perfect Number.

# A Perfect Number has the following properties:

# It comprises only 1 and 2.
# The number of digits in a Perfect number is even.
# It is a palindrome number.
# For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



# Problem Constraints
# 1 <= A <= 100000



# Input Format
# The only argument given is an integer A.



# Output Format
# Return a string that denotes the Ath Perfect Number.



# Example Input
# Input 1:

#  A = 2
# Input 2:

#  A = 3


# Example Output
# Output 1:

#  22
# Output 2:

#  1111


# Example Explanation
# Explanation 1:

# First four perfect numbers are:
# 1. 11
# 2. 22
# 3. 1111
# 4. 1221
# Return the 2nd Perfect number.
# Explanation 2:

# First four perfect numbers are:
# 1. 11
# 2. 22
# 3. 1111
# 4. 1221
# Return the 3rd Perfect number.

from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, a):
        q=deque()
        if a==1:
            return '11'
        if a==2:
            return '22'
        q.append('1')
        q.append('2')
        c,ans=2,0
        while True:
            num=q.popleft()
            q.append(num+'1')
            c+=1
            if a==c:
                ans=num+'1'
                break
            q.append(num+'2')
            c+=1
            if a==c:
                ans=num+'2'
                break
        return ans+ans[::-1]
            


