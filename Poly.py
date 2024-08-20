
def poly():
	clear()

	plantType = {}
	reservePlantType = {}
	
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			
			plantType[x,y] = [x, y, Entities.Grass, 0]
			reservePlantType[x,y] = [x,y , Entities.Tree]
	
	
	while True:
		
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				
				resourseList = unlockChecker(resourseList)
				upgradeList = unlockChecker(upgradeList, False)
				
				if get_entity_type() in [Entities.Bush, Entities.Tree, Entities.Carrots, Entities.Grass]:
					companion, getX, getY = get_companion()
					quick_print(get_companion())
					resourceWanted = Entities.Carrots
					
					
					
					if plantType[getX,getY][3] == 0:
						plantType[getX,getY][2] = companion
					else:
						reservePlantType[getX,getY][2] = companion
	
					
					
					
					
						
					if can_harvest():
						plantType[x,y][3] = 0
								
								
						harvest()
						
							
						
						if plantType[x,y][2] == Entities.Tree:
							treeDetected = 0
							
							
							for adjacent in [((x-1) % 10, y),(x, (y-1) % 10),((x+1) % 10, y),(x,(y+1) % 10)]:
								
								if plantType[adjacent][2] == Entities.Tree:
									plantType[x,y][2] = resourceWanted
									treeDetected = 1
									break
									
							if treeDetected == 0:
								plantType[x,y][3] = 1
		
			
							
	
									
									
									
									
						if plantType[x,y][2] == Entities.Carrots:
							if get_ground_type() == Grounds.Turf:
								till()
							if num_items(Items.Carrot_Seed) == 0:
								trade(Items.Carrot_Seed)
						
						if plantType[x,y][2] != Entities.Grass:
							if get_ground_type() == Grounds.Turf:
								till()
							water(0.5)
							plant(plantType[x,y][2])	
						else:
							if get_ground_type() == Grounds.Soil:
								till()
								
					
						
				move(North)
			move(East)
		