import functions as f

option = input('Enter option number: 1. Add, 2. Edit, 3. Mark Complete, '
               '4. show, 5. Exit')
# todo = []

while True:
    match option:
        case '1':
            text = input("Enter the todo to add: ")
            todo = f.readfile()
            todo.append(text + '\n')
            f.writefile(todo)
            print(f"'{text}' is added to the list.")
            print(f"Updated todo list is: \n{[x.strip() for x in todo]}")
            toadd = input("Enter 'y' to continue adding? ")
            if toadd.lower() == 'y':
                continue
            else:
                break

        case '2':
            todo = f.readfile()
            print(f'The list is:'
                  f'{[str(x+1) + ". " + str(y).strip() for x,y in enumerate(todo)]}')
            editoption = int(input("Enter the number to edit: "))
            edittext = input('New todo: ')
            todo.pop(editoption - 1)
            todo.insert(editoption - 1, edittext + '\n')
            f.writefile(todo)
            todo = f.readfile()
            temp = [x.strip() for x in todo]
            print(f'The new list is:{[x.strip() for x in todo]}')
            break

        case '3':
            todo = f.readfile()
            print(f'The list is:'
            f'{[str(x + 1) + ". " + str(y).strip() for x, y in enumerate(todo)]}')
            mark = input("Enter the number to mark complete: ")
            pop = todo.pop(int(mark) - 1)
            print(f"Removed todo: {pop}", end="")
            f.writefile(todo)
            print(f"New List: {[x.strip() for x in f.readfile()]}", end="")
            break

        case '4':
            print(f"Todos are: {[x.strip() for x in f.readfile()]}", end="")
            break

        case "":
            break


