'''
Created on Jan 29, 2015

@author: Alley
'''
import math
# from sphere import Sphere

class Vec3D(object):
    
    
    '''Nothing thing - useless method that allows me to use the Sphere import...'''
#     def nothing(self):
#         s = Sphere(1,2,3)
#         return s
    
    '''Constructor'''
    def __init__(self, ex,why,zee): 
        self.x = ex
        self.y = why
        self.z = zee
        
    '''Set the values for x, y, and z'''
    def setx(self,ex):
        self.x = ex
    def sety(self,why):
        self.y=why
    def setz(self,zee):
        self.z=zee
    '''Returns the individual values for x, y, and z respectively'''
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getz(self):
        return self.z
    
    '''Returns a tuple with the values of x, y, and z'''
    def getCoor(self):
        return (self.x,self.y,self.z)
    
    '''Returns the dot product of the given vector, and the vector "other"'''
    def dot(self,other):
        return (self.x*other.getx())+(self.y*other.gety())+(self.z*other.getz())
    
    '''Length of a vector squared'''    
    def lengthSquared(self):
        return self.x*self.x+self.y*self.y+self.z*self.z
    
    '''length of a vector'''
    def length(self):
        return math.sqrt(self.lengthSquared())
    
    '''Returns a unit vector'''
    def unitV(self):
        l = self.length()
        ex = self.x/l
        why = self.y/l
        zee = self.z/l
        return Vec3D(ex,why,zee)
    
    '''Returns the unit normal vector that happens at the given intersect and sphere
    param: poi - the point of intersect of a line and sphere
    scenter - the center of the sphere'''   
    def normU(self,poi,scenter):
        normVec = Vec3D((poi[0]-scenter[0]),(poi[1]-scenter[1]),(poi[2]-scenter[2]))
        return normVec.unitV()
    
    '''Returns a copy of the original vector'''
    def copy(self):
        return Vec3D(self.x,self.y,self.z)
    
    '''Returns the cross product of two vectors'''
    def cross(self,other):
        return Vec3D((self.y*other.getz()-self.z*other.gety()),(self.z*other.getx()-self.x*other.getz()),(self.x*other.gety()-self.y*other.getx()))
    
    '''subtracts two vectors'''
    def subtract(self,other):
        return Vec3D(self.x-other.getx(),self.y-other.gety(),self.z-other.getz())
    
    '''adds two vectors'''
    def add(self,other):
        return Vec3D(self.x+other.getx(),self.y+other.gety(),self.z+other.getz())
    
    '''multiplies each element of the vector by a scalar value'''
    def multiply(self,scalar):
        return Vec3D(self.x*scalar,self.y*scalar,self.z*scalar)
    
    def poi(self,t,origin=(0,0,0)):
        x = origin[0]+t*self.getx()
        y = origin[1]+t*self.gety()
        z = origin[2]+t*self.getz()
        return (x,y,z)
    
    '''Returns the t value for an equation of a line containing self (vector) for where it intersects the given sphere,
    returns None if it doesn't intersect with the given sphere.
    
    lorigin is the origin of the line you wish to be created from the given vector, if left empty it will assume 0,0,0 as the origin of the line'''
    def sphereInt(self, sphere, lorigin=(0,0,0), twoRes=False):
        lO = Vec3D(lorigin[0],lorigin[1],lorigin[2])
        sorigin = sphere.getCent()
        sO = Vec3D(sorigin[0],sorigin[1],sorigin[2])
        diff = lO.subtract(sO)
        
        tsquared = self.lengthSquared()
        
        t = 2*self.dot(diff)
#         
        c = diff.lengthSquared()-(sphere.getRad()*sphere.getRad())

        square = (t*t)-(4*tsquared*c)  # t^2 + 4ac - the value that will be square rooted later
        if square < 0:
            return None
        else:
            # Find the smallest positive t-value.
            tone = ((-t)+math.sqrt(square))/(2*tsquared)
            ttwo = ((-t)-math.sqrt(square))/(2*tsquared)
            if tone<ttwo:
                if tone>0:
                    if twoRes:
                        return (tone,ttwo)
                    return tone
                elif ttwo>0:
                    if twoRes:
                        return (ttwo,tone)
                    return ttwo
            else:
                if ttwo>0:
                    if twoRes:
                        return(ttwo,tone)
                    return ttwo
                elif tone>0:
                    if twoRes:
                        return (tone,ttwo)
                    return tone
            if twoRes:
                if tone > -0.0000001 or ttwo > -0.0000001:
                    return (tone,ttwo)
            return None