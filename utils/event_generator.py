from ics import Calendar, Event, DisplayAlarm
import arrow
import datetime
import utils.unit as u

# hardcoding the start of sem 2 because we're disgusting
start_sem = arrow.get("2020-08-24", "YYYY-MM-DD")
formal_exam_period = arrow.get("2020-11-30", "YYYY-MM-DD")
midsem_break = 7

def event_generator(units):

	# set up a calendar
	c = Calendar()
	c.creator = "The Null Pointers"

	# set up a dictionary for the general week events
	weekly = {}
	for i in range(1,14):
		weekly[i] = []

	# set up a list of formal exams
	final_exams = []

	for unit in units:

		for assessment in unit.list_of_assessments:

			# if the assessment has a due date we want to create an event
			# for it
			if assessment.due_date != None:

				e = Event()
				e.name = unit.code + ": " + assessment.description_title + " (" + "weighting: " + assessment.weight + ")"
				date = arrow.get(assessment.due_date, "DD MMM YYYY")
				e.begin = date
				e.description = assessment.description_body

				c.events.add(e)

			if assessment.due_str.startswith("Week "):

				week = int(assessment.due_str.split()[1])
				weekly[week].append(assessment)

			if assessment.is_final:
				final_exams.append(assessment)

	# loop through the general weekly assessments
	for week in sorted(weekly.keys()):

		if weekly[week] == []:
			continue

		e = Event()
		e.name = "Week " + str(week) + " Assessments"

		desc = ""
		for assessment in weekly[week]:
			desc += assessment.unit.code +": " + assessment.description_title + " (weighting: " + assessment.weight + ")"+ "\n"

		# shift by 1 to account for midsem break
		if week > 7:
			week += 1
		date = start_sem.shift(weeks=week-1)
		e.begin = date

		e.description = desc
		c.events.add(e)

	if final_exams != []:

		e = Event()
		e.name = "Your final exams"
		desc = ""
		for assessment in final_exams:
			desc += assessment.unit.code + ": " + assessment.description_title + " (weighting: " + assessment.weight + ")" + "\n"
		e.description = desc
		e.begin = formal_exam_period
		c.events.add(e)

	with open('static_files/calendar.ics', 'w+') as my_file:
		my_file.writelines(c)

# def get_timestring(assessment):
# 	''' Returns an arrow-formatted timestring for a assessment object '''
# 	if assessment.due_date != None:
# 		date = str(arrow.get(assessment.due_date, "DD MMM YYYY"))

# 	elif assessment.due_str.startswith("Week"):
# 		week = int(assessment.due_str.split()[1])
# 		# shift by 1 to account for midsem break
# 		if week > 7:
# 			week += 1
# 		date = str(start_sem.shift(weeks=week))

# 	elif assessment.due_str == "Formal exam period":
# 		date = str(formal_exam_period)

# 	else:
# 		# Hardcoded shifting to the end by 30 weeks
# 		date = str(start_sem.shift(weeks=30))

# 	return date

if __name__ == '__main__':
	units = [u.test_filling()]
	event_generator(units)