#!/bin/env python3

class Marble:

	def __init__(self, color="red", size=5):
		self.color = color
		self.size = size

	def setColor(self, color="red"):
		self.color = color

	def setSize(self, size=5):
		self.size = size

	def getColor(self):
		return self.color

	def getSize(self):
		return self.size

	def __str__(self):
		output = "This marble is " + str(self.color) + " and is " + str(self.size) + "mm."
		return output