# To-do list 

to_do_list = []

while True:
    ask_user_wish = input(
        "\nWhat you wish do to? [I]nsert task, [R]emove task, [D]isplay your current list "
        "[M]ark as done or [E]xit ").upper()
    
    if ask_user_wish == 'D':
        if len(to_do_list) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nCurrent to-do list: ")
            for index, item in enumerate(to_do_list):
                print(f"{index} - {item}")


    elif ask_user_wish == 'I':
        ask_task = input("What task you want to add? ")
        to_do_list.append(f'You added: {ask_task}')
        
    elif ask_user_wish == 'M':
        ask_to_done = input(f"Which task you wish to mark as done? {to_do_list} ")
        if ask_to_done == index or item:
            to_do_list.remove(ask_to_done) and to_do_list.insert 


        
    elif ask_user_wish == 'R':
        ask_to_remove = input("Which task you wish to remove ")
        if ask_to_remove in to_do_list:
            to_do_list.remove(ask_to_remove)



    elif ask_user_wish == 'E':
        exit()