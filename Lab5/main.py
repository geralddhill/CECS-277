# Names: Gerald Hill, Hoang Do
# Date: 9/23/24
# Desc: A simple, editable task list

import check_input
import task


def main_menu():
    ''' Display the main menu and return the user's valid input

    Arg: None
    
    Returns: The user's valid input 
    '''
    
    
    print("1. Display Current Task")
    print("2. Mark current task complete")
    print("3. Postpone current task")
    print("4. Add new task")
    print("5. Save and quit ")
    choice = check_input.get_int_range("Enter your choice: ", 1, 5)

    return choice



def read_file():
    """ Reads in tasks from file

    Args: None

    Returns: List of tasks
    """
    # Reads file
    f = open("tasklist.txt", "r")
    lines = f.readlines()
    f.close
    
    # Iterates through file and adds task to list
    tasks = []
    for line in lines:
        new_line = line.strip()
        desc, date, time = new_line.split(',')
        tasks.append(task.Task(desc, date, time))

    return tasks



def write_file(tasklist):
    ''' Writes updated tasklist to file

    Args:
        - tasklist: list of tasks (using task class)

    Returns: Nothing
    '''
    f = open("tasklist.txt", "w")

    # Writes individual tasks to file using repr()
    for task in tasklist:
        f.write(repr(task) + '\n')

    f.close()



def get_date():
    ''' Prompts user for date, validates input, and returns date as string

    Args: None

    Returns: Date as string
    '''
    # Gets input from user
    month = check_input.get_int_range("Enter month: ", 1, 12)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 2100)

    # Formats month and day correctly
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    
    return str(month) + '/' + str(day) + '/' + str(year)



def get_time():
    ''' Prompts user for time, validates input, and returns time as string

    Args: None

    Returns: Time as string
    '''
    # Gets input from user
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    minute = check_input.get_int_range("Enter minute: ", 0 ,59)

    # Formats hour and minute correctly
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    
    return str(hour) + ':' + str(minute)



def main():
    ''' Reads and updates tasklist based on user input
    '''
    # Reads tasks from file
    tasklist = read_file()
    # Sorts tasklist
    tasklist.sort()
    menu_input = 0

    while menu_input != 5:
        print("-Tasklist-")
        print("You have", len(tasklist), "tasks.")
        menu_input = main_menu()

        # Displays soonest task
        if menu_input == 1:
            if len(tasklist) < 1:
                print("Tasklist is empty.")
                continue
            print("Current task is:")
            print(tasklist[0])
        # Marks first task as complete and pops it from the list
        elif menu_input == 2:
            if len(tasklist) < 1:
                print("Tasklist is empty.")
                continue
            print("Marking current task as complete:")
            print(tasklist[0])
            tasklist.pop(0)
            if len(tasklist) > 0:
                print("New current task is:")
                print(tasklist[0])
            else:
                print("No new task.")
        # Allows user to enter new due date for the first task
        elif menu_input == 3:
            if len(tasklist) < 1:
                print("Tasklist is empty.")
                continue
            print("Postponing task:")
            print(tasklist[0])
            print()
            print("Enter new due date:")
            date = get_date()
            print("Enter new time:")
            time = get_time()
            desc = tasklist[0].get_description()
            tasklist[0] = task.Task(desc, date, time)
            tasklist.sort()
        # Asks user for input and appends to tasklist (and resorts list)
        elif menu_input == 4:
            desc = input("Enter a task: ")
            print("Enter due date:")
            date = get_date()
            print("Enter time:")
            time = get_time()
            tasklist.append(task.Task(desc, date, time))
            tasklist.sort()
            print()
        elif menu_input == 5:
            print("Saving and exiting.")
            write_file(tasklist)
        else:
            "Error in menu input!" # This should never occur





main()

