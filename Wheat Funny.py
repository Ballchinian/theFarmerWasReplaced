def wheatNum(harvestHayNum):
	while num_items(Items.Hay) <= harvestHayNum:
		if can_harvest():
			harvest()
			
		
