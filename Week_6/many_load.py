import csv  
from unesco.models import Category, State, Iso, Region, Site


def run():

    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()


    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        sta, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        nam = row[0]

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            lon = float(row[4])
        except:
            lon = None

        des = row[1]

        jus = row[2]

        try:
            ar = float(row[6])
        except:
            ar = None


        site = Site(name=nam, description=des, justification=jus, year=y,
        longitude=lon, latitude=lat, area_hectares=ar, category=cat, state=sta,
        region=reg, iso=iso)
        site.save()


