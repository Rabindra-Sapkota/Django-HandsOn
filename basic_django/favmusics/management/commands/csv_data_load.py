from csv import DictReader
from datetime import datetime
from typing import Any, Optional

from django.core.management import BaseCommand
from favmusics.models import Customer, Music
from pytz import UTC


DATE_FORMAT = '%Y-%m-%d'
MUSCIAN_SET = { 'Eminem', 'Nursat Ali Khan', 'Sakira', 'Raju Lama', 'Fatteman', 'Ram Krishna Dhakal' }


class Command(BaseCommand):
    help = "Loads data from sample_data.csv into database"

    def handle(self, *args: Any, **options: Any) -> None:
        if Customer.objects.exists() or Music.objects.exists():
            print("Data Already exists in database. Exiting script")
            return
        
        print("Loading Musician Data")
        
        for musician in MUSCIAN_SET:
            musician_obj = Music(name=musician)
            musician_obj.save()
        
        print("Musician Data Loaded")
        print("Loading Customers Data")

        for row in DictReader(open('./sample_data.csv')):
            customer = Customer()
            customer.name = row['CustomerName']
            customer.address = row['Address']
            raw_dob = row['Date of Birth']
            dob = UTC.localize(datetime.strptime(raw_dob, DATE_FORMAT))
            customer.dob = dob
            customer.gender = 'M' if row['Gender'] == 'male' else 'F'
            customer.save()
            print("Customer Data Loaded")

            raw_musician = row['FavouriteMusics']

            if not raw_musician:
                continue

            print("Adding musician")
            musician_list = [ name.strip() for name in raw_musician.split('|') ]
            for musician in musician_list:
                # Explore get_or_create two avoid two iteration of insert
                musician_obj = Music.objects.get(name=musician)
                customer.music.add(musician_obj)
            
            customer.save()
            print("Musician Added")
