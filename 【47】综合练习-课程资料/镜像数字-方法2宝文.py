a = input('数字：')
if len(a) == 1:
    if a == '1' or a == '0' or a == '8':
        print('是')
    else:
        print('不是')

elif len(a) % 2 == 0:
    b = 0
    c = -1
    d = 0
    for i in range(int(len(a)/2 - 1)):
        if a[b] == a[c] and a[b] == '1' or a[b] == '0' or a[b] == '8':
            b = b+1
            c = c-1
        elif a[b] == '9' and a[c] == '6':
            b = b+1
            c = c-1
        elif a[b] == '6' and a[c] == '9':
            b = b+1
            c = c-1
        else:
            print('不是')
            d = 1
            break
    if d == 0:
        print('是')

elif len(a) % 2 == 1:
    b = 0
    c = -1
    d = 0
    for i in range(int(len(a)/2 - 0.5)):
        if a[b] == a[c] and a[b] == '1' or a[b] == '0' or a[b] == '8':
            b = b+1
            c = c-1
        elif a[b] == '9' and a[c] == '6':
            b = b+1
            c = c-1
        elif a[b] == '6' and a[c] == '9':
            b = b+1
            c = c-1
        else:
            print('不是')
            d = 1
            break
    if d == 0:
        if a[int(len(a)/2 - 0.5)] == '0' or a[int(len(a)/2 - 0.5)] == '1' or a[int(len(a)/2 - 0.5)] == '8':
            print('是')
