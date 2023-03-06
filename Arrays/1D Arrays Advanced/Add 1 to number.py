A=[0,4,6,3,2]
value = int("".join([str(i) for i in A]))
value += 1
ans = [int(x) for x in str(value)]
print(ans)