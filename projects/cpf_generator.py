# First digit calculus 
CPF = ("746.824.890-70").replace(".","").replace("-","")
CPF_size = len(CPF[0:9])

i = 0
j = 10
first_digit = 0          # <-- o acumulador nasce AQUI, fora do loop, zerado

while i < CPF_size:
    first_digit += int(CPF[i]) * j   # <-- += acumula; só a multiplicação
    i += 1
    j -= 1



first_digit *= 10 
first_digit %= 11


first_digit = 0 if first_digit > 9 else first_digit 

print(f"Your first CPF digit is: {first_digit}")


# second digit calculus 
ten_digits = CPF[0:9] + str(first_digit)
ten_digits_size = len(ten_digits)



i = 0
j = 11
second_digit = 0          # <-- o acumulador nasce AQUI, fora do loop, zerado

while i < ten_digits_size:
    second_digit += int(ten_digits[i]) * j   # <-- += acumula; só a multiplicação
    i += 1
    j -= 1


second_digit *= 10 
second_digit %= 11



second_digit = 0 if second_digit > 9 else second_digit

print(f"Your second CPF digit is: {second_digit}")