clear()
def setup():
	
	def treePlant(evenOddChoice):
		till()
		if treeOddCounter == evenOddChoice:
			plant(Entities.tree)
			
		else:
			trade(Items.Sunflower_Seed)
			plant(Entities.Sunflower)
			petalCountArray.append(measure())
		move(North)
		
	petalCountArray = []
	treeOddCounter = 0
	
	for i in range(get_world_size()):
		for i in range(2):
			till()
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			move(North)
			
			treePlant(2)
			treePlant(0)
			treePlant(2)
			
			move(North)
			
		if treeOddCounter == 0:
			treeOddCounter = 1
		else:
			treeOddCounter = 0
			
		
		move(East)
	return(petalCountArray)
					
petalCountArray = setup()

while True:
		water()
					
		if get_entity_type() == Entities.Tree:
			harvest()
			plant(Entities.Tree)
			
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



			