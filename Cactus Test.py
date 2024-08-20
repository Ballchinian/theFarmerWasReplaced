while True:
	if get_ground_type() == Grounds.Turf:
		till()
	if num_items(Items.Cactus_Seed) == 0:
		trade(Items.Cactus_Seed)
	plant(Entities.Cactus)
	print(measure())
	if can_harvest():
		harvest()