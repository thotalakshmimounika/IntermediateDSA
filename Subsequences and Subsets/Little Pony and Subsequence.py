# Little Ponny has been given a string A, and he wants to find out the lexicographically minimum subsequence from it of size >= 2. Can you help him?

# A string a is lexicographically smaller than string b, if the first different letter in a and b is smaller in a. For example, "abc" is lexicographically smaller than "acc" because the first different letter is 'b' and 'c' which is smaller in "abc".

 



# Problem Constraints

# 1 <= |A| <= 105

# A only contains lowercase alphabets.



# Input Format

# The first and the only argument of input contains the string, A.



# Output Format

# Return a string representing the answer.



# Example Input

# Input 1:

#  A = "abcdsfhjagj" 
# Input 2:

#  A = "ksdjgha" 


# Example Output

# Output 1:

#  "aa" 
# Output 2:

#  "da" 


# Example Explanation

# Explanation 1:

#  "aa" is the lexicographically minimum subsequence from A. 
# Explanation 2:

#  "da" is the lexicographically minimum subsequence from A. 
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        n=len(a)
        s=''
        m1=a[0]
        for i in range(1,n-1):
            if a[i]<m1:
                m1=a[i]
        s+=m1
        for i in range(n):
            if a[i]==m1:
                m2=a[i+1]
                for j in range(i+1,n):
                    if a[j]<m2:
                        m2=a[j]
                s+=m2
                return s

            

