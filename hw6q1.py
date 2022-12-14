def max_chr(word):
    if len(word) == 1:
        # print(f'The ord of {word[0]} is: {ord(word[0])}')
        return word[0]
    mid = len(word) // 2
    right = max_chr(word[:mid])
    left = max_chr(word[mid:])
    if ord(right) < ord(left):
        return left
    else:
        return right


word = input()
print(max_chr(word))
