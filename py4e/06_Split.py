a = open('mbox-short.txt')

for i in a :
    j = i.rstrip()
    k = j.split()

    if len(k) < 3 or k[0] != 'From' :
        continue
    print(k[2])
