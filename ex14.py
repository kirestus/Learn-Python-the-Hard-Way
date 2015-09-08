from sys import argv

script, user_name, password = argv
prompt = '>'
pw = "fatcock1"

if (str(password) == pw):
	

	print "Hi %s, I'm the %s script." % (user_name, script)
	print "I'd like to ask you a few questions."
	print "Do you like me?"
	like = raw_input(prompt)

	print "Where do you live %s?" % user_name
	lives = raw_input(prompt)

	print ("what kind of computer do you have?")
	computer = raw_input(prompt)

	print"""
	Alright, so i said %s about liking me.
	You live in %s. Not sure where that is.
	And you have a %s computer. Nice!
	""" % (like,lives,computer)