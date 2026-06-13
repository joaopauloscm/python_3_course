CPF = ("956.111.020-26").replace(".","").replace("-","")
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