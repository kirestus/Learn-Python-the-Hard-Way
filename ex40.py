class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I dont want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around your family",
						"With a pocket full of shells"])
						
shake_ya_ass = Song(["Shake ya ass!",
						"Watch ya self!",
						"Shake ya ass!",
						"Show me whatcha workin with!"])
						
shake_ya_ass.sing_me_a_song()						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
