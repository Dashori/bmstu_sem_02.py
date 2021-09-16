##треугольник вокруг центра

import pygame as p
from math import *

triagle=[[100,300],[50,400],[160,400]]
center=[100,350]

sc = p.display.set_mode((400, 600))

def rotate(coord,phi):
    rot =(coord[0]*cos(phi)-coord[1]*sin(phi),coord[1]*cos(phi)+coord[0]*sin(phi))
    return rot
def line(coord):
    line_1=(coord[0]+0.003,coord[1]-0.003)
    return line_1
run=True
while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            
    sc.fill('white')
    p.draw.polygon(sc,'green',triagle)

    phi=0.001
    for i in range(3):
        triagle[i]=(triagle[i][0]-center[0], triagle[i][1]-center[1])
        triagle[i]=rotate(triagle[i],phi)
        triagle[i]=(triagle[i][0]+center[0],triagle[i][1]+center[1])
        center=line(center)

   
    p.display.flip()


p.quit()

