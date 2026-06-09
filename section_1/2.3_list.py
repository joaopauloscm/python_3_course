random_list = [123, True, 'joao']
random_list_d = random_list.copy() #copy your list to another one
print (random_list)
random_list[2] = 'paulo'.upper()
del random_list[0] # delete something from your list

random_list.append(10) # insert something at the end of your list
random_list.pop() # remove the last thing you added in your list or something you declared inside()


#random_list.clear  clear everthing
print (random_list)
random_list.insert(0,5)
print (random_list)

random_list_b = [10, 20, 30, 40]

ranmdom_list_c = random_list + random_list_b
print (ranmdom_list_c)

# or extend 
random_list.extend(random_list_b)
print (random_list)

print(random_list_d)

name_list = ['Darius','Garen','Kayle']
for name in name_list:
    print(name)