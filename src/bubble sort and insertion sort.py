# Python program for implementation of Bubble Sort
# Mukhamad Fatkhul Allam U
# 19102226
# MM 4

import numpy as np
from time import process_time

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
  
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


jumlah_data = int(input("masukkkan jumlah data : "));
arr = np.random.randint(0,10000,jumlah_data)
arr_1 = arr
arr_2 = arr
# Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]

start_time1 = process_time()
bubbleSort(arr_1)
end_time1 = process_time()

start_time2 = process_time()
insertionSort(arr_2)
end_time2 = process_time()

print("Sorted array bubble :")

print(arr_1)
print("\n Waktu Eksekusi : ", float(end_time1-start_time1),"second")

print("\n\n Sorted array insertion  :")

print(arr_2)
print("\n Waktu Eksekusi : ", float(end_time2-start_time2),"second")