from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Scrape unit information from the web and update database'

    def handle(self, *args, **kwargs):

        # Print time of scraping start to the console
        time = timezone.now().strftime('%X')
        print('Scraping URLs started at %s\n' % time, end="")

        # Print time of scraping end to the console
        time = timezone.now().strftime('%X')
        print('\nUnits all saved to database at %s\n' % time, end="")
