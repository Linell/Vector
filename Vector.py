"""
	Timothy Bonnette	
		University of Southern Mississippi
		Created - 4/9/12
	
	Edit Log: 4.9.12 @ 3:53PM
			- set up the base. Did initial testing.
			 @ 6:16PM
			- made a dot product, magnitude, and projection
			  functions. Results don't seem consistent though.
		  4.12.12 @ 5:49
			- implemented more operators. I may make a text file
			  to help keep track of everything.
			- worked on ensuring accurate results. Everything is 
			  in working order now. Every test I've ever tried 
			  has came back correctly.
			
"""
from math import *

# Base Idea taken from http://stackoverflow.com/questions/2401185/python-vector-class
def AutoFloatProperties(*props):
    '''metaclass'''
    class _AutoFloatProperties(type):
        # Inspired by autoprop (http://www.python.org/download/		releases/2.2.3/descrintro)
        def __init__(cls, name, bases, cdict):
            super(_AutoFloatProperties, cls).__init__(name, bases, cdict)
            for attr in props:
                def fget(self, _attr='_'+attr): return getattr(self, _attr)
                def fset(self, value, _attr='_'+attr): setattr(self, _attr, float(value))
                setattr(cls, attr, property(fget, fset))
    return _AutoFloatProperties

class Vector(object):
	"""
	Creates a vector/triple, having x, y and z coordinates as float values.
	"""
	__metaclass__ = AutoFloatProperties('x','y','z')
	def __init__(self, x=0, y=0, z=0):
		self.x, self.y, self.z = x, y, z # values converted to float via properties
	# The following definitions overload the operators to preform operations on the 
	# vectors
	def __add__(self, other):
		"""
		Operator +
		Adds the two vectors
		"""
		return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
		# Subtracts the two vectors
	def __sub__(self, other):
		"""
		Operator -
		Subtracts the two vectors
		"""
		return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
	def __invert__(self):
		"""
		Operator ~
		Returns the magnitude
		"""
		return (sqrt(self.x*self.x + self.y*self.y + self.z*self.z))
	def __mul__(self, other):
		"""
		Operator *
		The dot product of the two vectors
		"""
		return (self.x*other.x + self.y*other.y + self.z*other.z)
	def __pow__(self, other):
		"""
		Operator *
		The cross product of the two vectors
		"""
		return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)


#		Functions	
# Function takes two vectors (u,v) and returns the best approx
#	of u in the direction of v.
def proj(u,v):
	top = u*v
	bottom = ~v*~v
	mid = top/bottom
	return Vector(mid*v.x, mid*v.y, mid*v.z)
# Function takes two vectors (u,v) and returns the scalar projection
def comp(u,v):
	top = u*v
	bottom = ~v
	return top/bottom

# Function takes a single vector and returns a normalized vector
def norm(u):
	mag = ~u
	vector = Vector()
	vector.x = u.x/mag
	vector.y = u.y/mag
	if (u.z != 0):
		vector.z = u.z/mag
	return vector

if __name__ == '__main__':
	# Left here to facilitate easy testing.
	v1 = Vector(3,1)
	v2 = Vector(4,5,3)
	v3 = Vector(3,4,2)
	v4 = Vector(2,3,1)
	result = v1+v2+v3+v4
	print result.x, result.y, result.z
	print ~v1
	result = norm(v1)
	print result.x, result.y, result.z	
