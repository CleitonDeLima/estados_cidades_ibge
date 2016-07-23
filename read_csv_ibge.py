import csv
import json


# data = {
#     "11": {
#         "name": "Santa Catarina",
#         "cities": {
#             "4204202": "Chapecó",,
#             "9999991": "etc1",
#             ...
#         }
#     },
#     "10": {
#         "name": "São Paulo",
#         "cities": {
#             "3550308": "São Paulo",
#             "9999992": "etc2",
#             ...
#         }
#     }
# }

data = {}

with open('base_ibge.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        code_state = str(row['CodUF'])

        if code_state not in data:
            state_name = str(row['UF']).capitalize()

            data[code_state] = {}
            data[code_state].update(
                dict(
                    name=state_name,
                    cities=dict()
                )
            )

        city_name = str(row['NomeMunic']).capitalize()
        code_city = str(row['Codmundv'])

        data[code_state]['citys'].update(
            {
                code_city: city_name
            }
        )

with open('base_ibge.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
