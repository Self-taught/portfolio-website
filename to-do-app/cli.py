from functions import get_todos, write_todos
import time

print(time.strftime("%A %d %b %y"))

while True:
    user_action = input("Type add, show, edit, complete or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip("\n").title()
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            new_todo = input('Enter a new todo. ') + "\n"
            todos = get_todos("todos.txt")
            todos[number] = new_todo

            write_todos("todos.txt", todos)

        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = get_todos("todos.txt")
            to_pop = todos[number].strip('\n')
            todos.pop(number)

            write_todos("todos.txt", todos)

            message = f"Todo {to_pop} was removed from the list!"
            print(message)
        except IndexError:
            print("Item doesn't exist!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid!")

print("Bye")