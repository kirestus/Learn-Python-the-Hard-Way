from sys import exit

go = ('> ')
def huh(choice):
	print ('i dont understand what you mean by %s' % choice)

def room_gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input(go)
	if choice.isdigit() == True:
		print "This is a digit"
	#if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "5" in choice or "7" in choice or "8" in choice or "9" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice you arent greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
def room_bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice =raw_input(go)
		
		if choice == "take honey":
			dead("The bear looks at you and then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. you can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("the bear gets pissed and chews your face off")
		elif choice == "open door" and bear_moved:
			room_gold_room()
		else:
			huh(choice)
			
def room_cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insaine."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input(go)
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Tasty!!!")
	else:
		huh(choice)
		room_cthulu_room()
		
		
def dead(why):
	print why, "Good job, you tried your best!"
	exit(0)
	
def start():
	print ("You awaken in a dark room.")
	print ("There is a door to your right and left")
	print ('Which one do you take?')
	
	choice = raw_input(go)
	
	if choice == 'left':
		room_bear_room()
	elif choice == 'right':
		room_cthulu_room()
	else:
		dead("You starve like an asshole...")

start()
