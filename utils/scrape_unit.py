import pandas as pd
import sys
import unit 

def find_url(unit_code, year, sem_code):
    # Returns the url for a given unit code
    return "https://www.sydney.edu.au/units/" + unit_code + "/" + str(year) + "-" + sem_code.upper() + "-ND-CC"

def get_assessments(unit_url):
    # Regex for get_html matches the assessments table on the usyd website

    assessment = unit.Assessment()

    try:
        # Read 
        tables = pd.read_html(unit_url, match="Type", header = 0)

        # Remove every second row (gets rid of outcomes assessed)
        tables = [table.iloc[::2] for table in tables]

        # Drop the last row of the table since 
        table = tables[0][:-1]

    except ValueError as ve:
        # If there is no match for "Type", do nothing
        print("No tables of the assessment found")
        raise ValueError("No Assessment Table found")

    rows = [row for row in table.itertuples()]
    for row in rows:

        print("Type = {}, Desc. = {}, Weight = {}, Due = {}, Length = {}".format(row.Type.split("  ")[0], row.Description.split("  ")[0], row.Weight.split("  ")[0], row.Due.split("  ")[0], row.Length))
        due_string = row.Due.split("  ")
        if len(due_string) > 1:# and due_string[1].startswith("Due Date:"):
            # this is the specific due date for a subject if it is given
            print(due_string[1][10:])

        description = row.Description.split("  ")
        if len(description) > 1:
            print("Desc Title = {}".format(description[0]))
            print("Desc Body = {}".format(description[1]))

def get_schedule(unit_url):
    # Regex for get_html matches the assessments table on the usyd website
    try:
        tables = pd.read_html(unit_url, match="WK", header = 0)
    except ValueError as ve:
        # If there is no match for "Part", do nothing
        print("No tables of the schedule type found")
        raise ValueError("No Schedule Table found")

    table = tables[0]
    rows = [row for row in table.itertuples()]

    [print(row) for row in rows]
    print(tables)


def scrape(unit_url):
    assessments = get_assessments(unit_url)
    schedule = get_schedule(unit_url)


def scrape_unit_obj(unit_code, year = '2020', sem_code = 'S2C'):
    unit_url = find_url(unit_code, year, sem_code)
    scrape(unit_url)    
    
    # go to that url
    # create unit object with the name givne
    # populate the attributes other than the lists
    # start populating the lists with new instances of the assessment objects and schedule object
    # return hte object 

def main():
    if len(sys.argv) == 2:
        unit_code = sys.argv[1]
        scrape_unit_obj(unit_code)


if __name__ == '__main__':
    main()