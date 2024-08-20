def bushHarvesterFast(harvestFastWoodNum):
	while True:
		if harvestFastWoodNum <= num_items(Items.Wood):
			break
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_ground_type() == Grounds.Soil:
					plant(Entities.Bush)
				move(North)
			move(East)