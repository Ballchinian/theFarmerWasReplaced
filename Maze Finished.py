
def oppositeDirection(direction):
	return((direction+2)%4)
clear()
while True:
	maze()
	coordinates = {}
	restore = False
	directions = [North,East,South,West]
	
	#(North, East, West, South, Deadends)
	coordinates[get_pos_x(), get_pos_y()] = [True,True,True,True]

	while True:
		
		#Breaks loop to reset maze from the above while loop
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
			
		previousXCoordinate = get_pos_x() 
		previousYCoordinate = get_pos_y()
		
		
		#Need the checker so it knows when a dead end is a dead end asap
		#tureCounter check makes it less jittery on its way out
		if trueCounter(coordinates[get_pos_x(), get_pos_y()]) >= 3:
			#Checks each direction
			for directionTracker in range(4):
				if coordinates[get_pos_x(), get_pos_y()][directionTracker] == True:
					#if move() forces the drone to move, it doesnt just return True/False so we have to move the drone back
					if move(directions[directionTracker]) == True:
						move(directions[oppositeDirection(directionTracker)])
					else:
						coordinates[get_pos_x(),get_pos_y()][directionTracker] = False
				
		directionTracker = 0
		
		#Checks what directions are valid to travel
		for directionValidator in coordinates[get_pos_x(), get_pos_y()]:
			if directionValidator == True:
				
				move(directions[directionTracker])
				
				#Resets the path that the drone just traveled through so it can eventually travel that path if need be
				if restore == True:
					coordinates[previousXCoordinate, previousYCoordinate][oppositeDirection(previousDirectionTracker)] = True
					restore = False
				
				#Generates new tuples(coordinates) for the new tile if not explored yet
				if (get_pos_x(), get_pos_y()) not in coordinates:
					
					#(North, East, West, South)
					coordinates[get_pos_x(), get_pos_y()] = [True,True,True,True]
					
				#Tracks if the previous place was a dead end, if so invalidate path
				if trueCounter(coordinates[previousXCoordinate, previousYCoordinate]) == 1:
					coordinates[get_pos_x(),get_pos_y()][oppositeDirection(directionTracker)] = False
						
				#Now we want to block the drone from going back in on itself (relates to previous if restore... statement)
				if coordinates[get_pos_x(), get_pos_y()][oppositeDirection(directionTracker)] == True:
					coordinates[get_pos_x(), get_pos_y()][oppositeDirection(directionTracker)] = False
					restore = True
					previousDirectionTracker = directionTracker
				break
			
			#So we can try different directions the tracker shifts
			directionTracker = directionTracker + 1
			
			
			#The fail safe if we hit a dead end. Setting restore to false allows the drone to go back on itself to escape.
			if directionTracker == 4:
				coordinates[previousXCoordinate, previousYCoordinate][oppositeDirection(previousDirectionTracker)] = True
				restore = False
				
		
		