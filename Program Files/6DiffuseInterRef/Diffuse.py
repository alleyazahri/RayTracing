'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image 
from sphereEdit2 import Sphere
from multiprocessing import Pool
import random

width = 550
height = 550
image = Image.new('RGB',(width,height))
start = 2

def splitWork():
    pixels =[]
    p = Pool(4)
    for n in range(18):
        for i in range(width):
            for j in range(height):
                pixels.append((i,j,n))
        color = p.map(something,pixels)
        for i in range(len(pixels)):
            image.putpixel((pixels[i][0],pixels[i][1]),color[i])
        imgName = str(n+start) + "rainbowDarkp3noFuzz.jpg"
        print imgName
        image.save(imgName,"JPEG")
    
def something(param):
    n = param[2]
    n=n+start
    yDic={}  # s1  s2  s3  s5        R       O     `  Y       G       B       I       V
    yDic[0] = [-.4,.75,-.1,1,       -3,     20,     20,     20,     20,     20,     20]
    yDic[1] = [-0.9,0.3,.65,1.5,    -2.5,   20,     20,     20,     20,     20,     20]
    yDic[2] = [-.45,-.45,1.3,2,     -2,     -3,     20,     20,     20,     20,     20]
    yDic[3] = [0,-1,.95,2.5,        -1.5,   -2.5,   20,     20,     20,     20,     20]
    yDic[4] = [.45,-.45,.6,3,       -1,     -2,     -3,     20,     20,     20,     20]
    yDic[5] = [0.9,0,0.5,3.5,       -.5,    -1.5,   -2.5,   20,     20,     20,     20]
    yDic[6] = [.6,.55,-.1,20,       0,      -1,     -2,     -3,     20,     20,     20]
    yDic[7] = [.3,1.1,-.8,20,       .5,     -.5,    -1.5,   -2.5,   20,     20,     20]
    yDic[8] = [-.2,.85,-.45,20,     1,      0,      -1,     -2,     -3,     20,     20]
    yDic[9] = [-.8,0.6,0.1,20,      1.5,    .5,     -.5,    -1.5,   -2.5,   20,     20]
    yDic[10] = [-.35,-.15,.55,20,   2,      1,      0,      -1,     -2,     -3,     20]
    yDic[11] = [0.1,-0.95,1.2,20,   2.5,    1.5,    .5,     -.5,    -1.5,   -2.5,   20]
    yDic[12] = [.5,-.45,.85,20,     3,      2,      1,      0,      -1,     -2,     -3]
    yDic[13] = [0.9,0.0,0.5,20,     20,     2.5,    1.5,    .5,     -.5,    -1.5,   -2.5]
    yDic[14] = [.5,.6,-.25,20,      20,     3,      2,      1,      0,      -1,     -2]
    yDic[15] = [0.1,1.2,-0.85,20,   20,     20,     2.5,    1.5,    .5,     -.5,    -1.5]
    yDic[16] = [-.4,.75,-.35,20,    20,     20,     3,      2,      1,      0,      -1]
    yDic[17] = [-0.9,0.3,0.1,20,    20,     20,     20,     2.5,    1.5,    .5,     -.5]
    yDic[18] = [-.45,-.45,.65,20,   20,     20,     20,     3,      2,      1,      0]
    yDic[19] = [0,-1,1.2,20,        20,     20,     20,     20,     2.5,    1.5,    .5]
    yDic[20] = [-.4,.75,-.1,1,      20,     20,     20,     20,     3,      2,      1]
    yDic[21] = [-0.9,0.3,.65,1.5,   20,     20,     20,     20,     20,     2.5,    1.5]
    yDic[22] = [-.45,-.45,1.3,2,    20,     20,     20,     20,     20,     3,      2]
    yDic[23] = [0,-1,.95,2.5,       20,     20,     20,     20,     20,     20,     2.5]
    yDic[24] = [.45,-.45,.6,3,      20,     20,     20,     20,     20,     20,     3]
    yDic[25] = [0.9,0,0.5,3.5,      20,     20,     20,     20,     20,     20,     20]

    coords = yDic[n]

    '''Spheres! They are ordered such that in the first position
    they hold the radius, second is the center, and third is the color'''
    s3 = Sphere(1, (-2,coords[2],-3), (1,1,1),"mirror")  # Left Sphere
    s1 = Sphere(1, (0,coords[0],-3), (1,1,1),"mirror")  # Center Sphere
    s2 = Sphere(1, (2,coords[1],-4), (0.5,1.0,.5))  # Right Sphere
    s4 = Sphere(98.5, (0,-100,0), (1.0,1.0,1.0))  # Bottom Sphere
    s5 = Sphere(.4,(coords[3],-1.1,-2),(0.0,1.0,1.0))

    red = Sphere(.4,(coords[4],-1.1,-2),(1.0,0,0))
    orange = Sphere(.4,(coords[5],-1.1,-2),(1.0,0.6,0))
    yellow =Sphere(.4,(coords[6],-1.1,-2),(1.0,1.0,0.0))
    green = Sphere(.4,(coords[7],-1.1,-2),(0.0,1.0,0.0))
    blue = Sphere(.4,(coords[8],-1.1,-2),(0.0,0.0,1.0))
    indigo = Sphere(.4,(coords[9],-1.1,-2),(0.44,0.0,1.0))
    violet = Sphere(.4,(coords[10],-1.1,-2),(0.93,.5,0.93))


    light = Sphere(1,(0,10,0),(1.0,1.0,1.0),"light")
    l2 = Sphere(1,(5,10,5),(1.0,1.0,1.0),"light")
    l3 = Sphere(1,(10,10,10),(1.0,1.0,1.0),"light")

    # if param[3] <.25:
    #     which = param[4]
    #     if which == 0:
    #         red = Sphere(.4,(coords[4],-.9,-2),(1.0,0,0))
    #     if which == 1:
    #         orange = Sphere(.4,(coords[5],-.9,-2),(1.0,0.6,0))
    #     if which == 2:
    #         yellow =Sphere(.4,(coords[6],-.9,-2),(1.0,1.0,0.0))
    #     if which == 3:
    #         green = Sphere(.4,(coords[7],-.9,-2),(0.0,1.0,0.0))
    #     if which == 4:
    #         blue = Sphere(.4,(coords[8],-.9,-2),(0.0,0.0,1.0))
    #     if which == 5:
    #         indigo = Sphere(.4,(coords[9],-.9,-2),(0.44,0.0,1.0))
    #     if which == 6:
    #         violet = Sphere(.4,(coords[10],-.9,-2),(0.93,.5,0.93))
    sArray = [s4,s3,s1,s2,s5,red,orange,yellow,green,blue,indigo,violet]
    lArray = [light]

    if n > 5:
        lArray = [light,l2]
        if n > 10 :
            lArray = [light,l2,l3]
    
    checkHit = None
    i = param[0]
    j = param[1]

    closeSphere = None
    poi = None
    if (i%(width/10) == 0 and j==i) or i==j==width-1:
        print i/(width*1.0)
    ray = Vec3D((-1+2*(i/(width-1.0))),(1.0-2.0*(j/(height-1.0))),-1.0)
    closest = float("inf")
    for sphere in sArray:
        checkHit = ray.sphereInt(sphere)
        if checkHit != None:
            if checkHit<closest:
                closeSphere = sphere
                closest = checkHit
                poi = ray.poi(checkHit)
                
    '''Background'''
    if closeSphere==None:
        return (0,int(256*((0.2*(1-ray.gety()))-0.0000001)),int(256*(0.1*0.0000001)))
    else:
        color = closeSphere.getColor(0,ray,poi,sArray,lArray)
        return (int(256*(color[0]-0.0000001)),int(256*(color[1]-0.0000001)),int(256*(color[2]-0.0000001)))

if __name__ == '__main__':
    splitWork()
