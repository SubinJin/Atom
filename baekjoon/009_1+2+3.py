anslst = [i * 0 for i in range(10)]
anslst[0] = 1
anslst[1] = 2
anslst[2] = 4
for i in range(3, 10) :
    anslst[i] = anslst[i - 1] + anslst[i - 2] + anslst[i - 3]

n = input()
for i in range(int(n)) :
    print(anslst[int(input())-1])
