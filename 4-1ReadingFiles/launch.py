class Teacher(object):
	def __init__(self, name, subject):
		self.name = name
		self. subject = subject
	
	def isSubjectBest(self):
		return self.subject == "Biology"

third = Teacher("Ms. Fiske", "English")
fifth = Teacher("Mr. Flax", "Biology")
print(third.isSubjectBest())
