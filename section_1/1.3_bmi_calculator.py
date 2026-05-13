#BMI Calculator

ask_name = input("What's your name? ") 
ask_height = 1.70
ask_weight = 85

bmi = ask_weight / (ask_height * ask_height)

print (f'{ask_name} your BMI is: {bmi:.2f}' )
