A= [5, -2, 3 , 1, 2]
B = 3
N=len(A)
leftSum = [0] * N
rightSum = [0] * N
maxSum = 0

# Fill leftSum array
leftSum[0] = A[0]
for i in range(1, N):
    leftSum[i] = max(leftSum[i-1], leftSum[i-1] + A[i])

# Fill rightSum array
rightSum[N-1] = A[N-1]
for i in range(N-2, -1, -1):
    rightSum[i] = max(rightSum[i+1], rightSum[i+1] + A[i])

# Find the maximum sum
for b in range(1,B+1):
    for i in range(0, N-b+1):
        maxSum = max(maxSum, leftSum[i] + rightSum[i])

print(maxSum)

            
