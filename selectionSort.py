def selectionSort(arr):   # TOC is Big O of n square
  for i in range(len(arr)):
    currPos = i
    for j in range(i,len(arr)):
      if arr[currPos] > arr[j]:
        currPos = j
    arr[i],arr[currPos] = arr[currPos],arr[i]
  return arr
