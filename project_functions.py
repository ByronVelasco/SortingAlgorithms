from math import inf


def bubble_sort(A):
	n = len(A)
	for i in range(n):  # Outer loop to iterate through the entire list
		# The last i elements are already sorted in each iteration
		for j in range(0, n - i - 1):  # Inner loop to compare adjacent elements
			if A[j] > A[j + 1]:  # If the current element is greater than the next
				A[j], A[j + 1] = A[j + 1], A[j]  # Swap the elements
				

def insertion_sort(A):
	n = len(A)  # Get the length of the array
	for i in range(1, n):  # Iterate from the second element to the end
		key = A[i]         # Store the current element to be positioned
		j = i - 1          # Start comparing with the previous element
		# Shift elements of A[0..i-1], that are greater than key, to one position ahead
		while j >= 0 and key < A[j]:
			A[j + 1] = A[j]  # Move element one position to the right
			j -= 1           # Move to the previous element
		A[j + 1] = key       # Place the key after the last shifted element
		

def selection_sort(A):
	n = len(A)  # Get the length of the list
	for i in range(n - 1):  # Iterate over each position in the list except the last
		min = i  # Assume the current position holds the minimum value
		for j in range(i + 1, n):  # Check the rest of the list for a smaller value
			if A[j] < A[min]:  # If a smaller value is found
				min = j  # Update the index of the minimum value
		A[i], A[min] = A[min], A[i]  # Swap the found minimum with the current position
		

def merge_sort(A):
	# If the list has more than one element, proceed to sort
	if len(A) > 1:
		half = len(A) // 2  # Find the midpoint to divide the array
		left = A[:half]     # Create left subarray
		right = A[half:]    # Create right subarray

		# Recursively sort both halves
		merge_sort(left)
		merge_sort(right)

		# Append infinity to both subarrays to act as sentinels
		left.append(inf)
		right.append(inf)

		i = j = 0  # Initialize pointers for left and right subarrays

		# Merge the sorted subarrays back into A
		for k in range(len(A)):
			if left[i] <= right[j]:
				A[k] = left[i]  # Take from left if smaller or equal
				i += 1
			else:
				A[k] = right[j]  # Take from right otherwise
				j += 1
				

def max_heapify(A, n, i):
	largest = i  # Assume current root is largest
	left = 2 * i + 1  # Left child index
	right = left + 1  # Right child index

	# If left child exists and is greater than root
	if left < n and A[left] > A[largest]:
		largest = left
	# If right child exists and is greater than current largest
	if right < n and A[right] > A[largest]:
		largest = right
	# If largest is not root, swap and continue heapifying
	if largest != i:
		A[i], A[largest] = A[largest], A[i]  # Swap root with largest child
		max_heapify(A, n, largest)  # Recursively heapify the affected subtree


def heap_sort(A):
	n = len(A)
	# Build a max heap (rearrange list)
	for i in range(n // 2 - 1, -1, -1):
		max_heapify(A, n, i)
	# Extract elements from heap one by one
	for i in range(n - 1, 0, -1):
		A[i], A[0] = A[0], A[i]  # Move current root to end
		max_heapify(A, i, 0)     # Heapify reduced heap
		

def partition(A, p, r):
	pivot = A[r]  # Choose the last element as the pivot
	i = p - 1  # Initialize the index for the smaller element
	for j in range(p, r):
		if A[j] <= pivot:  # If the current element is less than or equal to the pivot
			i += 1  # Increment the index for the smaller element
			A[i], A[j] = A[j], A[i]  # Swap the elements
	A[i + 1], A[r] = A[r], A[i + 1]  # Place the pivot in its correct position
	return i + 1  # Return the index of the pivot


def quick_sort(A, p=0, r=None):
	if r is None:  # Evaluate this condition only once
			r = len(A) - 1

	def recursive_quick_sort(A, p, r):
		if p < r:  # Base case: stop when the sublist has one or no elements
			pivot_index = partition(A, p, r)  # Partition the list and get the pivot index
			recursive_quick_sort(A, p, pivot_index - 1)  # Recursively sort the left partition
			recursive_quick_sort(A, pivot_index + 1, r)  # Recursively sort the right partition

	# Call the inner recursive function
	recursive_quick_sort(A, p, r)