#!/usr/bin/env python
# coding: utf-8

# In[1]:


temp1 = float(input())
temp2 = float(input())
temp3 = float(input())
temp1_correct = bool(((-10.0)<temp1) and (temp1<(40.0)))
temp2_correct = bool(((-10.0)<temp2) and (temp2<(40.0)))
temp3_correct = bool(((-10.0)<temp1) and (temp3<(40.0)))
temp1 = ((-10.0<=temp1<=40.0)*temp1 + int(temp1<-10.0)*(-10.0) + int(temp1>40.0)*40.0)
temp2 = ((-10.0<=temp2<=40.0)*temp2 + int(temp2<-10.0)*(-10.0) + int(temp2>40.0)*40.0)
temp3 = ((-10.0<=temp3<=40.0)*temp3 + int(temp3<-10.0)*(-10.0) + int(temp3>40.0)*40.0)
label = 'ERROR'
label = (temp1_correct and temp2_correct and temp3_correct)*("NO ") + label
evg_temp = ((temp1+temp2+temp3)/3.0)
print(label)
print(f'Avg: {evg_temp:2.2f}')
print(f'Rounded Avg: {round(evg_temp)}')


# In[ ]:




