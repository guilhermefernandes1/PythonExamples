class Square:
	""" Class to implement an example
	of OO. Calculates the area and the
	perimeter."""

	def __init__(self,height):
		self.height = height

	def area(self):
		""" Returns the area of the Square """
		return self.height * self.height

	def perimeter(self):
		""" Returns the perimeter of the Square """
		return self.height * 4