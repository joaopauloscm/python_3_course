# more practice on enumerate and for 
# ex1
# numbers = [10, 20, 30, 40]
# total = 0
# for number in numbers:
#     total += number 

# print(total)
# ex 2
# string = '12345'
# total = 0


# for digit in (string):
#     total += int(digit)

# print(total)

# #ex 3
# fruits = ['Banana', 'apple','grape' ]

# for index, fruit in enumerate(fruits):
#     print(index,fruit)


#ex 4
# grades = [8,5,9,3,7]

# for index, grade in enumerate(grades):
#     if grade > 7:
#         print(grade,index)

#ex 5 
# digits = "123456789"
# counter = 10
# total = 0

# for digit in digits:
#     total += int(digit) * counter
#     counter -= 1

# print(total)

#ex 6 
# digits = "123456789"
# total = 0

# for index, digit in enumerate(digits):
#     total += int(digit) * (10 - index)

# print(total)

#ex 7 
# letters= ["P", "Y", "T", "H", "O", "N"]
# full_word = ''

# for letter in letters:
#    full_word += letter

# print(full_word)

#ex 8 
students = ["Ana", "Bruno", "Carla", "Davi"]
for index, student in enumerate(students):
    status = "first in list" if index == 0 else "in list"
    print(f"{index} - {student} - {status}")
   




# name_list = ['mary','john','angelo']

# for index, name in enumerate(name_list):
#     print(f"{index} - {name}")
