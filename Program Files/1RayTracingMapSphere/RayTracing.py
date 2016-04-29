'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image
import random

if __name__ == '__main__':
    width = 550
    height = 550
    # radius = 1.9
    s2xChange = -0.1
    s2zChange = 0.05
    s3xChange = 0.1
    s4radChange = -4.875
    # Original Location: radius 1 center (0,0,-3)
    # s1 = [1,(0,0,-3),(1.0,0.5,0.5)]
    # s2 = [1,(2,0,-4),(0.5,1.0,0.5)]
    # s3 = [1,(-2,0,-3),(0.5,0.5,1.0)]
    # s4 = [98.5,(0,100,0),(1.0,1.0,1.0)] #White
    s1 = [1, (0, 0, -3), (1, 0, 0)]
    s2 = [1, (1.0999999999999992, 0, -3.5500000000000016), (0, 1, 0)]
    s3 = [1, (-1.0999999999999992, 0, -3), (0, 0, 1)]
    s4 = [54.625, (0, 100, 0), (1, 1, 1)]
    sArray = [s1,s2,s3,s4]
    cconstant = 0.3

    for n in range(10):
        '''image stuffs'''
        image = Image.new('RGB',(width,height))
        image.putpixel((0,0),(255,255,255))
        s1randx = random.random()
        s1randy = random.random()
        if s1randx > 0.66666:
            s1randx = 0.08
        elif s1randx < 0.33333:
            s1randx = -0.08
        else:
            s1randx = 0.0
        if s1randy > 0.66666:
            s1randy = 0.08
        elif s1randy < 0.33333:
            s1randy = -0.08
        else:
            s1randy = 0.0

        s2randx = random.random()
        s2randy = random.random()
        if s2randx > 0.66666:
            s2randx = 0.08
        elif s2randx < 0.33333:
            s2randx = -0.08
        else:
            s2randx = 0.0
        if s2randy > 0.66666:
            s2randy = 0.08
        elif s2randy < 0.33333:
            s2randy = -0.08
        else:
            s2randy = 0.0

        s3randx = random.random()
        s3randy = random.random()
        if s3randx > 0.66666:
            s3randx = 0.08
        elif s3randx < 0.33333:
            s3randx = -0.08
        else:
            s3randx = 0.0
        if s3randy > 0.66666:
            s3randy = 0.08
        elif s3randy < 0.33333:
            s3randy = -0.08
        else:
            s3randy = 0.0

        s4randx = random.random()
        s4randy = random.random()
        if s4randx > 0.66666:
            s4randx = 0.08
        elif s4randx < 0.33333:
            s4randx = -0.08
        else:
            s4randx = 0.0
        if s4randy > 0.66666:
            s4randy = 0.08
        elif s4randy < 0.33333:
            s4randy = -0.08
        else:
            s4randy = 0.0

        s1 = [s1[0],(s1[1][0]+s1randx,s1[1][1]+s1randy,s1[1][2]),(1,0,0)]
        s2 = [s2[0],(s2[1][0]+s2randx,s2[1][1]+s2randy,s2[1][2]),(0,1,0)]
        s3 = [s3[0],(s3[1][0]+s3randx,s3[1][1]+s3randy,s3[1][2]),(0,0,1)]
        s4 = [s4[0],(s4[1][0]+s4randx,s4[1][1]+s4randy,s4[1][2]),(1,1,1)]
        sArray = [s1,s2,s3,s4]


        '''actual creating of the image'''
        for i in range(width):
            for j in range(height):
                ray = Vec3D((-1+2*(i/(width-1.0))),(-1.0+2.0*(j/(height-1.0))),-1.0)
                closest = float("inf")
                for sphere in sArray:
                    checkHit = ray.sphereInt(sphere[0],sphere[1])
                    if checkHit != None and checkHit<closest:
                            closest = checkHit
                            color = sphere[2]
                if closest==float("inf"):
                    image.putpixel((i,j),(0,int(256*((0.2*(1+ray.gety()))-0.0000001)),int(256*(0.1*0.0000001))))
                else:
                    nx = ray.getx()*closest
                    ny = ray.gety()*closest
                    nz = ray.getz()*closest+3  # add three here to off-center the sphere
                    normal = Vec3D(nx,ny,nz)
                    normal = normal.unitV()
                    image.putpixel((i,j),(int(256*((color[0]*cconstant+(((normal.getx()+1)/2)-0.0000001))/(cconstant+1))),
                                          int(256*((color[1]*cconstant+(((normal.gety()+1)/2)-0.0000001))/(cconstant+1))),
                                          int(256*((color[2]*cconstant+(((normal.getz()+1)/2)-0.0000001))/(cconstant+1)))))
        imgName = str(n) + "Offp2ChangeColor.jpg"
        image.save(imgName,"JPEG")
        s1 = [s1[0],(s1[1][0]-s1randx,s1[1][1]-s1randy,s1[1][2]),(1,0,0)]
        s2Cent = s2[1]
        s2 = [s2[0], (s2Cent[0]-s2xChange-s2randx,s2Cent[1]-s2randy,s2Cent[2]-s2zChange),(0,1,0)]
        s3 = [s3[0],(s3[1][0]-s3xChange-s3randx,s3[1][1]-s3randy,s3[1][2]),(0,0,1)]
        if n>12:
            s4radChange = -6
        # print s4[0]
        print sArray
        if s4[0] <= 5.5:
            s4radChange = -2.5
        if s4[0] <=3.5:
            s4radChange /= 2.1
        s4 = [s4[0]-s4radChange,(s4[1][0]-s4randx,s4[1][1]-s4randy,s4[1][2]),(1,1,1)]

        cconstant += 0.3
        sArray = [s1,s2,s3,s4]
        print n, " Done"