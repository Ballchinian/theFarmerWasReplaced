def checkFert():
	if num_items(Items.Fertilizer) == 0:
		trade(Items.Fertilizer)
	use_item(Items.Fertilizer)