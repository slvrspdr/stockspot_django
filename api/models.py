from django.db import models

from datetime import datetime

from django_mysql.models import JSONField


class Company(models.Model):
    index = models.IntegerField(default=0, null=False)
    company = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.company


fruit_list = ["orange", "apple", "banana", "strawberry", ]
vegetable_list = ["beetroot", "cucumber", "carrot", "celery"]

class People(models.Model):
    index = models.IntegerField(null=False)
    guid = models.CharField(max_length=100, null=True)
    has_died= models.BooleanField(null=False, default=False)
    balance = models.CharField(max_length=20, null=True)
    picture = models.CharField(null=True, max_length=200)
    age = models.IntegerField(null=True)
    eyeColor = models.CharField(null=True, max_length=20)
    name = models.CharField(null=False, max_length=100)
    gender = models.CharField(null=True, max_length=20)
    company_id = models.IntegerField(null=False, default=0)
    email = models.CharField(null=True, max_length=200)
    phone = models.CharField(null=True, max_length=20)
    address = models.CharField(null=True, max_length=255)
    about = models.CharField(null=True, max_length=1000)
    registered = models.DateTimeField(null=False, default = datetime.utcnow)
    tags = JSONField()
    friends = JSONField()
    greeting = models.CharField(null=True, max_length=200)
    favouriteFood = JSONField()

    def __str__(self):
        return self.name


    @staticmethod
    def get_one(name):
        try:
            person = People.objects.get(name=name)
            data = {
                "username":person.name,
                "age": person.age,
                "fruits": [f for f in person.favouriteFood if f in fruit_list], 
                "vegetables": [v for v in person.favouriteFood if v in vegetable_list]
            }
            return data
        except:
            return None
    
    @staticmethod
    def get_multi(name_list):
        people = []
        common = []

        people_qs = People.objects.filter(name__in=name_list)
        if people_qs:
            first = True
            common_friends = []
            for p in people_qs:
                people.append({"name":p.name, "age":p.age, "address":p.address, "phone":p.phone})

                friends = list(map(lambda x: x["index"], p.friends))
                if first:
                    common_friends = friends
                else:
                    common_friends = [f for f in friends if f in common_friends]
                
                first = False

            common_qs = People.objects.filter(index__in=common_friends, eyeColor="brown", has_died=False)
            if common_qs:
                for p in common_qs:
                    common.append({"name":p.name, "age":p.age, "address":p.address, "phone":p.phone})

        if people:
            return { "people":people, "common":common }
        else:
            return None

