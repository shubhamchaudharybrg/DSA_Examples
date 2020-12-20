def quickSort(arr):     # TOC is Big O of log n
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop()
		higher = []
		lower = []
		for i in arr:
			if i > pivot:
				higher.append(i)
			else:
				lower.append(i)
		return quickSort(lower)+[pivot]+quickSort(higher)
		
print(quickSort([333,0,4,3,88,4,2,5,6,7,222]))				
