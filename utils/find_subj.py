import pandas as pd
import sys


def get_all_unit_codes(session = 'S2C', year = '2020'):
	tables = pd.read_html('https://www.timetable.usyd.edu.au/uostimetables/' + year)
	table = tables[0].itertuples() 
	for row in table:
		if row[2] == session:
			yield "{}&{}".format(row[1], row[4])

def main():
	yield_next = get_all_unit_codes()
	while True:

		print(next(yield_next))

if __name__ == '__main__':
	main()