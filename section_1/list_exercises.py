# Market List

products_bought = []

while True:
    ask_user_input = input(
        "\nWhat do you desire? [I]nsert, [R]emove, [S]how list or [E]xit: "
    ).upper()

    if ask_user_input == 'I':
        ask_user_insert = input("What do you wish to insert? ")
        products_bought.append(ask_user_insert)
        print(f'"{ask_user_insert}" added successfully.')

    elif ask_user_input == 'S':
        if len(products_bought) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nCurrent shopping list:")
            for index, item in enumerate(products_bought):
                print(f"{index} - {item}")

    elif ask_user_input == 'R':
        if len(products_bought) == 0:
            print("Your shopping list is empty.")
            continue

        ask_for_removal = input(
            f'Current list: {products_bought}\nWhat item do you wish to remove? '
        )

        if ask_for_removal in products_bought:
            products_bought.remove(ask_for_removal)
            print(f'"{ask_for_removal}" removed successfully.')
        else:
            print("Item not found.")

    elif ask_user_input == 'E':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose I, R, S or E.")