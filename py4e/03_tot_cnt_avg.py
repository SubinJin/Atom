tot = 0
cnt = 0
avg = 0

while True :
    val = input('Enter prime number : ')

    if val == 'done' :
        break
    else :
        try :
            num = float(val)
            tot = tot + num
            cnt = cnt + 1
            avg = tot / cnt
        except :
            print('bad data')
            continue
print('tot = ', tot)
print('cnt = ', cnt)
print('avg = ', avg)
