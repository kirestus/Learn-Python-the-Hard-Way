print "you enter a dark room with two doors. Do you go through door #1 or door #2?"

choose = "> "

door = raw_input(choose)

if door == '1':
	print "There's a giant bear here eating a cheese cake. what do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input(choose)
	
	if bear == '1':
		print "the bear eats your face off... good job!"
	elif bear == '2':
		print "the bear eats your legs off... good jorb!"
	else:
		print "Well... doing %s is proball better... Bear runs away" % bear
		
elif door == '2':
	print "You stare into the endless abyss at a chihuhuas retina"
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. understing revolvers yelling melodies."
	
	insanity= raw_input(choose)
	
	if insanity == "1" or insanity == '2':
		print "Your body survives by a mind of jello. Good Job!"
	else:
		print "the insanity rots your eyes into a pool of muck! Good Job!"
	
else:
	print "you stumble around and fall on a kind and die. Good Job!"
