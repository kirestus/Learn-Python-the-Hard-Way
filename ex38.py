item_list= ['sword','key','gauntlet','trombone']

more_items = "Ryan A4 Marina Gus Souljaboy DBZ LINUX"
more_items_list = more_items.split(' ')

print item_list[0:4]

while len(item_list) < 10:
	next_one = more_items_list.pop()
	print next_one
	item_list.append(next_one)
	print item_list
