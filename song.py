"""
create a class Song that has methods: __init__(self, lyrics) 
where lyrics is a list containing the lines of the input song, 
and singmeasong that prints all the lines of the song.
"""

class Song():
	
	def __init__(self, title):
		self.title = title
		self.lyrics = []

	def add_lyrics(self, lyrics):
		self.lyrics.append(lyrics)

	def sing_me_a_song(self):
		print(self.title)
		print(self.lyrics)


t = Song("Mary Had A Little Lamb")
t.add_lyrics("Mary had a little lamb,")
t.add_lyrics("It's fleece was white as snow, yeah.")
t.add_lyrics("Everywhere the child went,")
t.add_lyrics("The little lamb was sure to go, yeah.")
t.add_lyrics("He followed her to school one day,")
t.add_lyrics("And broke the teachers rule.")
t.add_lyrics("What a time did they have,")
t.add_lyrics("That day at school.")
t.add_lyrics("Tisket, tasket,")
t.add_lyrics("A green and yellow basket.")
t.add_lyrics("Sent a letter to my baby,")
t.add_lyrics("On my way I passed it.")
t.sing_me_a_song()



