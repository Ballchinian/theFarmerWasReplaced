def woodPlanter():
	#Need to change to include Wood
	y=get_pos_y()
	while get_pos_y() != 0:
		if y>=get_world_size()/2:
			move(North)
		elif y<get_world_size()/2:
			move(South)
	for x in range(get_world_size()):
			
		harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		move(North)
		for y in range(get_world_size()-1):
			harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Bush)
			move(North)
		move(East)
		