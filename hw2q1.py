#!/usr/bin/env python
# coding: utf-8

# In[3]:


year = int(input())
day = int(input()) #1-365 day in a particular year counted from January 1st to the current date.

#is it leap year
leap_year = (year%4 == 0) and (year%400 == 0 or year%100 != 0)

m1 = m3 = m5 = m7 = m8 = m10 = 31
m4 = m6 = m9 = m11 = 30
m2 = 28 + int(leap_year)


date_month = max(
    
12*((m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11) < day <= (m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12) ),
11*((m1+m2+m3+m4+m5+m6+m7+m8+m9+m10    ) < day <= (m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11)     ),
10*((m1+m2+m3+m4+m5+m6+m7+m8+m9        ) < day <= (m1+m2+m3+m4+m5+m6+m7+m8+m9+m10)         ),
9 *((m1+m2+m3+m4+m5+m6+m7+m8           ) < day <= (m1+m2+m3+m4+m5+m6+m7+m8+m9)             ),
8 *((m1+m2+m3+m4+m5+m6+m7              ) < day <= (m1+m2+m3+m4+m5+m6+m7+m8)                ),
7 *((m1+m2+m3+m4+m5+m6                 ) < day <= (m1+m2+m3+m4+m5+m6+m7)                   ),
6 *((m1+m2+m3+m4+m5                    ) < day <= (m1+m2+m3+m4+m5+m6)                      ),
5 *((m1+m2+m3+m4                       ) < day <= (m1+m2+m3+m4+m5)                         ),
4 *((m1+m2+m3                          ) < day <= (m1+m2+m3+m4)                            ),
3 *((m1+m2                             ) < day <= (m1+m2+m3)                               ),
2 *((m1                                ) < day <= (m1+m2)                                  ),
1 *((0                                 ) < day <= (m1)                                     ),

)


date_day = day - m1*(date_month>1) - m2*(date_month>2) - m3*(date_month>3) - m4*(date_month>4) - m5*(date_month>5) - m6*(date_month>6) - m7*(date_month>7) - m8*(date_month>8) - m9*(date_month>9) - m10*(date_month>10) - m11*(date_month>11)

print (leap_year)
print (f'{date_day}/{date_month}/{year}')

