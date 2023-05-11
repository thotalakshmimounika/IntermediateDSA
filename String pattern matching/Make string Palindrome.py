A = "abc"
hash_for = hash_bak = 0
p = 1
mod = 10**9+7
ans = 0
for i, ch in enumerate(A):
    val = ord(ch) - ord('a')
    hash_for = (hash_for * 26 + val) % mod
    hash_bak = (val * p + hash_bak) % mod
    p = p * 26 % mod
    if hash_for == hash_bak:
        ans = max(ans, i + 1 )
print(len(A) - ans)