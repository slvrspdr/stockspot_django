from django.core.management.base import BaseCommand, CommandError
from api.models import Company

import json

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='company data file path')
        parser.add_argument("-d", "--delete", action="store_true", help='Delete all existing data')

    def handle(self, *args, **options):
        if options["delete"]:
            print("** delete all records in Company table")
            Company.objects.all().delete()

        company_file = options['file_path']
        print("** import {} file".format(company_file))
        with open(company_file) as json_file:
            data = json.load(json_file)
            for p in data:
                company = Company()
                company.index = p.get('index', 0)
                company.company = p.get('company', '')
                company.save()
        print("** Completed")  