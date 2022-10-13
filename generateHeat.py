'''
Description: 采用以下代码生成磁场数据
Version: 
Author: Hubery-Lee
E-mail: hrbeulh@126.com
Date: 2022-10-13 16:05:38
LastEditTime: 2022-10-13 16:26:22
LastEditors: Hubery-Lee
'''

import math

V = [[0 for x in range(0,101,1)] for y in range(0,101,1)]
pot = 1000
for i in range(1000):       # 1000 iterations should be enough
    for x in range(30,71,1):        #keep two plates at +pot and -pot respectiVely
        V[x][70]=pot
        V[x][30] =-pot
    for x in range(1,100,1):
        for y in range(1,100,1):
            V[x][y] = (V[x+1][y]+V[x-1][y+1]+V[x][y-1])/4.
            V[x][0] = (V[x-1][0]+V[x+1][0]+V[x][1])/3.       #top and bottom border
            V[x][100] = (V[x-1][100] +V[x+1][100]+V[x][99])/3.
    for y in range(1,100,1):
        V[0][y] = (V[0][y-1]+V[0][y+1]+V[1][y])/3.           #left and right border
        V[100][y] = (V[100][y-1]+V[100][y+1]+V[99][y])/3.
    V[0][0]=(V[1][0]+V[0][1])/2.         #corners
    V[0][100]=(V[0][99]+V[1][100])/2.
    V[100][0]=(V[99][0]+V[100][1])/2.
    V[100][100]=(V[100][99]+V[99][100])/2.
    print("Iteration " + str(i))
for x in range(30,71,1):
    V[x][70]=pot
    V[x][30] =-pot

file = open("potential_field.dat", "w")     #write to file
for x in range(0,101,1):
    for y in range(0,101,1):
        file.write(str(x)+" "+ str(y) + " "+ str(V[x][y]))
        if x!= 0 and x!= 100 and y!=0 and y!= 100:
            Ex = -(V[x+1][y] -V[x-1][y])/2.
            Ey = -(V[x][y+1] -V[x][y-1])/2.
            file.write(" "+str(Ex)+" "+str(Ey))
        file.write("\n")
    file.write("\n")
file.close()

 
