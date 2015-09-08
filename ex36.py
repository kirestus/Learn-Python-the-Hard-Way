from sys import exit

cursor = ("> ")
rooms = {
	'Jail Cell' : 'You awaken in a small jailcell with a skeleton in it and door that exits to the south',
	'Long Hallway':'A long tretcherus hallway  with a bright light coming from the far south end'
}


#calls the menu to choose from
def menu():
	menu_state = 0
	print "+================+"
	print "# 1.) look at    #"
	print "# 2.) pick up    #"
	print "# 3.) push/pull  #"
	print "# 4.) open       #"
	print "# 5.) use item   #"
	print "# 6.) talk to    #"
	print "# 7.) fight      #"
	print "+================+"
	print "\nWhat do you do?"
	while menu_state == 0:
		choice = raw_input(cursor)
		#limits the input to only choices on the menu
		if choice.isdigit() == True and int(choice) <= 7 and int(choice) > 0:
			print "good choice"
			menu_state = 1;
			return choice
		else:
			print "need a number here"

def inventory():

	print "werd"
	

#describe the room you are in and return the name of the room
def describe_room(room_number):
	room_name = "nul"
	room_describe = "nul"
	
	if room_number == 1:
		room_name = rooms[]
		print rooms('Jail Cell')
	elif room_number == 2:
		print rooms('Long Hallway')
	else:
		print "you broke it"
	
	print (room_describe)
	return room_name
	

describe_room(1)
#menu()

