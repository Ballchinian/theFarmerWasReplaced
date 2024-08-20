clear()
def setup():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Turf:
				till()
			if get_entity_type() != Entities.Cactus:
				harvest()
			if num_items(Items.Cactus_Seed) == 0:
				trade(Items.Cactus_Seed)
			plant(Entities.Cactus)
			move(North)
		move(East)

def cactusSort(LatOrHor):
	if LatOrHor == 'Lat':
		direction = North
		directionEnd = East
		
	elif LatOrHor == 'Hor':
		direction = East
		directionEnd = North
		
	for x in range(get_world_size()):
		moveOn = False
		for y in range(get_world_size()):
			if LatOrHor == 'Lat':
				cactusCountDict[get_pos_y()] = measure()
			elif LatOrHor == 'Hor':
				cactusCountDict[get_pos_x()] = measure()
			move(direction)
		while moveOn == False:
			moveOn = True

			for ySouthNorth in range(get_world_size()-1):
				if cactusCountDict[ySouthNorth] > cactusCountDict[ySouthNorth+1]:
					moveOn = False
					swap(direction)
					swappedCactus = cactusCountDict[ySouthNorth]
					cactusCountDict[ySouthNorth] = cactusCountDict[ySouthNorth+1]
					cactusCountDict[ySouthNorth+1] = swappedCactus
				move(direction)
			move(direction)
			
		move(directionEnd)

setup()


while True:
	cactusCountDict = {}
	
	
	cactusSort('Lat')
	cactusSort('Hor')
	harvest()
	setup()
			
			
			
				
			