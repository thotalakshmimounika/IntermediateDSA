a='scaler'
b=[[0,2],[2,4]]
n = len(a)
vowels = set(['a', 'e', 'i', 'o', 'u'])
prefix_counts = [0] * (n+1)
for i in range(1, n+1):
    prefix_counts[i] = prefix_counts[i-1] + (a[i-1] in vowels)
counts = []
for query in b:
    start, end = query
    count = prefix_counts[end+1] - prefix_counts[start]
    counts.append(count)
print(counts)
