s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join(map(str, s))
s=set(listToStr)
for i in range(26):
    if chr(97+i) not in s:
        print(0)