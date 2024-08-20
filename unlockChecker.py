def unlockChecker(resourseList):
	#Inefficent, Has to check entire list every time an upgrade goes through
	maxTotal = 0
	unlockTracker = 0
	for unlockListPoint in resourseList:
		total = 0
		for resourses in get_cost(unlockListPoint):
			
			#Devalues carrots under multiplier
			if resourses == Entities.Carrots:
				multiplier = 24
			else:
				multiplier = 1
				
			total = total + multiplier * get_cost(unlockListPoint)[resourses]
			
		if total > maxTotal:
			maxTotal = total
			nextUpgrade = unlockListPoint
			
	
		
	return nextUpgrade, get_cost(nextUpgrade)
	