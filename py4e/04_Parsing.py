string = 'X-DSPAM-Confidence: 0.8457 '

where = string.find(' ')
print(where)
check = string[where+1:]
print(check)
type(check)
check2 = float(string[where+1:])
print(check2)
type(check)
