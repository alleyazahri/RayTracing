'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image 
# from random import Random as rand

if __name__ == '__main__':
    width = 550
    height = 550
    
    '''Spheres! They are ordered such that in the first position
    they hold the radius, second is the center, and third is the color'''

    yDic ={}

    yDic[6] = [.45,-.45,.6]
    yDic[7] = [0.9,0,0.5]
    yDic[8] = [.6,.55,-.1]
    yDic[9] = [.3,1.1,-.8]
    yDic[10] = [-.2,.85,-.45]
    yDic[11] = [-.8,0.6,0.1]
    yDic[12] = [-.35,-.15,.55]
    yDic[13] = [0.1,-0.95,1.2]
    yDic[14] = [.5,-.45,.85]
    yDic[15] = [0.9,0.0,0.5]
    yDic[16] = [.5,.6,-.25]
    yDic[17] = [0.1,1.2,-0.85]
    yDic[18] = [-.4,.75,-.35]
    yDic[19] = [-0.9,0.3,0.1]
    yDic[20] = [-.45,-.45,.65]
    yDic[21] = [0,-1,1.2]



    shadowV = Vec3D(0,1,0)
    scale = 0.0
    for n in range(22):
        coords = yDic[n]
        s1 = (1,(0,coords[0],-3),(1.0,0.5,0.5)) #Red
        s2 = (1,(2,coords[1],-4),(0.5,1.0,0.5)) #Green
        s3 = (1,(-2,coords[2],-3),(0.5,0.5,1.0)) #Blue
        s4 = (98.5,(0,-100,0),(1.0,1.0,1.0)) #White
        sArray = [s1,s2,s3,s4]
        '''image stuffs'''
        image = Image.new('RGB',(width,height))
        image.putpixel((0,0),(255,255,255))

        '''actual creating of the image'''
        for i in range(width):
            for j in range(height):
                ray = Vec3D((-1+2*(i/(width-1.0))),(1.0-2.0*(j/(height-1.0))),-1.0)
                closest = float("inf")
                for sphere in sArray:
                    center = sphere[1]
                    radius = sphere[0]
                    color = sphere[2]
                    checkHit = ray.sphereInt(radius,center)
                    '''Background'''
                    if checkHit==None and closest == float("inf"):
                        image.putpixel((i,j),(0,int(256*((0.2*(1-ray.gety()))-0.0000001)),int(256*(0.1*0.0000001))))
                    else:
                        '''Checking Spheres'''
                        if checkHit != None:
                            if checkHit<closest:
                                poi = ray.poi(checkHit)
                                normal = ray.normU(poi,center)
                                if normal.gety()>0:
                                    r = color[0]*(normal.gety()+scale)
                                    g = color[1]*(normal.gety()+scale)
                                    b = color[2]*(normal.gety()+scale)
                                    if (normal.gety()+scale) > 1:
                                        r = color[0]
                                        g = color[1]
                                        b = color[2]
                                # Lower half of the spheres
                                else:
                                    r = scale*color[0]
                                    g = scale*color[1]
                                    b = scale*color[2]
                                image.putpixel((i,j),(int(256*(r-0.0000001)),int(256*(g-0.0000001)),int(256*(b-0.0000001))))
                                '''Shadow of Spheres'''
                                for s2 in sArray:
                                    if s2 != sphere:
                                        cent = s2[1]
                                        rad = s2[0]
                                        col = s2[2]
                                        shadow = shadowV.sphereInt(rad,cent,poi)
                                        if shadow != None:
                                            r =scale*color[0]
                                            g = scale*color[1]
                                            b = scale*color[2]
                                            image.putpixel((i,j),(int(256*(r-0.0000001)),int(256*(g-0.0000001)),int(256*(b-0.0000001))))
                                closest = checkHit
                                if closest == None:
                                    print "None!"
        imgName = str(n) + "dark.jpg"
        print imgName, " Done!"
        image.save(imgName,"JPEG")

