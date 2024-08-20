def setup():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
				
			if get_entity_type() != Entities.Pumpkin:
				harvest()
				
			if num_items(Items.Pumpkin_Seed) == 0:
				trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
			move(North)
		
		move(East)
	move(North)
		

setup()

startLocation = (get_pos_x(), get_pos_y())

while True:
	for land in range (get_world_size()):
		while True:
			if get_entity_type() != Entities.Pumpkin:
				if num_items(Items.Pumpkin_Seed) == 0:
					trade(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)
			
			elif can_harvest():
				break
			checkFert()
		move(North)
		
	move(East)
	
	if (get_pos_x(), get_pos_y()) == startLocation:
		harvest()



			