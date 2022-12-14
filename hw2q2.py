#!/usr/bin/env python
# coding: utf-8

# In[ ]:


char_1 = ord(input())
char_2 = ord(input())
char_3 = ord(input())

#print(f'{char_1}, {char_2}, {char_3}')

char_1 = (ord('A') <= char_1 <= ord('Z'))*(char_1 - ord('A') + 1) + (ord('a') <= char_1 <= ord('z'))*(char_1 - ord('a') + 1)
char_2 = (ord('A') <= char_2 <= ord('Z'))*(char_2 - ord('A') + 1) + (ord('a') <= char_2 <= ord('z'))*(char_2 - ord('a') + 1)
char_3 = (ord('A') <= char_3 <= ord('Z'))*(char_3 - ord('A') + 1) + (ord('a') <= char_3 <= ord('z'))*(char_3 - ord('a') + 1)

a = min(char_3,char_2,char_1)
c = max(char_3,char_2,char_1)
b = (char_3 + char_2 + char_1 - a - c)
#print(f'{char_1}, {char_2}, {char_3}') 
print(f'{a}{b}{c}')

