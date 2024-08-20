clear()
def setup():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			till()
			move(North)
		
		move(East)
		

setup()
pumpkinTracker = True
while True:
		water()
		if get_entity_type() != Entities.Pumpkin:
			if num_items(Items.Pumpkin_Seed) == 0:
				trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
			pumpkinTracker = False
		move(North)

		if get_pos_y() == 0:
			move(East)
			if get_pos_x() == 0:
				if pumpkinTracker:
					harvest()
				else:
					pumpkinTracker = True




			