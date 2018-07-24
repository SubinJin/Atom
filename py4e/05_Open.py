open = open('mbox-short.txt')
print(open)

for i in open :
    # print(i) 이렇게 하면 개행이 너무 많이 됨

    a = i.rstrip() # 개행을 없애줌
    print(a.upper())
