import csv
from app.models import Disease #Change App Name

with open('D://Users/Desktop/isa/covid.csv') as csvfile:   #Change file location
	reader=csv.DictReader(csvfile)
	for row in reader:
			p = Disease(country=row['country'],total_cases=row['total cases'],total_deaths=row['total deaths'],total_recovered=row['total recovered'],active_cases=row['active cases'])
			p.save()
