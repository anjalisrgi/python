# Python program to swap first and last element of a list
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
#code	
newList = [36, 34, 32, 30, 29]
print(swapList(newList))
