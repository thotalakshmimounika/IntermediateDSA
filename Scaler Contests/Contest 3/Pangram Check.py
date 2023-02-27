s = ['the','quick','brown','fox','jumps','over','the','lazy','dog']
listToStr = ''.join(map(str, s))
print(listToStr)
s=set(listToStr)
d=set()
for i in listToStr:
    d.add(i)
if len(d)==26:
    print(1)

