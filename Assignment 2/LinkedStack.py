from LinkedList import LinkedList

class LinkedStack(object):
	"""docstring for LinkedStack"""
	def __init__(self, order="FILO", **kwargs):
		super(LinkedStack, self).__init__()
		self.arg = arg
		self.stack = LinkedList()

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		if(self.type == 'FILO' || self.type == 'LIFO'):
			self.stack.pop(-1)
		else:
			self.stack.pop(0)