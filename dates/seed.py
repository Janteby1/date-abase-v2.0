import csv 
from dates.models import Dates 

with open("dates/seed.txt", encoding='latin-1') as f:
    reader = csv.reader(f, delimiter="\t")
    # header = reader.next()
    for row in reader:
        print (row)
        _, created = Dates.objects.get_or_create(
            place = row[0],
            category = row[1],
            address = row[2],
            area = row[3],
            state = row[4],
            phone = row[5],
            website = row[6],
            parking = row[7],
            price = row[8],
            maps = row[9],
            notes = row[10],
            )
        
    


