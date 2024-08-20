clear()
def setup():
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if num_items(Items.Egg) == 0:
				trade(Items.Egg)
			use_item(Items.Egg)
			move(North)
		move(East)
		
directions = [North,East,South,West]
setup()
while True:
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if get_entity_type() != Entities.Dinosaur:
				if num_items(Items.Egg) == 0:
					trade(Items.Egg)
				use_item(Items.Egg)
				
			adjacent = 0
			for direction in directions:
				chickenType = measure()
				if measure(direction) == chickenType:
					adjacent = adjacent + 1
			if adjacent >= 3:
				harvest()
			move(North)
		move(East)
			