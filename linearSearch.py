def linearSearch(arr,seek):  # TOC is Big O of n
	found = False
	for element in range(len(arr)):
		if arr[element] == seek:
			found = True
			return element
	if found == False:
		return -1
 
print(linearSearch([5,63,6,2,1],1))
