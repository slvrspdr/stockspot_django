from django.test import TestCase
from django.test import Client

from django.core.management import call_command

from .models import Company, People

import json

# Import data once for the tests
def setUpModule():
    call_command('import_company', 'resources/companies.json')
    call_command('import_people', 'resources/people.json')


class TestAPI(TestCase): 
    def setUp(self):
        client = Client(SERVER_NAME='localhost')         


    def test_get_existing_company(self):
        result = self.client.get('/v1/api/company/BUGSALL') 
        self.assertEqual(result.status_code, 200) 
        
    def test_get_not_existing_company(self):
        result = self.client.get('/v1/api/company/not_existing_company') 
        self.assertEqual(result.status_code, 404) 


    def test_get_existing_name(self):
        result = self.client.get('/v1/api/people/Moon%20Herring') 
        self.assertEqual(result.status_code, 200) 
        
    def test_get_not_existing_name(self):
        result = self.client.get('/v1/api/people/not_existing_name') 
        self.assertEqual(result.status_code, 404) 

    def test_get_existing_multi(self):
        result = self.client.get('/v1/api/people/Moon%20Herring,Rosemary%20Hayes') 
        self.assertEqual(result.status_code, 200)

        self.assertIsNotNone(result.json()["people"])
        self.assertIsNotNone(result.json()["common"])

    def test_get_not_existing_multi(self):
        result = self.client.get('/v1/api/people/name1,name2') 
        self.assertEqual(result.status_code, 404)