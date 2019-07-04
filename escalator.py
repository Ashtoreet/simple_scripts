import csv
from datetime import date, datetime


# today = datetime.strptime('01.02.2018', '%d.%m.%Y')
today = datetime.now()
print(today)
with open('metro.csv', 'r', encoding='utf-8') as f:
    fields = [
            'ID', 'Name', 'Longitude_WGS84',
            'Latitude_WGS84', 'NameOfStation',
            'Line', 'ModeOnEvenDays', 'ModeOnOddDays',
            'FullFeaturedBPAAmount',
            'LittleFunctionalBPAAmount', 'BPAAmount',
            'RepairOfEscalators', 'global_id', 'geoData'
            ]
    reader = csv.DictReader(f, fields, delimiter=';')
    stations = {}


    for row in reader:

        if row['RepairOfEscalators'] is not '':
            dates = row['RepairOfEscalators'].split('-')
            dates = [
                        datetime.strptime(dates[0], '%d.%m.%Y'),
                        datetime.strptime(dates[1], '%d.%m.%Y')
                    ]

            if dates[0] < today and today < dates[1]:
                stations[row['NameOfStation']] = row['RepairOfEscalators']

    if stations:
        for station in stations:
            print(station)
    else:
        print('Empty.')
