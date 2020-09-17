'''
CMPSC465
Assignment2 Problem1
Authors: Jillian Haffner, Rachael Owens, Kevin O'Connor
Sept. 20, 2020
'''

import sys


def merge_two_sorted_arrays(arr1, arr2):
	# create array for final array
	final_arr = []

	# calculate len of the final array
	sz1 = len(arr1)
	sz2 = len(arr2)
	final_sz = sz1 + sz2

	p1 = arr1[0]
	p2 = arr2[0]
	j1 = 0
	j2 = 0
	gthan = 0		# counts how many numbers satisfy: i < j & A[i] > A[j]

	# merge and sort the two input arrays
	for i in range(0, final_sz):
		# sanity check: if arr1 is fully used, appends only from arr2
		if (j1 >= sz1):
			# sanity check: arr2
			if (j2 <= sz2):
				final_arr.append(arr2[j2])
				j2 += 1
		# sanity check: if arr2 is fully used, appends only from arr1
		elif (j2 >= sz2):
			final_arr.append(arr1[j1])
			j1 += 1
		# append arr1 value if less than arr2 value
		elif (int(arr1[j1]) < int(arr2[j2])):
			final_arr.append(arr1[j1])
			j1 += 1
		# append both arr1 and arr2 values if equal
		elif int(arr1[j1]) == int(arr2[j2]):
			final_arr.append(arr1[j1])
			j1 += 1
			final_arr.append(arr2[j2])
			j2 += 1
			i += 1
		# append arr2 value if less than arr1 value
		else:
			final_arr.append(arr2[j2])
			j2 += 1
	return final_arr


# takes an array and the len of the array as parameters to print the array
def print_array(arr):
	for k in range(0, len(arr) - 1):
		print(arr[k], end = " ")
	print(arr[len(arr) - 1], end = "")
	return

def main():
	# parse the two lines of input into len and array
	n = input()
	line2 = input()
	arr = line2.split()
	if int(n) < 2:
		print_array(arr)
		return
	else:
		arr = merge_sort(arr)
		print_array(arr)
		return


def merge_sort(arr):
	if len(arr) < 2:
		return arr
	mid = len(arr) // 2
	left = merge_sort(arr[: mid])
	right = merge_sort(arr[mid :])
	return merge_two_sorted_arrays(left, right)


main()





def main():
	n = input()
	arr = input().split()
	array_indices = []
	# find smallest # in array
	# resort array 
	# 

	for i in range(0, n):				# runs in O(n)
		# call check_num(n, arr, 0, 1)


def check_num(n, arr, i, j):			# run in O(logn)
	'''
	if n <= 1: return (0)
	else if arr[i]>arr[j]: 
		x
	'''