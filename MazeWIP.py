coordinates = {}
restore = False
directions = [North,East,South,West]

#(North, East, West, South, Deadends)
coordinates[get_pos_x(), get_pos_y()] = [True,True,True,True]

def oppositeDirection(direction):
	return((direction+2)%4)
			

while True:
	
	if get_entity_type() == Entities.Treasure:
		harvest()
	previousXCoordinate = get_pos_x() 
	previousYCoordinate = get_pos_y()
	

	directionTracker = 0
	
	for directionValidator in coordinates[get_pos_x(), get_pos_y()]:
		#So the drone cant go along already broken paths
		if directionValidator == True:
			
			
			if move(directions[directionTracker]) == True:
				#Resets the path
				if restore == True:
					coordinates[previousXCoordinate, previousYCoordinate][oppositeDirection(previousDirectionTracker)] = True
					restore = False
				
				if (get_pos_x(), get_pos_y()) not in coordinates:
					#(North, East, West, South, Deadends)
					coordinates[get_pos_x(), get_pos_y()] = [True,True,True,True]
				
				#Tracks if the previous place was a dead end, if so invalidate path
				if trueCounter(coordinates[previousXCoordinate, previousYCoordinate]) == 1:
					coordinates[get_pos_x(),get_pos_y()][oppositeDirection(directionTracker)] = False
					
				#Now we want to block the drone from going back in on itself
				if coordinates[get_pos_x(), get_pos_y()][oppositeDirection(directionTracker)] == True:
					
					coordinates[get_pos_x(), get_pos_y()][oppositeDirection(directionTracker)] = False
					restore = True
					previousDirectionTracker = directionTracker
				break
			else:
				#Invalidates B
				coordinates[get_pos_x(), get_pos_y()][directionTracker] = False
		directionTracker = directionTracker + 1
		if directionTracker == 4:
			coordinates[previousXCoordinate, previousYCoordinate][oppositeDirection(previousDirectionTracker)] = True
			restore = False
			
	quick_print(get_pos_x(), get_pos_y())
	quick_print(coordinates[get_pos_x(), get_pos_y()])
	