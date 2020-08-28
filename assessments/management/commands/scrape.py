from django.core.management.base import BaseCommand
from django.utils import timezone
import assessments.models
import utils.find_subj as find
import utils.scrape_unit as scrape


class Command(BaseCommand):
    help = 'Scrape unit information from the web and update database'

    def handle(self, *args, **kwargs):

        # Print time of scraping start to the console
        time = timezone.now().strftime('%X')
        print('Scraping URLs started at %s\n' % time, end="")

        thing = find.get_all_unit_codes()
        for ting in thing:
        	print(ting)
        	(code, name) = ting.split("&")
        	try:
        		scrape.scrape_unit_obj(code, name)
        	except ValueError as ve:
        		if str(ve) == "Unit website does not exist":
        			print("going to next website")
        			f = open("nonExists.txt", "a")
        			f.write("{}\n".format(code))
        			f.close()

        			continue
        		else:
        			raise ValueError()
        	print("Saving unit {}: {} to database".format(code, name))
        # Print time of scraping end to the console
        time = timezone.now().strftime('%X')
        print('\nUnits all saved to database at %s\n' % time, end="")
