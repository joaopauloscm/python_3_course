text = "Joao"
for letter in text:
    print(letter)

print("------")

numbers = range(1, 11)

for number in numbers:
    if number == 2:
        print("I'm not going to display 2")
        continue

    print(number)