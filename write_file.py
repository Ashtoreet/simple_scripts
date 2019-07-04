import csv


users_list = [
                {'first_name': 'Gloria', 'last_name': 'Armstrong', 'balance': '8.82'},
                {'first_name': 'Amanda', 'last_name': 'Scott', 'balance': '9.5'}
]


with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'balance']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for i in users_list:
        writer.writerow(i)
        # v = i.keys()
        # for b in v:
        #     print(b, ';', i[str(b)])
        #     writer.writerow(b, i[str(b)])
