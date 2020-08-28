def find_url(unit_code):
	# Returns the url for a given unit code


def get_unit_obj(unit_code):
	
	unit_url = find_url(unit_code)
	
	scrape(unit_url)	
	
	# go to that url
	# create unit object with the name givne
	# populate the attributes other than the lists
	# start populating the lists with new instances of the assessment objects and schedule object
	# return hte object 