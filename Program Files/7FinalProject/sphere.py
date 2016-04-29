'''
Created on Feb 26, 2015

@author: Alley
'''

from vec3d import Vec3D
import random


class Sphere:

    # Constructor
    def __init__(self, r, c, col, clas = None, dif = 12):
        self.radius = r
        self.center = c
        self.color = col
        self.reflect = dif
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
    
    '''Returns a random ray given an original point (poi) and a random point in the given sphere'''
    def randRay(self,sphere,poi=(0,0,0)):
        # 'create' a cube whose diagonal corners are at (0,0,0) and (radius,radius,radius)
        radius = sphere.getRad()
        r = radius/2
        while True: 
            x = random.random()*radius  #random x, y,and z the cube
            y = random.random()*radius
            z = random.random()*radius
            if ((r-x)*(r-x)+(r-y)*(r-y)+(r-z)*(r-z))<=(radius*radius):  #checks if that random point is also in the sphere
                break
        direction = sphere.getCent()
        direction = (direction[0]-r,direction[1]-r,direction[2]-r)
        
        return Vec3D((direction[0]+x)-poi[0],(direction[1]+y)-poi[1],(direction[2]+z)-poi[2])
        
    '''Returns the shadow color at a given pixel'''
    def getShadow(self, iterations, ray, poi, sphereSet, lightSet, origCol = None):
        if iterations > 1:
            return origCol
        else:
            color = 0.0
            count = 0
            shade = 0.0
            normal = ray.normU(poi,self.center)
            direction = None
            for sphere in sphereSet:
                for light in lightSet:
                    direction = self.randRay(light,poi)
                    direction = direction.unitV()
                    shadow = direction.sphereInt(sphere,poi,True)
                    count +=1
                    if shadow is None:
                        shade = 1.0
                    else:
                        shade = 0.0
                    color += normal.dot(direction)*shade
            color /= count
        if origCol is None:
            return self.getShadow(iterations+1,ray,poi,sphereSet,lightSet,(color,color,color))
        else:
            return self.getShadow(iterations+1,ray,poi,sphereSet,lightSet,((origCol[0]+color)/2,(origCol[1]+color)/2,(origCol[2]+color)/2))

    '''Returns the color of a random ray for diffuse spheres'''
    def getSparkle(self,iterations,poi,sphereSet,lightSet,origCol=None):
        if iterations > 2:
            return origCol
        else:
            invSphere = Sphere(0.7,(poi[0]+0.5,poi[1]+.5,poi[2]+.5),(0.0,0.0,0.0))
            diffRay = self.randRay(invSphere,poi)
            closest = float("inf")
            color = None
            for sphere in sphereSet:
                if sphere != self:
                    checkHit = diffRay.sphereInt(sphere,poi)
                    if checkHit is None and closest == float("inf"):
                        color = (0,((0.2*(1-diffRay.gety()))-0.0000001),(0.1*0.0000001))
                    elif checkHit != None:
                        if checkHit < closest:
                            closest = checkHit
                            color = sphere.origCol()
            for l in lightSet:
                checkHit = diffRay.sphereInt(l,poi)
                if checkHit != None:
                    if checkHit < closest:
                        color = l.origCol()
            if origCol is not None:
                color = ((color[0]+origCol[0])/2, (color[1]+origCol[1])/2, (color[2]+origCol[2])/2)
            return self.getDiffuse(iterations+1,poi,sphereSet,lightSet,color)

    def getDiffuse(self,iterations,poi,sphereSet,lightSet,origCol=None):
        if iterations > 2:
            return origCol
        else:
            invSphere = Sphere(0.3,(poi[0]+0.5,poi[1]+.5,poi[2]+.5),(0.0,0.0,0.0))
            diffRay = self.randRay(invSphere,poi)
            closest = float("inf")
            color = None
            for sphere in sphereSet:
                if sphere != self:
                    checkHit = diffRay.sphereInt(sphere,poi)
                    if checkHit is None and closest == float("inf"):
                        color = None
                    elif checkHit != None:
                        if checkHit < closest:
                            closest = checkHit
                            color = sphere.origCol()
            for l in lightSet:
                checkHit = diffRay.sphereInt(l,poi)
                if checkHit != None:
                    if checkHit < closest:
                        color = l.origCol()
            if origCol is not None and color is not None:
                color = ((color[0]+origCol[0])/2, (color[1]+origCol[1])/2, (color[2]+origCol[2])/2)
            elif origCol is not None:
                color = origCol
            return self.getDiffuse(iterations+1,poi,sphereSet,lightSet,color)

    '''Returns the color of a sphere object'''
    def getColor(self, iterations, ray, poi,sphereSet,lightSet,origCol=None):
        normal = ray.normU(poi,self.center)
        originalCol = self.origCol()
        if iterations > 2:
            return origCol
        elif self.classification is None or self.classification == "sparkle":
            shadow = self.getShadow(0, ray, poi, sphereSet, lightSet, origCol)
            diffcol = self.getDiffuse(0,poi,sphereSet,lightSet, origCol)
            if self.classification == "sparkle":
                sparkleCol = self.getSparkle(0,poi,sphereSet,lightSet,origCol)
            else:
                sparkleCol = (1,1,1)
            if diffcol is None:
                diffcol = (1,1,1)
            color = (((shadow[0]*originalCol[0]*(self.reflect-1)+diffcol[0])/self.reflect)*sparkleCol[0],
                     ((shadow[1]*originalCol[1]*(self.reflect-1)+diffcol[1])/self.reflect)*sparkleCol[1],
                     ((shadow[2]*originalCol[2]*(self.reflect-1)+diffcol[2])/self.reflect)*sparkleCol[2])
            if color is None:
                color = (self.color[0]*normal.gety(),self.color[1]*normal.gety(),self.color[2]*normal.gety())
                if origCol is None:
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
                        color = (0,((0.2*(1-reflect.gety()))-0.0000001)*originalCol[1],(0.1*0.0000001)*originalCol[2])
                    elif checkHit != None:
                        if checkHit < closest:
                            closest = checkHit
                            newPOI = reflect.poi(checkHit,poi)
                            color = other.getColor(iterations+1,reflect,newPOI,sphereSet,lightSet)
                            color = (color[0]*originalCol[0],color[1]*originalCol[1],color[2]*originalCol[2])
            for l in lightSet:
                checkHit = reflect.sphereInt(l,poi)
                if checkHit != None:
                    if checkHit < closest:
                        color = originalCol
            return color
        else:
            # Assumes sphere is a light sphere
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