class Poem(object):
	def __init__(self, category, text, rhymes):
		self.category = category
		self.text = text
		self.rhymes = rhymes

	def isHaiku(self):
		return self.category == "haiku"

myPoem = Poem("Seuss", "New socks. Two socks. Whose socks? Sue's socks.", rhymes = True)
print(myPoem.text + " Haiku?" + str(myPoem.isHaiku()))
