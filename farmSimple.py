def farmSimple(nextResourse, amountNeeded):
	while True:
		for x in range(get_world_size()):
			if num_items(nextResourse) >= amountNeeded:
				break
			for y in range(get_world_size()):
				if nextResourse == Entities.Carrots:
					constCostCarrots = 12 * (get_world_size())**2
					if num_items(Items.Wood) < constCostCarrots:
						#Will need to check if trees are avaialable
						woodPlanter()
						fasterBushHarvester(constCostCarrots)