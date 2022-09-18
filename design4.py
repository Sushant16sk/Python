for i in range(6,0,-1):
    for j in range(6-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()