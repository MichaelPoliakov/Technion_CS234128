def print_binary(num):
    if num < 2:
        return num % 2
    return 10 * print_binary(num // 2) + (num % 2)


num = int(input())
print(print_binary(num))
