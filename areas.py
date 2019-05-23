class Circle: #  compute the area of a circle
	
	pi = 3.14159 #  class variable

	def __init__(self, radius):
		self.r = radius
	
	def area(self):
		return self.pi*self.r**2

	def circumference(self):
		return 2*self.pi*self.r


class Rectangle: 

	def __init__(self, length, width):
		self.l = length
		self.w = width

	def area(self):
		return self.l*self.w


r = float(input("please enter radius: "))
c = Circle(r)
print("Area of circle: ", c.area())
print("Circumference: ", c.circumference())

l = float(input("please enter length: "))
w = float(input("please enter width: "))
a = Rectangle(l,w)
print("Area of rectangle: ", a.area())
