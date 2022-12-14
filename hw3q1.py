kind = int(input())  # 0 for ALEPH. 1 for BEIT.
leangth = int(input())
if kind == 0:
    leangth -= 1
    for i in range(leangth + 1):
        line_odd = [' ']*i + ['*']*(leangth + 1 - i)
        # print(line_odd)
        print(''.join(line_odd))
elif leangth % 2 != 0:  # kind not 0, meaning it is 1. but we still should varify that it is olso not a prime leangth..
    #leangth += 1
    i = 0
    while i <= leangth:
        line = [' '] * ((leangth-(i+1)) // 2) + ['*'] * (i+1)
        print(''.join(line))  # line prime    {0, 2, 4, 6, ..., leangth+1}
        print(''.join(line))  # line odd      {1, 3, 5, ..., leangth}
        i += 2
else:
    print('ERROR')