'''
Description: 
version: 
Author: Hubery-Lee
E-mail: hrbeulh@126.com
Date: 2022-10-12 22:37:42
LastEditTime: 2022-10-13 12:03:32
LastEditors: Hubery-Lee
'''
from ROOT import *
#sin(x)
# fw = open("dataError.txt",'w')
# for x in range(-10, 10,1):
#     rndd = TRandom3()
#     errorI=rndd.Uniform(0,0.1)
#     y=sin(x)+errorI
#     fw.write(str(x)+'\t'+str(y)+'\t'+str(errorI)+'\n')
    
#a*exp(-bx)
fw = open("ExpdataError.txt",'w')
for x in range(0, 20,1):
    rndd = TRandom3()
    errorI=rndd.Uniform(0,0.1)
    y=2*exp(-0.2*x)+errorI
    fw.write(str(x)+'\t'+str(y)+'\t'+str(errorI)+'\n')
