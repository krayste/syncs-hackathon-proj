from django.core.management.base import BaseCommand
from django.utils import timezone
from assessments.models import DB_Unit, DB_Assessment, DB_Schedule, DB_Topic
import utils.find_subj as find
import utils.scrape_unit as scrape


class Command(BaseCommand):
    help = 'Scrape unit information from the web and update database'

    def handle(self, *args, **kwargs):

        # Print time of scraping start to the console
        time = timezone.now().strftime('%X')
        print('Scraping URLs started at %s\n' % time, end="")

        # Set all db unit and child records to inactive
        DB_Unit.objects.all().update(active=False)
        DB_Assessment.objects.all().update(active=False)
        DB_Schedule.objects.all().update(active=False)
        DB_Topic.objects.all().update(active=False)

        thing = find.get_all_unit_codes()
        for ting in thing:
            print(ting)
            (code, name) = ting.split("&")
            try:
                unit_obj = scrape.scrape_unit_obj(code, name)
            except ValueError as ve:
                if str(ve) == "Unit website does not exist":
                    # print("going to next website")
                    f = open("nonExists.txt", "a")
                    f.write("{}\n".format(code))
                    f.close()

                    continue
                else:
                    raise ValueError()
            if DB_Unit.objects.filter(code=unit_obj.code).count() > 0:
                unit_db = DB_Unit.objects.get(code=unit_obj.code)
            else:
                unit_db = DB_Unit()
            unit_db.save_from_obj(unit_obj)
            print("Saving unit {}: {} to database".format(code, name))

        # Delete inactive objects from the database
        DB_Unit.objects.filter(active=False).delete()
        DB_Assessment.objects.filter(active=False).delete()
        DB_Schedule.objects.filter(active=False).delete()
        DB_Topic.objects.filter(active=False).delete()

        # Print time of scraping end to the console
        time = timezone.now().strftime('%X')
        print('\nUnits all saved to database at %s\n' % time, end="")
