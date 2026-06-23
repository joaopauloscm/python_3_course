# def salutation(name):
#     print(f"Hello! {name}")

# salutation("Joao")

# def area(base,height):
#     return base * height 

# result = area(2,5)
# print (result)

# def exponentiation(base,exponent=2):
#     return base**exponent

# result_exponentiation = exponentiation(10)
# print (result_exponentiation)

def avg_grades(*grades):
    total = 0                      # acumulador começa em 0, DENTRO da função
    for grade in grades:           # percorre cada nota da tupla
        total += grade             # total cresce: total = total + grade
    final_grade = total / len(grades)   # soma dividida pela quantidade
    return final_grade             # devolve a média

print(avg_grades(8, 9, 10))        # 9.0

    