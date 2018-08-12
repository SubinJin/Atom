lst = []
for i in range(9) :
    lst.append(int(input()))
print(lst)
for j in range(8) :
    for k in range(j + 1, 9) :
        a = sum(lst)-lst[j]-lst[k]
        if a == 100 :
            lst.pop(k)
            lst.pop(j)
            lst.sort()
            for l in range(7) :
                print(lst[l])
            break
