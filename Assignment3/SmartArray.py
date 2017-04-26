class SmartArray(object):
	"""docstring for SmartArray"""
	def __init__(self, **kwargs):
		super(SmartArray, self).__init__(**kwargs)
		self.array = []

	def append(self, value):
		self.array.append(value)
	
	def pop(self, pos):
		self.array.pop(pos)

	def insert(self, pos, value):
		if(pos > (len(self.array)-1)):
			self.append(value)
		else:
			i = self.array[:pos]
			j = self.array[pos:]
			i.append(value)
			for k in j:
				i.append(k)
			self.array = i

	def __str__(self):
		return str(self.array)