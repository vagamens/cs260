#!/bin/env python3

import random
from marble import Marble

class MarbleBag:

	def __init__(self, numMarbles=10, color="brown"):
		self.marbles = [None]*numMarbles
		self.color = color

	def addMarble(self, marble):
		for i in range(self.getNumMarbles()):
			if self.marbles[i] == None:
				self.marbles[i] = marble
				return
		self.marbles.append(marble)

	def emptyBag(self):
		self.marbles = []

	def getMarble(self, num):
		return self.marbles[num]

	def getMarbles(self):
		return self.marbles

	def getRandomMarble(self):
		return self.getMarble(random.randInt())

	def randomFillBag(self):
		colors = ["red", "green", "blue"]
		for i in range(len(self.marbles)):
			self.marbles[i] = Marble(color=colors[random.randint(0,len(colors)-1)], size=random.randint(1,10))

	def getNumMarbles(self):
		return len(self.marbles)

	def setColor(self, color="brown"):
		self.color = color

	def getColor(self):
		return self.color

	def __str__(self):
		output = "This bag is " + self.color
		output = output + " and has " + str(len(self.marbles)) + " marbles."
		output = output + "\n"
		return 