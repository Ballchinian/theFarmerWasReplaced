def water(fert=0.95):
	if get_water() < fert:
			use_item(Items.Water_Tank)
			if num_items(Items.water_tank) == 0:
				if num_items(Items.Wood) !=0:
					trade(Items.Empty_Tank)