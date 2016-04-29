'''
Created on Jan 29, 2015

@author: Alley
'''
from vec3d import Vec3D
from PIL import Image 
from sphere import Sphere
from multiprocessing import Pool

width = 300
height = 300
image = Image.new('RGB',(width,height))

def splitWork():
    pixels =[]
    p = Pool(4)
    for i in range(width):
        for j in range(height):
            pixels.append((i,j))
    color = p.map(something,pixels)
    for i in range(len(pixels)):
        image.putpixel(pixels[i],color[i])
    image.save("FinalPics.jpg","JPEG")
    
def something(param):
    '''Spheres! They are ordered such that in the first position
    they hold the radius, second is the center, and third is the color'''
    s3 = Sphere(1, (-2,0,-3), (1.0,0.1,0.1))  # Left Sphere
    s1 = Sphere(1, (0,0,-3), (.1,1.0,1.0),"sparkle")  # Center Sphere
    s2 = Sphere(1, (2,0,-4), (0.0,1.0,0.1),None,8)  # Right Sphere
    s4 = Sphere(98.5, (0,-100,0), (1.0,1.0,1.0))  # Bottom Sphere
    s5 = Sphere(0.5, (-1,1.2,-2.8), (1,1,1), "mirror")
    s6 = Sphere(0.5, (1,1.2,-2.8), (0.0,1.0,1.0), "mirror")

    light = Sphere(1,(0,10,0),(1.0,1.0,1.0),"light")
    l2 = Sphere(1,(5,10,5),(1.0,1.0,1.0),"light")
    l3 = Sphere(1,(10,10,10),(1.0,1.0,1.0),"light")
    sArray = [s4,s3,s1,s2,s5,s6]
    lArray = [l3,l2,light]
    '''image stuffs'''
    
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
