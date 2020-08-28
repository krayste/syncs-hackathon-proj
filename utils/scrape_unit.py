import pandas as pd
import sys
import unit as u

def find_url(unit_code, year, sem_code):
    # Returns the url for a given unit code
    return "https://www.sydney.edu.au/units/" + unit_code + "/" + str(year) + "-" + sem_code.upper() + "-ND-CC"

def get_assessments(unit_url,unit):
    # Regex for get_html matches the assessments table on the usyd website
    # Modifying the unit object by building up the assessment list 


    try:
        # Read 
        tables = pd.read_html(unit_url, match="Type", header = 0)

        # Remove every second row (gets rid of outcomes assessed)
        tables = [table.iloc[::2] for table in tables]

        # Drop the last row of the table since 
        table = tables[0][:-1]

    except ValueError as ve:
        # If there is no match for "Type", do nothing
        #print("No tables of the assessment found")
        raise ValueError("No Assessment Table found")

    rows = [row for row in table.itertuples()]

    ls = []

    for row in rows:

        assessment = u.Assessment()
        assessment.set_unit(unit)
        assessment.set_type_str(row.Type.split("  ")[0])

        weight = row.Weight.split("  ")[0]
        description = row.Description.split("  ")
        body = None

        if len(description) > 1:
            body = description[1]

        assessment.set_weight_desc_body(weight, description[0], body = body)

        due_string = row.Due.split("  ")
        due_date = None
        if len(due_string) > 1:
            # this is the specific due date for a subject if it is given
            due_date = due_string[1][10:]
        due_string = due_string[0]

        # TODO - implement final exam checking 
        assessment.set_due_strings(due_string, False, due_date = due_date)

        assessment.set_length(row.Length)

        unit.add_assessment(assessment)
        # print(assessment)


def get_schedule(unit_url, unit):
    # Regex for get_html matches the assessments table on the usyd website
    try:
        tables = pd.read_html(unit_url, match="WK", header = 0)
    except ValueError as ve:
        # If there is no match for "Part", do nothing
        print("No tables of the schedule type found")
        raise ValueError("No Schedule Table found")

    table = tables[0]
    rows = [row for row in table.itertuples()]

    # [print(row) for row in rows]
    # print(tables)


def scrape(unit_url, unit):
    assessments = get_assessments(unit_url, unit)
    schedule = get_schedule(unit_url,unit)


def scrape_unit_obj(unit_code, year = '2020', sem_code = 'S2C'):
    unit = u.Unit()
    unit.name = unit_code 

    unit_url = find_url(unit_code, year, sem_code)
    scrape(unit_url, unit)

    print(unit)
    
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