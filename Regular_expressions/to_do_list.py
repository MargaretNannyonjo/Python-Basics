task_list = []

def to_do_list():
    print("THE TO-DO LIST")
    print()
    while True:  
        action = input("Do you want to add, delete, view tasks, or exit? ")

        if action.lower() == "add":
            task = input("ADD TASK: ")
            if task not in task_list:
                task_list.append(task)
                print(f"You have successfully added '{task}'")
            else:
                print(f"'{task}' already exists")

        elif action.lower() == "delete":
            task = input("What task do you want to delete? ")
            if task in task_list:
                task_list.remove(task)
                print(f"'{task}' has been successfully deleted")
            else:
                print(f"'{task}' does not exist")

        elif action.lower() == "view":
            if task_list:
                print("Current Tasks:")
                for index, task in enumerate(task_list, start=1):
                    print(f"{index}. {task}")
            else:
                print("The task list is empty")

        elif action.lower() == "exit":
            break  

        else:
            print("Invalid action! Please choose from add, delete, view tasks, or exit.")

to_do_list()
