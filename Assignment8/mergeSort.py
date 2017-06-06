def sort(array):
	if len(array) == 1:
		return array
	left, right = split(array)
	left = sort(left)
	right = sort(right)
	return merge(left, right)

def split(array):
	left, right = [], []
	middle = len(array)/2
	for i in range(len(array)):
		if i<middle:
			left.append(array[i])
		else:
			right.append(array[i])
	return (left, right)

def merge(array1, array2):
	array = []
	i, j = 0, 0
	while True:
		if i<len(array1) and j<len(array2):
			if array1[i]<=array2[j]:
				array.append(array1[i])
				i+=1
			else:
				array.append(array2[j])
				j+=1
		elif i>=len(array1) and j<len(array2):
			array.append(array2[j])
			j+=1
		elif j>=len(array2) and i<len(array1):
			array.append(array1[i])
			i+=1
		else:
			break
	return array