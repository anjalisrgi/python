# Python program to swap first and last element of a list


def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
#code	
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
