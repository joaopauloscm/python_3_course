if 10 > 5:
    print ('10 is greater than 5')

ask_number_1 = int(input("Give me a number "))
ask_number_2 = int(input("Give me a second number "))

if ask_number_1 > ask_number_2:
    print (f'{ask_number_1} is greater than {ask_number_2}')

elif ask_number_1 == ask_number_2:
    print (f'{ask_number_1} is equal to {ask_number_2}')

else:
     print (f'{ask_number_1} is less than {ask_number_2}')
