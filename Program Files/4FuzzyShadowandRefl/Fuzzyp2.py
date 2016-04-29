'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image 
from sphere import Sphere
# from random import Random as rand

if __name__ == '__main__':
    width = 1000
    height = 1000
    
    '''Spheres! They are ordered such that in the first position
    they hold the radius, second is the center, and third is the color'''
    s1 = Sphere(1,(0,0,-3),(0.0,1.0,1.0),"mirror") #Red - will be mirror!
    s2 = Sphere(1,(2,0,-4),(0.0,1.0,0.1)) #Green
    s3 = Sphere(1,(-2,0,-3),(0.0,0.1,1.0)) #Blue
    s4 = Sphere(98.5,(0,-100,0),(1.0,1.0,1.0)) #White
    s5 = Sphere(.2,(-1.8,0,-2),(1.0,0.5,0.5))
    light = Sphere(1,(0,10,0),(1.0,1.0,1.0),"light")
    l2 = Sphere(1,(5,10,5),(1.0,1.0,1.0),"light")
    sArray = [s4,s3,s1,s2]
    lArray = [light,l2]
    '''image stuffs'''
    image = Image.new('RGB',(width,height))
    image.putpixel((0,0),(255,255,255))

    '''actual creating of the image'''
    for i in range(width):
        for j in range(height):
            if (i%(width/10) == 0 and j==i) or i==j==width-1:
                print i/(width*1.0)
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
                            color = sphere.getColor(0,ray,poi,sArray,lArray)
                            origColor = sphere.origCol()
                            color = (color[0]*origColor[0],color[1]*origColor[1],color[2]*origColor[2])
                            image.putpixel((i,j),(int(256*(color[0]-0.0000001)),int(256*(color[1]-0.0000001)),int(256*(color[2]-0.0000001))))
                            closest = checkHit
                    
    image.save("Comparejpeg.jpg","JPEG")

            