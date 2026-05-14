#string slicing
# [s:e:j] start, end, jump

example_one = "Hello Joao"
print (example_one[0:5])
example_one = "Hello Joao"


# LEN:character count 
print(len(example_one))

ask_user_name = (input("What's your name! "))

if ask_user_name.isdigit():
    print ("Please type a name made out of letters")
    exit()

ask_user_age =  (input("What's your age! "))

if ask_user_age.isdigit():
    print (f"Your age is {ask_user_age}")
else:
    print("Please type a number")
    exit()


print (f'Your name reversed is: {ask_user_name[::-1]}')

if " " in ask_user_name:
    print (f'Your name has a space')
else:
    print (f'Your name does not have a space')

print (f'Your name has {len(ask_user_name)} letters')

print (f'the first letter of your name is: {ask_user_name[0:1]}')

print (f'the last letter of your name is {ask_user_name[-1:]}')