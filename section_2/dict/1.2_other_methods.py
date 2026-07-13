# person= {
# 'Name': 'Joao Paulo',
# 'Last Name': 'Pereira Santana',
# 'age': '21',

# }
# person.setdefault("age", 0)
# print(person['age'])


# # print(len(person))
# # print((list(person.keys())))
# # print((list(person.values())))
# #print((list(person.items())))

# # for key, value in person.items():
# #     print(key,value)

# #shallow copy
# dic1 = {
#     'k1':"1",
#     'k2':"2",
#     'k3':"3"
# }

# dic2 = dic1.copy()

# dic2 ['k1']=1000

# print (dic1)
# print (dic2)

p1= {
'Name': 'Joao Paulo',
'Last_Name': 'Pereira Santana',
'age': '21',

}
# print(p1.get('Name'))
# Name = p1.pop('Name')
# print(p1)

# last_key = p1.popitem()
# print(p1)

# p1.update({
#     'Name': 'Leo',
#     'age': '39',

# })
# print(p1)
p1.update(Name="Leo" ,Last_Name="Andrés Messi",age =39)
print(p1)