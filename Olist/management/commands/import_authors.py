import csv
from django.core.management.base import BaseCommand
from Olist.models import Author

class Command(BaseCommand):
    help = 'Import authors from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path of CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0].strip()
                if name:
                    Author.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Import Successfull'))
