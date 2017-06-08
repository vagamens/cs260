#!/bin/env python3

# Assignment 8:
# 	Implement mergesort, quicksort, or heapsort as a method abailable
#	for an unsorted list.

import sort, random, time

def main():
	# Create test array
	testArray = [random.randint(1,100) for _ in range(20)]
	# measure the elapsed time for the algorithm
	start = time.time()
	merged = sort.merge(testArray)
	end = time.time()
	# print merge sort results
	print "Merge Sort: completed in: "+str(end-start)+" seconds"
	print testArray
	print str(merged)+'\n'
	# measure the elapsed time for the quick sort algorithm
	start = time.time()
	quickly = sort.quick(testArray)
	end = time.time()
	# print quick sort results
	print "Quick Sort: completed in: "+str(end-start)+" seconds"
	print testArray
	print str(quickly)+'\n'
	start = time.time()
	heaped = sort.heap(testArray)
	end = time.time()
	# print merge sort results
	print "Heap Sort: completed in: "+str(end-start)+" seconds"
	print testArray
	print str(heaped)+'\n'

if __name__ == '__main__':
	main()