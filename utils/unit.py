
class Unit:
	def __init__(self):
		self.name = None
		self.code = None
		self.has_final = None
		self.list_of_assessments = []
		self.list_of_schedules = []

	def set_names(self, name, code):
		''' Fill the name and codes '''
		self.name = name
		self.code = code

	def add_assessment(self, assessment):
		''' Appends a blank assessment object to the unit's list '''
		self.list_of_assessments.append(assessment)

	def add_schedule(self, schedule):
		''' Appends a blank schedule object to the unit's list '''
		self.list_of_schedules.append(schedule)

class Assessment:
	def __init__(self):
		# Reference to a unit object 
		self.unit = None

		self.type_str = None
		self.description_title = None
		self.description_body = None

		self.weight = None 

		# Due str, ie "Multiple Weeks"
		self.due_str = None
		self.due_date = None 
		self.is_final = False
		self.length = None 

	def set_weight_desc_body(self, weight, description, body=None):
		''' Setter method for description and weight strings'''
		self.weight = weight
		self.description_body = description
		self.description_body = body

	def set_due_strings(self, due_str, is_final, due_date = None):
		''' Setter method for the due strings '''
		self.due_str = due_str
		self.is_final = is_final
		self.due_date = due_date
	def set_length(self, length):
		''' Sets the length string attribute '''
		self.length = length 

class Schedule:
	def __init__(self):
		self.wk_str = None
		self.list_of_topics = []

	def set_week(self, week):
		self.wk_str = week

	def add_topic(self, topic):
		''' Appends a topic object to the list of topics '''
		self.list_of_topics.append(topic)

class Topic:
	def __init__(self):
		self.topic_str = None
		self.learning_str = None

	def set_topic_learn(self, topic_str, learning_str):
		self.topic_str = topic_str
		self.learning_str = learning_str

def test_filling():
	# Test filling out an object INCOMPLETE
	topic = Topic()
	topic.set_topic_learn("1. Introduction to the unit;", "Online class (2 hr)")
	
	schedule = Schedule()
	schedule.set_week("Week 01")
	schedule.add_topic(topic)

	assessment = Assessment()
	assessment.set_weight_desc_body("")

	unit = Unit()
	unit.set_names("Object Oriented Programming", "INFO1113")


if __name__ == "__main__":
	print("Test")
