# (and) everything needs to be true if not everything is false!

# or: if something is true everything else is true 
# if 10 or 5 > 1: print("is greater than 1")

# not: not true = fase 

system_control = input('Do you want to enter or leave the system? ')
password = 6767




if system_control == 'enter':
    ask_password = int(input("Whats the password? "))
    if ask_password == password:
      print ("You entered the system")
    else:
         print('Wrong password!')

elif system_control == 'leave':
  print  ('You left the system')
  


elif system_control != 'enter' or 'leave':
   print("Try again and type either enter or leave! ")

