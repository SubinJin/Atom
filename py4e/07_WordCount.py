fname = input('Enter File : ')
if len(fname) < 1 :
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        di[w] = di.get(w, 0) + 1

largest = -1
# 왜 None을 하면 안먹힐까요
theword = None
for key, value in di.items() :
    print(key, value)
    if value < largest :
        largest = value
        theword = key

print('Done', theword, largest)
