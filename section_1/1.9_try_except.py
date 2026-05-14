# try: tries to run the code
#except : something happens when the code was runned 

ask_number = input('Please type a number! ')


try:
    int_number = int(ask_number)
    print(int_number * 2)

except:
    print("Please type a valid number")
