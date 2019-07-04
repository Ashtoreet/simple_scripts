import csv
from collections import Counter


with open('station.csv', 'r', encoding='utf-8') as f:
    fields = [
                'ID', 'Name', 'Longitude_WGS84',
                'Latitude_WGS84', 'Street', 'AdmArea',
                'District', 'RouteNumbers', 'StationName',
    			'Direction', 'Pavilion', 'OperatingOrgName',
    			'EntryState', 'global_id', 'geoData'
    			]
    reader = csv.DictReader(f, fields, delimiter=',')

    station_streets = []
    metro_station = []


    for row in reader:
        if row['Street'] != 'проезд без названия':  # проезд разные улицы
            station_streets.append(row['Street'])


    street_list = Counter(station_streets)

    print(max(street_list, key=street_list.get))
