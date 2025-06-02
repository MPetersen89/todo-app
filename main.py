# from functions import get_todos, write_todos
import functions

while True:
    # Getting user inputs and removing spaces from the inputs
    user_action = input("ADD a to-do, SEE your list, EDIT your list, COMPLETE an item, or DONE?")
    user_action = user_action.lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.title() + '\n')

        functions.write_todos(todos)   ## order matters here: may also use (filepath="todos.txt", todos_arg=todos). But since filepath is defined in the function, no need for it here.

    elif user_action.startswith("see"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # for item in todos:
        #     item = item.strip('\n')

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}) {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            edit = input("What would you like to change it to?")
            todos[number] = edit + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Sorry, that is not a valid command.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"{todo_to_remove} has been completed. Way to go!")
        except IndexError:
            print("Sorry, there isn't a to-do with that number.")
            continue

    elif user_action.startswith("done"):
        break


    else:
        print("Invalid command. What would you like to do?")

