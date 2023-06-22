# Given a positive integer A, write a program to find the Ath Fibonacci number.

# In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.

# NOTE: 0th term is 0. 1th term is 1 and so on.



# Problem Constraints
# 0 <= A <= 44



# Input Format
# First and only argument is an integer A.



# Output Format
# Return an integer denoting the Ath Fibonacci number.



# Example Input
# Input 1:

#  A = 4
# Input 2:

#  A = 6


# Example Output
# Output 1:

#  3
# Output 2:

#  8

def fib(n,dp):
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    ans=fib(n-1,dp)+fib(n-2,dp)
    dp[n]=ans
    return ans

def main():
    n=int(input())
    dp=[-1]*(n+1)
    print(fib(n,dp))
if __name__ == '__main__':
    main()

#TC-O(N)|| SC- O(N)

#Method -2
def main():
    n=int(input())
    a,b=0,1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print(b)
    return 0

if __name__ == '__main__':
    main()
    
#TC-O(N)|| SC- O(1)