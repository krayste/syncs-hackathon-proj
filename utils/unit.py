
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

    def set_due_strings(self, due_str, is_final, due_date=None):
        ''' Setter method for the due strings '''
        self.due_str = due_str
        self.is_final = is_final
        self.due_date = due_date

    def set_length(self, length):
        ''' Sets the length string attribute '''
        self.length = length

    assessment = Assessment()
    assessment.set_weight_desc_body("50%", "Written Final Exam", "It covers all aspects of this unit.")
    assessment.set_due_strings("Formal exam period", True)
    assessment.set_length("2 hours")

    unit = Unit()
    unit.set_names("Object Oriented Programming", "INFO1113")
    unit.add_assessment(assessment)
    unit.add_schedule(schedule)
    return unit


if __name__ == "__main__":
    unit = test_filling()
=======
    assessment = Assessment()
    assessment.set_weight_desc_body("")

    unit = Unit()
    unit.set_names("Object Oriented Programming", "INFO1113")


if __name__ == "__main__":
    print("Test")
>>>>>>> Stashed changes
