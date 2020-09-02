from django.core.management.base import BaseCommand, CommandError
from api.models import People
from dateutil.parser import parse

import json

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='people data file path')
        parser.add_argument("-d", "--delete", action="store_true", help='Delete all existing data')

    def handle(self, *args, **options):
        if options["delete"]:
            print("** delete all records in People table")
            People.objects.all().delete()
        
        people_file = options['file_path']
        print("** import {} file".format(people_file))
        with open(people_file) as json_file:
            data = json.load(json_file)
            for p in data:
                people = People()
                people.index = p.get('index', 0)
                people.guid = p.get('guid', '')
                people.has_died= p.get('has_died', False)
                people.balance = p.get('balance', '')
                people.picture = p.get('picture', '')
                people.age = p.get('age', 0)
                people.eyeColor = p.get('eyeColor', '')
                people.name = p.get('name', '')
                people.gender = p.get('gender', '')
                people.company_id = p.get('company_id', 0)
                people.email = p.get('email', '')
                people.phone = p.get('phone', '')
                people.address = p.get('address', '')
                people.about = p.get('about', '')
                people.registered = parse(p.get('registered', ''))
                people.tags = p.get('tags', [])
                people.friends = p.get('friends', [])
                people.greeting = p.get('greeting', '')
                people.favouriteFood = p.get('favouriteFood', [])
                people.save()

        print("** Completed")        
