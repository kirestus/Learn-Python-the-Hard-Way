from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print('This scene is not yet configured. Subclass it and impliment enter()')
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to print out the last scene
		current_scene.enter()
		
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"Great Jorb!11!"
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet"
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container. There's a keypad lock on hte box"
		print "and you need the code to get the bomb out. If you can get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guess <10:
			print "BZZZEDDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "The container clicks open and the seal breaksm letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes on last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
		
		
class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "You burst onto the Bridge with the neutron destuct bomb"
		print "under your arm and suprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons outyet, as they see the active bomb under your"
		print "arm and don't what to set it off."
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'
		
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
		
class TheBridge(Scene):

	def enter(self):
		pass
		
class EscapePod(Scene):
	
	def enter(self):
		pass
		
class Map(object):

	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass
		

a_map = Map('centeral_corridor')
a_game = Engine(a_map)
a_game.play()
