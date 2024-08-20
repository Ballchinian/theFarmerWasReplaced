clear()
def maze():
	plant(Entities.Bush)
	while True:
		if num_items(Items.Fertilizer) == 0:
			trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
		if get_entity_type() == Entities.Hedge:
			break
			
maze()