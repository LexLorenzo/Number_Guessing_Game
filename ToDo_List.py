def print_options():
    print("Here are the available features of this program.")
    for i in range(len(options)):
        print(i + 1, options[i])
    print()


def print_tasks():
    print("These are your current tasks:")
    for i in range(len(tasks)):
        print("{}. {}".format(i + 1, tasks[i]))
    print()


options = ("Show my tasks.", "Add a task.", "Update a task.", "Mark task as done.", "Save tasks in a file.",
           "Load tasks from a file.", "Stop the program.")
tasks = []

print_options()
ans = int(input("Enter the number of the process that you would like done: "))

while ans != 7:
    if ans == 1:
        if len(tasks) != 0:
            print_tasks()
        else:
            print("You currently have no tasks.")
    elif ans == 2:
        add = input("Enter the tsk that you would like to be added to your ToDo list: ")
        tasks.append(add)
    elif ans == 3:
        print_tasks()
        upd = int(input("Select the task that you would like to update: "))
        tasks.pop(upd - 1)
        new = input("Enter a new input for this task: ")
        tasks.insert(upd - 1, new)
    elif ans == 4:
        print_tasks()
        done = int(input("Select the task that you would like to be marked as done: "))
        print("Task '{}' is now marked as done and will be removed from your tasks.".format(tasks[done - 1]))
        tasks.pop(done - 1)
    elif ans == 5:
        save = open("Save_Tasks.txt", 'w')
        save.write("These are your current tasks:\n")
        for i in range(len(tasks)):
            save.write("{}. {}\n".format(i + 1, tasks[i]))
        print("Successfully saved your task in a new file.")
        save.close()
    elif ans == 6:
        load = open(input("Enter the name of you load file: "), 'r')
        load.readline()
        for data in load:
            tasks.append(data[2:len(data) - 1])
        print("Successfully loaded your saved tasks.")
        load.close()
    else:
        print("Please enter only an integer within the range of the available options.")
    print()
    print_options()
    ans = int(input("Enter the number of the process that you would like done: "))
