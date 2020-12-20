def bubbleSort(arr):  # TOC is Big O of n square
	swapped = False
	while swapped == False:
		swapped = True
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
				swapped	 = False
	return arr
