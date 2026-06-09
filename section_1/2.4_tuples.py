# Unpacking and Tuples
# name1, name2, name3, = name_list = ['Joao', 'Ellen','Matthew']
# print (name1)

name1,*_ = name_list = ['Joao', 'Ellen','Matthew']
print (name1, _)

#Tuple
tuple_example = 'AAA', 123,True
#convert to list tuple_example = list(tuple_example)
print (tuple_example)