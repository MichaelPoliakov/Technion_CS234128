def addition (ls_x, y):
    sum = 0
    i = 0
    while i < len(ls_x):
        sum += int(ls_x[-1-i]) * (10 ** i)
        i += 1
    sum = str(sum + y)
    my_str = [int(ch) for ch in sum]
    return my_str

x = [int(s) for s in input().split(",")]
y = int(input())
print(addition(x,y))