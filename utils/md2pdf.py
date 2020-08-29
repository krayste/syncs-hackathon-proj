import pypandoc
from utils.unit import Assessment
import arrow

''' if running for first time, run this snippet

# expects an installed pypandoc: pip install pypandoc
from pypandoc.pandoc_download import download_pandoc
# see the documentation how to customize the installation path
# but be aware that you then need to include it in the `PATH`
download_pandoc()

#note for later: Put this in setup.py @Josh TODO://

'''

# This is all just making the file into one nice long string

# function to take a list of unit objects and order their assessment objects by week and then due date
def order_ass(units):

	assessments = []

	for unit in units:
		for ass in unit.list_of_assessments:
			assessments.append(ass)

	ass_dict = Assessment.create_dictionary(assessments)

	ordered_ass = []
	for key in sorted(ass_dict.keys()):

		for ass in ass_dict[key]:
			ordered_ass.append(ass)

	return ordered_ass

#f = open("../assignment_dates.md")
#string = f.readlines()
#string = "".join(string)





def create_md_string(list_of_assessments):
	string = '''| **Subject** | **Type**| **Description** | **Weighting** | **Due Date** |
	|==|==|==|==|==|\n'''
	for assessment in list_of_assessments:
		new_line = "|\n"
		new_line += "| " +assessment.unit.code + " |\n"
		new_line += "| " +assessment.type_str + " |\n"
		new_line += "| " +assessment.description_title + " |\n"
		new_line += "| " +assessment.weight + " |\n"
		new_line += "| " +assessment.due_str + " |\n"
		string += new_line + "\n" 

	return string

def string_to_pdf(markdown_string):
	output = pypandoc.convert_text(markdown_string, 'pdf', outputfile="../output.pdf", format="md", extra_args=['-H','static_files/options.sty'])
	return
