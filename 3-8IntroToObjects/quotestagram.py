# quotestagram.py
# the best quote-sharing service

class Quote(object):

	def __init__(self, quote_text, user_posted, location, num_likes):

		self.quote_text = quote_text
		self.user_posted = user_posted
		self.location = location
		self.num_likes = num_likes

	# adds one to the 'like' count
	def like(self):
		self.num_likes = self.num_likes + 1

	# takes one away from the 'like' count
	def un_like(self):
		self.num_likes = self.num_likes - 1

	# prints the full quote
	def show_quote(self):
		print("U: " + self.user_posted)	
		print("L: " + self.location)
		print("Quote: " + self.quote_text)
		print("Likes: " + str(self.num_likes))

# post some quotes
x = Quote("Nothing with Shawn.", "kevin_is_kool", "San Francisco", 0)
y = Quote("If I wasn't crazy, I'd be insane.", "me", "The Edge of The World", 0)
z = Quote("It doesn't matter.", "michelle", "Starbucks San Pablo", 0)

# print our quotes
z.show_quote()

# put Quotes in a list
my_quotes = []
my_quotes.append(x)
my_quotes.append(y)
my_quotes.append(z)
user_quote = "Hello. How are you?"
speaker = "Adele"
location = "London"

my_quotes.append(Quote(user_quote, speaker, location, 0))

# call our show_quote function for all of our Quote objects
for q in my_quotes:
	q.show_quote()







