
# # Even or Odd

try:
    ask_user_number = int(input('Tell me an INT number! '))
    
        
except:
    ask_user_number = float 
    print ("Your number is not an INT ")
    exit()



divisible_by_two = ask_user_number % 2 == 0



if divisible_by_two:
    print ("Your number is even! ")
else:
    print ("Your number is odd! ")

    


# # What time is it 

ask_user_time = int(input("Hello What time is it? "))


if ask_user_time >= 0 and ask_user_time <= 11:
    print ("Good Morning ")

elif ask_user_time >= 12 and ask_user_time <= 17:
    print ("Good afternoon ")

else:
    print("Good night")


ask_user_name = input("Whats your name? ")
name_size = len(ask_user_name)

if name_size <=4:
    print("Your name is short! ")

elif name_size >=5 and name_size <=6:
    print("Your name is medium! ")

else:
    print("Your name is too long! ")




#mini calculator 

while True:
    start_or_exit = input("Type 'C' to continue or 'E' to exit: ")

    if start_or_exit == 'E':
        break

    if start_or_exit != 'C':
        print("Invalid option")
        continue

    ask_first_number = int(input("Tell me a number: "))
    ask_operator = input("Now tell me a math operator (+, -, /, *): ")
    ask_second_number = int(input("Tell me a second number: "))

    if ask_operator == '+':
        print(f'Your result is: {ask_first_number + ask_second_number}')
    elif ask_operator == '-':
        print(f'Your result is: {ask_first_number - ask_second_number}')
    elif ask_operator == '/':
        print(f'Your result is: {ask_first_number / ask_second_number}')
    elif ask_operator == '*':
        print(f'Your result is: {ask_first_number * ask_second_number}')
    else:
        print("Invalid operator")