'''
Created on Feb 26, 2015

@author: Alley
'''

from vec3d import Vec3D

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
        
    '''Returns the radius of a sphere object'''   
    def getRad(self):
        return self.radius
    
    '''Returns the center of a sphere object'''
    def getCent(self):
        return self.center
    
    '''Returns the color of a sphere object'''
    def getColor(self, iterations, ray, poi=None, sphereSet=None):
#         sColor = Vec3D(self.color[0],self.color[1],self.color[2])
        normal = ray.normU(poi,self.center)
        if iterations > 10:
            return (1,1,1)
        elif self.classification == None:
            shadowV = Vec3D(0,1,0)
            color = None
            for subS in sphereSet:
                if subS != self:
                    if not subS.isLight():
                        shadow = shadowV.sphereInt(subS,poi)
                        if shadow != None:
                            color = (0,0,0)
            if color == None:
                color = (self.color[0]*normal.gety(),self.color[1]*normal.gety(),self.color[2]*normal.gety())
            return color
        elif self.classification == "mirror":
            reflect = normal.multiply(2*ray.dot(normal))
            reflect = ray.subtract(reflect)
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
                            color = other.getColor(iterations+1,reflect,newPOI,sphereSet)
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
        
        