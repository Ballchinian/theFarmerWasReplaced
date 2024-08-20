def setup():
	
	petalCountDict = {}
	for i in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Turf:
				till()
			if get_entity_type() != Entities.Sunflower:
				harvest()
				
			if num_items(Items.Sunflower_Seed) == 0:
				trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)
			petalCountDict[get_pos_x(), get_pos_y()] = measure()
			move(North)
		move(East)
		
	tracker = 15
	petalTrackerBin = 0
	
	return(petalCountDict, tracker, petalTrackerBin)
	
petalCountDict, tracker, petalTrackerBin = setup()
	
while True:
	if tracker <= 10:
		harvest()
		petalCountDict, tracker, petalTrackerBin = setup()
	for coordinates in petalCountDict:
		if petalCountDict[coordinates] == tracker:
			if petalTrackerBin == 0:
				petalTrackerBin = 1
				
			x, y = coordinates
			if x-get_pos_x() >= 0: 
				for xMove in range(x-get_pos_x()):
					move(East)
			else:
				for xMove in range(get_pos_x()-x):
					move(West)
					
			if y-get_pos_y() >= 0: 
				for yMove in range(y-get_pos_y()):
					move(North)
			else:
				for yMove in range(get_pos_y()-y):
					move(South)

			water()
			
			if can_harvest():
				harvest()
				if num_items(Items.Sunflower_Seed) == 0:
					trade(Items.Sunflower_Seed)
				plant(Entities.Sunflower)
				petalCountDict[get_pos_x(), get_pos_y()] = measure()
				if measure() >= tracker:
					tracker = measure()
			else:
				checkFert()
					
	
	if petalTrackerBin == 0:
		tracker = tracker - 1
		petalTrackerBin = 0
	petalTrackerBin = 0
			