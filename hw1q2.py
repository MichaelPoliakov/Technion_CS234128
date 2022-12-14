#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = str(input())
b = input()
c = input()
x = int(input())
y = int(input())
string_1 = ''
#string_1 = a*x + c*((y>x)*int(y-x)) + (b+c)*2*(y//x)
leangth_string_1 = x + ((y>x)*int(y-x)) + 4*(y//x)
print(a*x + c*((y>x)*int(y-x)) + (b+c)*2*(y//x))
print (leangth_string_1)

