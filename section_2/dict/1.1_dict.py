# person = {
#     'name' : 'Joao Paulo',
#     'Major': 'Computer Science '
    
# }
# print(person['Major'])


person = {}

key = 'name'

person[key] = 'Joao Paulo'
person['last name'] = "Pereira Santana"

del person['last name']
# print(person.get('last name','Does not exist'))
if person.get('last name') is None:
    print("Does not exist") 


