# Write a recursive function that, given a string S, prints the characters of S in reverse order.



# Problem Constraints
# 1 <= |s| <= 1000



# Input Format
# First line of input contains a string S.



# Output Format
# Print the character of the string S in reverse order.



# Example Input
# Input 1:

#  scaleracademy
# Input 2:

#  cool


# Example Output
# Output 1:

#  ymedacarelacs
# Output 2:

#  looc


# Example Explanation
# Explanation 1:

#  Print the reverse of the string in a single line.

import sys
sys.setrecursionlimit(10**6)
def revstring(a):
    n=len(a)
    if n<=0:
        return ''
    else:
        return a[n-1]+revstring(a[:-1])

def main():
    s=input()
    ans= revstring(s)
    print(ans)
if __name__ == '__main__':
    main()