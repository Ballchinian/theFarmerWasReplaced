clear()
def setup():
	for i in range(get_world_size()):
		for i in range(3):
			till()
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			move(North)
		for i in range(3):
			till()
			plant(Entities.Bush)
			move(North)
		
		till()
		trade(Items.Sunflower_Seed)
		plant(Entities.Sunflower)

		for i in range(3):
			move(North)
			
		move(East)
		
def water(x=0.95):
	if get_water() < x:
			use_item(Items.Water_Tank)
			if num_items(Items.water_tank) == 0:
				if num_items(Items.Wood) !=0:
					trade(Items.Empty_Tank)
setup()

petalCount = 0
petalTrackerx = 999
killPetal = 999
while True:
		water()
					
		if get_entity_type() == Entities.Bush:
			harvest()
			plant(Entities.Bush)
			
		elif get_entity_type() == Entities.Carrots:
			harvest()
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			
		elif get_entity_type() == Entities.Grass:
			harvest()
		
		elif get_entity_type() == Entities.Sunflower:
			if get_pos_x() == killPetal:
				harvest()
				trade(Items.Sunflower_Seed)
				plant(Entities.Sunflower)

			if measure() > petalCount:
				petalCount = measure()
				petalTrackerx = get_pos_x()
				
			if get_pos_x() == get_world_size()-1:
				killPetal = petalTrackerx
				petalCount = 0
				petalTrackerx = 999
				
			
			
			
		move(North)
		if get_pos_y() == 0:
			move(East)



			