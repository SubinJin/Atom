fname = input('Enter File : ')
if len(fname) < 1 :
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        di[word] = di.get(word, 0) + 1

tmp = list()
for key, value in di.items() :
    newtmp = (value, key)
    tmp.append(newtmp)

tmp = sorted(tmp, reverse = True)

for value, key in tmp[:10] :
    print(key, value)
