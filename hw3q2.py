n = int(input())  # n∈[1,100]
arithmetic_mean = list(range(n, 23*n, n))
geometric_mean = list(range(1, 23))
combined = []
for i in range(22):
    combined.append(arithmetic_mean[i] % 100)
    combined.append((n ** geometric_mean[i]) % 100)
#
#  first line
q = 1
while q <= 9:
    print(combined[q-1], end=' ')
    q += 1
else:
    print(combined[q-1], end='\n')
#
#  2-10 lines
for i in range(2, 11):
    n = combined[2*i - 2]
    if n != 0:
        arithmetic_mean = list(range(n, 6*n, n))
    else:
        arithmetic_mean = [0]*6
    sub_combined = []
    for j in range(5):
        sub_combined.append(arithmetic_mean[j] % 100)
        sub_combined.append((n ** geometric_mean[j]) % 100)
    q = 1
    while q <= 9:
        print(sub_combined[q-1], end=' ')
        q += 1
    else:
        if i != 10:
            print(sub_combined[q-1], end='\n')
        else:
            print(sub_combined[q - 1])