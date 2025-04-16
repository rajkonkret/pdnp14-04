# '{"name":"John", "age":30, "car":null}'
# dane typu klucz-wartosc
# uzywany do komunikacji miedzy systemami w internecie
# odpowiednikiem json ajest słownik

import json

person_dict = {'name': "Radek", 'age': 40, "czy_pali": None}
# {"name": "Radek", "age": 40, "czy_pali": null}
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortuje po kluczach
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as f:
    data = json.load(f)

print(data)
print(type(data))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>

print(data['name'])  # Radek

json_text = json.dumps(data)
print(json_text)
print(type(json_text))
# {"age": 40, "czy_pali": null, "name": "Radek"}
# <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
