class ArrayStack(object):
	"""docstring for ArrayStack"""
	def __init__(self, order="FILO", **args):
		super(ArrayStack, self).__init__(**args)
		self.stack = []
		self.type = order

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		if(self.type == 'FILO' || self.type == 'LIFO'):
			self.stack.pop(-1)
		else:
			self.stack.pop(0)