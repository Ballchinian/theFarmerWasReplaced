def sort(list):
	sortedList = [list[0]]
	index = 0
	
	for num in list:
		if sortedList[len(sortedList)-1] < num:
			sortedList.append(num)
		else:
			for sortedNum in sortedList:
				if sortedNum >= num:
					sortedList.insert(index, num)
					break
				else:
					index = index+1
			index = 0
	sortedList.remove(list[0])
	return(sortedList)

	
	
	
	