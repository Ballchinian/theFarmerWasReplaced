def bushPlanter(threeByThree): 
	if threeByThree == True:
		bushWidth = 3
	else:
		bushWidth = 1
	for width in range(bushWidth):
		till()
		plant(Entities.Bush)
		move(North)
		till()
		plant(Entities.Bush)
		if bushWidth == 3:
			move(North)
			till()
			plant(Entities.Bush)
			move(East)