class Square:
	""" Class to implement an example
	of OO. Calculates the area and the
	perimeter."""

	def __init__(self,height):
		self.height = height

	def area(self):
		return self.height ^ 2

	def perimeter(self):
		return self.height * 4