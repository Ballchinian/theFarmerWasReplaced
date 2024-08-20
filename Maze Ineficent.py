clear()
def maze():
	plant(Entities.Bush)
	while True:
		if can_harvest():
			for i in range(25):
				if num_items(Items.Fertilizer) == 0:
					trade(Items.Fertilizer)
				use_item(Items.Fertilizer)
			break
			
movementList = [0,1,2,3]
maze()
while True:
	movementIndex = random() * 4
	movement = movementList[movementIndex]
	if movement == 0:
		direction = North
	elif movement == 1:
		direction = East
	elif movement == 2:
		direction = South
	elif movement == 3:
		direction = West
	move(direction)


	if get_entity_type() == Entities.Treasure:
		harvest()
		maze()
	