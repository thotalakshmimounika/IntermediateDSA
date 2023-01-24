N = 3
trust = [[1,3],[2,3]]
count = [0]*(N+1)
print(count)
for i,j in trust:
    print(i,j)
    count[i]-=1#outdegree
    count[j]+=1#indegree
    print(count)
print(count)
for i in range(1,N+1):
    if count[i] == N-1:
        print(i)
print(-1)
