def insertionSort(arr):   # TOC is Big O of n square
	for end in range(len(arr)):
		pos = end
		while pos>0 and arr[pos]<arr[pos-1]:
			arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
			pos = pos-1
	return arr

print(insertionSort([2,4,1,9,0,333,5,66,3]))
