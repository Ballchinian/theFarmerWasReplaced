clear()
def setup():
	petalCountArray = []
	for i in range(get_world_size()):
		for i in range(1):
			till()
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			move(North)
		for i in range(2):
			till()
			plant(Entities.Bush)
			move(North)
		
		for i in range (5):
			till()
			trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)
			petalCountArray.append(measure())
			move(North)
	
		for i in range(2):
			move(North)
			
		move(East)
	return(petalCountArray)
		
def water(x=0.95):
	if get_water() < x:
			use_item(Items.Water_Tank)
			if num_items(Items.water_tank) == 0:
				if num_items(Items.Wood) !=0:
					trade(Items.Empty_Tank)
					
petalCountArray = setup()

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
			if max(petalCountArray) == measure():
				harvest()
				trade(Items.Sunflower_Seed)
				plant(Entities.Sunflower)
				petalCountArray.remove(max(petalCountArray))
				petalCountArray.append(measure())
				
				
				
			
			
			
		move(North)
		if get_pos_y() == 0:
			move(East)



			