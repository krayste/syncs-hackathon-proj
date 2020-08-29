def identify_finals(assessment):

	if assessment.due_str == "Formal exam period":
		assessment.is_final = True