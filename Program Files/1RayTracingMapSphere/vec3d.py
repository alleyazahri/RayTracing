'''
Created on Jan 29, 2015

@author: Alley
'''
import math

class Vec3D(object):
    
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
    
    '''Returns the cross product of two vectors'''
    def cross(self,other):
        return Vec3D((self.y*other.getz()-self.z*other.gety()),(self.z*other.getx()-self.x*other.getz()),(self.x*other.gety()-self.y*other.getx()))
    
    '''subtracts two vectors'''
    def subtract(self,other):
        return Vec3D(self.x-other.getx(),self.y-other.gety(),self.z-other.getz())
    
    '''adds two vectors'''
    def add(self,other):
        return Vec3D(self.x+other.getx(),self.y+other.gety(),self.z+other.getz())
    
    '''returns the t value for an equation of a line containing the vector for where it intersects the sphere,
    returns None if it doesn't intersect with the given sphere
    sorigin is the origin of the sphere, will assume 0,0,0 if left empty
    lorigin is the origin of hte line you wish to be created from the given vector, if left empty it will assume 0,0,0 as the origin of the line'''
    def sphereInt(self,radius,sorigin=(0,0,0),lorigin=(0,0,0)):
        lO = Vec3D(lorigin[0],lorigin[1],lorigin[2])
        sO = Vec3D(sorigin[0],sorigin[1],sorigin[2])
        diff = lO.subtract(sO)
        
        tsquared = self.lengthSquared()
        
        t = 2*self.dot(diff)
#         
        c = diff.lengthSquared()-(radius*radius)

        square = (t*t)-(4*tsquared*c)
        if square<=0 or tsquared == 0:
            return None
        else:
            tone = ((-t)+math.sqrt(square))/(2*tsquared)
            ttwo = ((-t)-math.sqrt(square))/(2*tsquared)
            if tone<ttwo:
                if tone>0:
                    return tone
                elif ttwo>0:
                    return ttwo
            else:
                if ttwo>0:
                    return ttwo
                elif tone>0:
                    return tone
            return None
        
    
# if __name__ == '__main__':
#     x = Vec3D(2,0,0)
#     print x.length()
#        
    
    
        