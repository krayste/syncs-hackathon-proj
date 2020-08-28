from ics import Calendar, Event
import arrow

# for testing
from utils.unit import test_filling

# hardcoding the start of sem 2 because we're disgusting
start_sem = arrow.get("2020-08-24", "YYYY-MM-DD")
formal_exam_period = arrow.get("2020-11-30", "YYYY-MM-DD")
midsem_break = 7

def event_generator(units):

	c = Calendar()
	for unit in units:

		for assessment in unit.list_of_assessments:

			if assessment.due_date != None:
				e = Event()
				e.name = unit.code + ": " + assessment.type_str
				date = arrow.get(assessment.due_date, "DD MMM YYYY")
				e.begin = date
				c.events.add(e)

			elif assessment.due_str.startswith("Week"):
				e = Event()
				e.name = unit.code + ": " + assessment.type_str
				week = int(assessment.due_str.split()[1])

				# shift by 1 to account for midsem break
				if week > 7:
					week += 1
				date = start_sem.shift(weeks=week)
				e.begin = date
				c.events.add(e)

			elif assessment.due_str == "Formal exam period":
				e = Event()
				e.name = unit.code + ": " + assessment.type_str
				e.begin = formal_exam_period
				c.events.add(e)

	with open('calendar.ics', 'w') as my_file:
		my_file.writelines(c)

units = [test_filling()]
event_generator(units)