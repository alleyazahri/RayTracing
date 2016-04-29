'''
Created on Feb 26, 2015

@author: Alley
'''

from vec3d import Vec3D
import random

class Sphere:
    
    '''useless method that allows me to use the Vec3D class'''
#     def nothing(self):
#         n = Vec3D(1,2,3)
#         return n
#     
    '''Constructor'''
    def __init__(self, r, c, col, clas = None): 
        self.radius = r
        self.center = c
        self.color = col
        self.classification = clas
        
    '''Returns the original assigned color of the sphere'''
    def origCol(self):
        return self.color
        
    '''Returns the radius of a sphere object'''   
    def getRad(self):
        return self.radius
    
    '''Returns the center of a sphere object'''
    def getCent(self):
        return self.center
    
    def randRay(self,sphere,poi=(0,0,0)):
        #'create' a cube whose diagonal corners are at (0,0,0) and (radius,radius,radius)
        radius = sphere.getRad()
        r = radius/2
        while True:
            x = random.random()*radius
            y = random.random()*radius
            z = random.random()*radius
            
            if ((r-x)*(r-x)+(r-y)*(r-y)+(r-z)*(r-z))<=(radius*radius):
                break
        direction = sphere.getCent()
        direction = (direction[0]-r,direction[1]-r,direction[2]-r)
        
        return Vec3D((direction[0]+x)-poi[0],(direction[1]+y)-poi[1],(direction[2]+z)-poi[2])
        
    '''Returns the shadow amount'''
    def getShadow(self,iterations,ray,poi,sphereSet,lightSet,origCol = None):
        normal = ray.normU(poi,self.center)
        if iterations > 1:
            return origCol
        elif self.classification == None:
            color = None
            for light in lightSet:
                randShadowRay = self.randRay(light,poi)
                for sphere in sphereSet:
                    if sphere != self:
                        shadow = randShadowRay.sphereInt(sphere, poi)
                        if shadow != None:
                            if origCol == None:
                                color = self.getShadow(iterations+1,ray,poi,sphereSet,lightSet,(0.0,0.0,0.0))
                            else:
                                color = self.getShadow(iterations+1,ray,poi,sphereSet,lightSet,((0.0+origCol[0])/2.0,
                                                                                                (0.0+origCol[1])/2.0,(0.0+origCol[2])/2.0))
            if color == None:
                if origCol == None:
                    color = self.getShadow(iterations+1,ray,poi,sphereSet,lightSet,(normal.gety(),normal.gety(),normal.gety()))
                else:
                    color = self.getShadow(iterations+1,ray,poi,sphereSet,lightSet,((origCol[0]+normal.gety())/2,(origCol[1]+normal.gety())/2,(origCol[2]+normal.gety())/2))
            return color
          
    '''Returns the color of a sphere object'''
    '''Returns the color of a sphere object'''
    def getColor(self, iterations, ray, poi,sphereSet,lightSet,origCol=None):
#         sColor = Vec3D(self.color[0],self.color[1],self.color[2])
        normal = ray.normU(poi,self.center)
        if iterations > 20:
            return (1,1,1)
        elif self.classification == None:
            color = self.getShadow(0, ray, poi, sphereSet, lightSet, origCol)

            if color == None:
                color = (self.color[0]*normal.gety(),self.color[1]*normal.gety(),self.color[2]*normal.gety())
                if origCol == None:
                    color = self.getColor(iterations+1,ray,poi,sphereSet,lightSet,(color[0],color[1],color[2]))
                else:
                    color = self.getColor(iterations+1,ray,poi,sphereSet,lightSet,
                                          ((origCol[0]+color[0])/2.0,(origCol[1]+color[1])/2,(origCol[2]+color[2])/2))
            return color
        elif self.classification == "mirror":
            reflect = normal.multiply(2*ray.dot(normal))
            reflect = ray.subtract(reflect)
            invSphere = Sphere(0.03,(poi[0]+reflect.getx(),poi[1]+reflect.gety(),poi[2]+reflect.getz()),(0.0,0.0,0.0))
            reflect = self.randRay(invSphere,poi)
            closest = float("inf")
            for other in sphereSet:
                if other != self:
                    checkHit = reflect.sphereInt(other,poi)
                    if checkHit == None and closest == float("inf"):
                        color = (0,((0.2*(1-reflect.gety()))-0.0000001),(0.1*0.0000001))
                    elif checkHit != None:
                        if checkHit < closest:
                            closest = checkHit
                            newPOI = reflect.poi(checkHit,poi)
                            color = other.getColor(iterations+1,reflect,newPOI,sphereSet,lightSet)
            for l in lightSet:
                checkHit = reflect.sphereInt(l,poi)
                if checkHit != None:
                    if checkHit < closest:
                        color = (1.0,1.0,1.0)
            return color
        else:
            #Assumes sphere is a light sphere
            return (1.0,1.0,1.0)
        
    '''Returns true if the sphere is designated as a 'mirror'''
    def isMirror(self):
        if self.classification == "mirror":
            return True
        else:
            return False
        
    '''Returns true the sphere is designated as a 'light'''
    def isLight(self):
        if self.classification == "light":
            return True
        else:
            return False
        
        