import sys
sys.path.insert(0, '../Assignment2')

from LinkedList import LinkedList
from Node import Node

class SortedList(LinkedList):
	"""docstring for SortedList"""
	def __init__(self, **args):
		super(SortedList, self).__init__(**args)
		self.arg = arg
	
	def insert(value):
		node = Node(None, None, value)
		if(self.head.adjacent == self.tail):
			node.setPrevious(self.head)
			node.setAdjacent(self.tail)
			self.head.setAdjacent(node)
			self.tail.setPrevious(node)
		else:
			curNode = Node(None, False, None)
			while(curNode.adjacent != None):
				if(curNode.value >= node.value):
					node.setPrevious(curNode.previous)
					curNode.setPrevious(node)
					node.previous.setAdjacent(node)
					node.setAdjacent(curNode)
				else:
					curNode = curNode.previous