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


    for row in reader:
        if 'Метро' in row['Name']:  # проезд разные улицы
            station_streets.append(row['Name'])

print(station_streets)

#OrderedDict([('ID', '1002257'), ('Name', '«Новоданиловский пр.», Новоданиловский проезд (в центр)'), ('Longitude_WGS84', '37.62238028'), ('Latitude_WGS84', '55.70177114'), ('Street', 'Новоданиловский проезд'), ('AdmArea', 'Южный административный округ'), ('District', 'Донской район'), ('RouteNumbers', 'Тм16'), ('StationName', 'Новоданиловский пр.'), ('Direction', 'в центр'), ('Pavilion', 'нет'), ('OperatingOrgName', ''), ('EntryState', 'активна'), ('global_id', '858355661'), ('geoData', '{type=Point, coordinates=[37.62238028, 55.70177114]}')])
