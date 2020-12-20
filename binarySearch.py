def binarySearch(arr,seek):  #TOC is Big O of log n
	l = 0
	h = len(arr) - 1
	while l <= h:
		mid = (l+h)//2
		if arr[mid] == seek:
			return mid
		elif arr[mid] > seek:
			h = mid - 1
		elif arr[mid] < seek:
			l = mid + 1
	return -1
