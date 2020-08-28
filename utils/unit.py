
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

    def __repr__(self):
        string = "Name = {}\n".format(self.name)
        for ass in self.list_of_assessments:
            string += str(ass)
        for sched in self.list_of_schedules:
            string += str(sched)
        return string

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

    def set_unit(self, unit):
        ''' Set reference back to unit object parent '''
        self.unit = unit

    def set_type_str(self, type_str):
    	self.type_str = type_str

    def set_weight_desc_body(self, weight, description, body=None):
        ''' Setter method for description and weight strings'''
        self.weight = weight
        self.description_title = description
        self.description_body = body

    def set_due_strings(self, due_str, is_final, due_date = None):
        ''' Setter method for the due strings '''
        self.due_str = due_str
        self.is_final = is_final
        self.due_date = due_date
    
    def set_length(self, length):
        ''' Sets the length string attribute '''
        self.length = length 

    def __repr__(self):
        string = ""
        string += "Type: " + self.type_str + "\n"
        string += "Desc: " + self.description_title + "\n"
        string += "Body: " + self.description_body + "\n"
        string += "Weight: " + self.weight + "\n"
        string += "Due: " + self.due_str + "\n"
        if self.due_date:
            string += "Date: " + self.due_date + "\n"
        string += "Final? " + str(self.is_final) + "\n"
        string += "Length: " + self.length + "\n"
        return string


class Schedule:
    def __init__(self):
        self.unit = None

        self.wk_str = None
        self.list_of_topics = []

    def set_unit(self, unit):
        ''' Set reference back to unit object parent '''
        self.unit = unit

    def set_week(self, week):
        self.wk_str = week

    def add_topic(self, topic):
        ''' Appends a topic object to the list of topics '''
        self.list_of_topics.append(topic)

    def __repr__(self):
        string = self.wk_str + " "
        for topic in self.list_of_topics:
            string += str(topic) + "\n"

        return string 

class Topic:
    def __init__(self):
        self.schedule = None
        self.topic_str = None
        self.learning_str = None

    def set_schedule(self, schedule):
        ''' Set reference back to schedule object parent '''
        self.schedule = schedule

    def set_topic_learn(self, topic_str, learning_str):
        self.topic_str = topic_str
        self.learning_str = learning_str

    def __repr__(self):
        return "{}: {}".format(self.topic_str, self.learning_str)

def test_filling():
    # Test filling out an object INCOMPLETE
    topic = Topic()
    topic.set_topic_learn("1. Introduction to the unit;", "Online class (2 hr)")
    
    schedule = Schedule()
    schedule.set_week("Week 01")
    schedule.add_topic(topic)

    unit = Unit()
    unit.set_names("Object Oriented Programming", "INFO1113")
    unit.add_schedule(schedule)

    final_exam = Assessment()
    final_exam.set_type_str("Final exam (open book)")
    final_exam.set_weight_desc_body("50%", "Written Final Exam", "It covers all aspects of this unit.")
    final_exam.set_due_strings("Formal exam period", True)
    final_exam.set_length("2 hours")
    unit.add_assessment(final_exam)

    online_task = Assessment()
    online_task.set_type_str("Online Task")
    online_task.set_weight_desc_body("10%", "Online Task", "Several Online Tasks to be completed throughout the semester. Please see the Canvas Page of this unit to know the due dates of these tasks.")
    online_task.set_due_strings("Multiple weeks", False)
    online_task.set_length("N/A")
    unit.add_assessment(online_task)

    small_test1 = Assessment()
    small_test1.set_type_str("Small test")
    small_test1.set_weight_desc_body("7%", "Online Quiz 1", "Two quizzes are to be completed respectively in Week 6 and week 11. These quizzes are designed to test both knowledge and skills of course materials in the semester thus far.")
    small_test1.set_due_strings("Week 06", False)
    small_test1.set_length("40 minute quiz")
    unit.add_assessment(small_test1)

    assignment1 = Assessment()
    assignment1.set_type_str("Assignment")
    assignment1.set_weight_desc_body("10%", "Assignment 1", "Demonstrating programming ability from specification")
    assignment1.set_due_strings("Week 07", False)
    assignment1.set_length("N/A")
    unit.add_assessment(assignment1)

    small_test2 = Assessment()
    small_test2.set_type_str("Small test")
    small_test2.set_weight_desc_body("8%", "Online Quiz 2", "Two quizzes are to be completed respectively in Week 6 and week 11. These quizzes are designed to test both knowledge and skills of course materials in the semester thus far.")
    small_test2.set_due_strings("Week 11", False)
    small_test2.set_length("40 minute quiz")
    unit.add_assessment(small_test2)

    assignment2 = Assessment()
    assignment2.set_type_str("Assignment")
    assignment2.set_weight_desc_body("15%", "Assignment 2", "Demonstrating programming ability from specification")
    assignment2.set_due_strings("Week 12", False)
    assignment2.set_length("N/A")
    unit.add_assessment(assignment2)

    return unit

if __name__ == "__main__":
    unit = test_filling()
