def sort(array):
	if len(array) <= 1:
		return array
	elif len(array) == 2 and array[0] == array[1]:
		return array
	left, right = split(array)
	left = sort(left)
	right = sort(right)
	return merge(left, right)

def split(array):
	pivot = (maximum(array) + minimum(array))/2
	left, right = [], []
	for i in array:
		if i<=pivot:
			left.append(i)
		else:
			right.append(i)
	return left, right

def merge(left, right):
	array = left
	for i in right:
		array.append(i)
	return array

def maximum(array):
	m = 0
	for i in array:
		if i > m:
			m = i
	return m

def minimum(array):
	m =array[0]
	for i in array:
		if i < m:
			m = i
	return m