'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image 
from sphere import Sphere
# from random import Random as rand

if __name__ == '__main__':
    width = 550
    height = 550

    yDic = {}
    yDic[0] = [.45,-.45,.6]
    yDic[1] = [0.9,0,0.5]
    yDic[2] = [.6,.55,-.1]
    yDic[3] = [.3,1.1,-.8]
    yDic[4] = [-.2,.85,-.45]
    yDic[5] = [-.8,0.6,0.1]
    yDic[6] = [-.35,-.15,.55]
    yDic[7] = [0.1,-0.95,1.2]
    yDic[8] = [.5,-.45,.85]
    yDic[9] = [0.9,0.0,0.5]
    yDic[10] = [.5,.6,-.25]
    yDic[11] = [0.1,1.2,-0.85]
    yDic[12] = [-.4,.75,.4]
    yDic[13] = [-0.9,0.3,1.5]
    yDic[14] = [.2,-.45,3.1]
    yDic[15] = [1,-1,4]     # Blue Disappears
    yDic[16] = [2.8,-.45,2.5]
    yDic[17] = [4,0,0.8]    # Red Disappears
    yDic[18] = [2.7,.55,0]
    yDic[19] = [1.1,1.1,-.8,-3.5]
    yDic[20] = [.55,.85,-.45,-3]
    yDic[21] = [0,0.6,0.1,-2.5]
    yDic[22] = [-.35,-.15,.55,-2]
    yDic[23] = [0.1,-0.95,1.2,-1.5]
    yDic[24] = [.5,-.45,.85,-1]
    yDic[25] = [0.9,0.0,0.5,-.5]
    yDic[26] = [.5,.6,-.25,0]
    yDic[27] = [0.1,1.2,-0.85,.5]
    yDic[28] = [-.4,.75,-.1,1,-3,20,20,20,20,20,20]
    yDic[29] = [-0.9,0.3,.65,1.5,-2.5,-3,20,20,20,20,20]
    yDic[30] = [-.45,-.45,1.3,2,-2,-2.5,-3,20,20,20,20]
    yDic[31] = [0,-1,.95,2.5,-1.5,-2,-2.5,-3,20,20,20]
    yDic[32] = [.45,-.45,.6,3,-1,-1.5,-2,-2.5,-3,20,20]
    yDic[33] = [0.9,0,0.5,3.5,-.5,-1,-1.5,-2,-2.5,-3,20]
    # yDic[34] = [.45,-.45,.6,20,0,-.5,-1,-1.5,-2,-2.5,-3]
    # yDic[35] = [0.9,0,0.5,20,.5,0,-.5,-1,-1.5,-2,-2.5]
    yDic[36] = [.6,.55,-.1,20,1,.5,0,-.5,-1,-1.5,-2]
    yDic[37] = [.3,1.1,-.8,20,1.5,1,.5,0,-.5,-1,-1.5]
    yDic[38] = [-.2,.85,-.45,20,2,1.5,1,.5,0,-.5,-1]
    yDic[39] = [-.8,0.6,0.1,20,2.5,2,1.5,1,.5,0,-.5]
    yDic[40] = [-.35,-.15,.55,20,3,2.5,2,1.5,1,.5,0]
    yDic[41] = [0.1,-0.95,1.2,20,20,3,2.5,2,1.5,1,.5]
    yDic[42] = [.5,-.45,.85,20,20,20,3,2.5,2,1.5,1]
    yDic[43] = [0.9,0.0,0.5,20,20,20,20,3,2.5,2,1.5]
    yDic[44] = [.5,.6,-.25,20,20,20,20,20,3,2.5,2]
    yDic[45] = [0.1,1.2,-0.85,20,20,20,20,20,20,3,2.5]
    yDic[46] = [-.4,.75,-.35,20,20,20,20,20,20,20,3]
    yDic[19] = [-0.9,0.3,0.1]
    yDic[20] = [-.45,-.45,.65]
    yDic[21] = [0,-1,1.2]

    shadowV = Vec3D(0,1,0)
    n = 41
    while n<47:
        coords = yDic[n]
        '''Spheres! They are ordered such that in the first position
        they hold the radius, second is the center, and third is the color'''
        s1 = Sphere(1,(0,coords[0],-3),(1.0,0.5,0.5)) #Red
        s2 = Sphere(1,(2,coords[1],-4),(0.5,1.0,0.5)) #Green
        s3 = Sphere(1,(-2,coords[2],-3),(0.5,.5,1.0)) #Blue
        s4 = Sphere(98.5,(0,-100,0),(1.0,1.0,1.0)) #White
        light = Sphere(1,(0,10,0),(1.0,1.0,1.0),"light")
        if n > 15:
            s3 = Sphere(1,(-2,coords[2],-3),(0.5,.5,1.0),"mirror") #Blue
            if n > 18:
                s1 = Sphere(1,(0,coords[0],-3),(1.0,0.5,0.5),"mirror") #Red
                s5 = Sphere(.4,(coords[3],-1.1,-2),(0.0,1.0,1.0))
                if n>27:
                    red = Sphere(.4,(coords[4],-1.1,-2),(1.0,0,0))
                    orange = Sphere(.4,(coords[5],-1.1,-2),(1.0,0.6,0))
                    yellow =Sphere(.4,(coords[6],-1.1,-2),(1.0,1.0,0.0))
                    green = Sphere(.4,(coords[7],-1.1,-2),(0.0,1.0,0.0))
                    blue = Sphere(.4,(coords[8],-1.1,-2),(0.0,0.0,1.0))
                    indigo = Sphere(.4,(coords[9],-1.1,-2),(0.44,0.0,1.0))
                    violet = Sphere(.4,(coords[10],-1.1,-2),(0.93,.5,0.93))

        sArray = [s4,s3,s1,s2,light]
        if n > 18:
            sArray.append(s5)
            if n>27:
                sArray.append(red)
                sArray.append(orange)
                sArray.append(yellow)
                sArray.append(green)
                sArray.append(blue)
                sArray.append(indigo)
                sArray.append(violet)



        '''image stuffs'''
        image = Image.new('RGB',(width,height))
        image.putpixel((0,0),(255,255,255))

        '''actual creating of the image'''
        for i in range(width):
            for j in range(height):
                # if (i%(width/10) == 0 and j==i) or i==j==width-1:
                #     print i/(width*1.0)
                ray = Vec3D((-1+2*(i/(width-1.0))),(1.0-2.0*(j/(height-1.0))),-1.0)
                closest = float("inf")
                for sphere in sArray:
                    checkHit = ray.sphereInt(sphere)

                    '''Background'''
                    if checkHit==None and closest == float("inf"):
                        image.putpixel((i,j),(0,int(256*((0.2*(1-ray.gety()))-0.0000001)),int(256*(0.1*0.0000001))))
                    else:
                        if checkHit != None:
                            if checkHit<closest:
                                poi = ray.poi(checkHit)
                                color = sphere.getColor(0,ray,poi,sArray)
                                image.putpixel((i,j),(int(256*(color[0]-0.0000001)),int(256*(color[1]-0.0000001)),int(256*(color[2]-0.0000001))))
                                closest = checkHit
        imgName = str(n) + "mirror.jpg"
        print imgName
        image.save(imgName,"JPEG")
        n+=1