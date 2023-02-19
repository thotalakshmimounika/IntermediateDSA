A=3
B=2
_str = '01'
for i in range(1, A):
    _rStr = ''
    for val in _str:
        if val == '0':
            _rStr += '1'
        else:
            _rStr += '0'
    _str += _rStr
print(int(_str[B]))
