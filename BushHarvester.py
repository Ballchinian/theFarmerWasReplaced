def bushHarvester(harvestWoodNum):

	while num_items(Items.Wood) <= harvestWoodNum:
		if can_harvest():
			harvest()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Bush)
			else:
				currentTime = get_time() 
				while True:
					if get_time() - currentTime <= 3.3:
						if can_harvest():
							harvest()
					else:
						break
		move(North)