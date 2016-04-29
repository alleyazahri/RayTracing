'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image 
from sphere import Sphere
from multiprocessing import Pool

if __name__ == '__main__':
    # Spheres! They are ordered such that in the first position
    # they hold the radius, second is the center, third is the color, and fourth is 'classification'
    s1 = Sphere(1,(0,0,-3),(1.0,0.1,0.1),"mirror")  #Center Sphere
    s2 = Sphere(1,(2,0,-4),(0.0,1.0,0.1))  #Left Sphere
    s3 = Sphere(1,(-2,0,-3),(0.0,1.0,1.0))  #Right Sphere
    s4 = Sphere(98.5,(0,-100,0),(1.0,1.0,.5))  #Bottom Sphere

    light = Sphere(1,(0,10,0),(1.0,1.0,1.0),"light")
    l2 = Sphere(1,(5,10,5),(1.0,1.0,1.0),"light")
    l3 = Sphere(1,(10,10,10),(1.0,1.0,1.0),"light")
    sArray = [s4,s3,s1,s2]
    lArray = [l3,l2,light]

    # Image Stuffs
    width = 250
    height = 250
    image = Image.new('RGB',(width,height))

    for i in range(width):
        for j in range(height):
            checkHit = None
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
                image.putpixel((i,j),(0,int(256*((0.2*(1-ray.gety()))-0.0000001)),int(256*(0.1*0.0000001))))
            else:
                color = closeSphere.getColor(0,ray,poi,sArray,lArray)
                origColor = closeSphere.origCol()
                color = (color[0]*origColor[0],color[1]*origColor[1],color[2]*origColor[2])
                image.putpixel((i,j),(int(256*(color[0]-0.0000001)),int(256*(color[1]-0.0000001)),int(256*(color[2]-0.0000001))))
    image.save("FuzzyEverywhere.jpg","JPEG")