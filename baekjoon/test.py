a = int(input())
count = 0
alst = [a]

def cal(a) :
    lst = []
    for i in a :
        lst.append(i-1)
        if i % 2 == 0 :
            lst.append(i/2)
        if i % 3 == 0 :
            lst.append(i/3)
    return lst

while True :
    if a == 1 :
        print(count)
        break

    tmp = alst[:]
    alst = []
    alst = cal(tmp)
    count += 1

    if min(alst) == 1 :
        print(count)
        break
