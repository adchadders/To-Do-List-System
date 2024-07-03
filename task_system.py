from datetime import date
from taskClass import Task
import pickle
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def save_lists(lists):
    with open('lists.pkl', 'wb') as file:
        pickle.dump(lists, file)

def load_lists():
    with open('lists.pkl', 'rb') as file:
       loaded = pickle.load(file)

    return loaded


def view_lists(lists):
    for list in lists:
        print("-------------------------------")
        list.print_info()

def createTask():
    name = input("Name: ")
    description = input("Description: ")
    time_freq  = input("Time/Freq: ")
    deadline = input("Deadline: ")
    return Task(name, description, time_freq, deadline)

def select_list(lists):
    clear_console()
    for index, task in enumerate(lists):
        print(index,"---",task.name,"-",task.description)

    selection = int(input("> "))
    return selection

def get_main_menu_option():
    options = ["Open List","View lists","New list","Delete list","Save and Quit"]

    for index, option in enumerate(options):
        print(index,"----",option)
    
    selection = int(input("Enter nubmer selection: "))

    return options[selection]

def get_edit_list_option():
    options = ["Open Subtask","Change Name", "Change Description", "Change Time", "Change Deadline", "Change Complete", "View Subtasks", "Add subtask", "Delete Sublist"]
    for index,option in enumerate(options):
        print(index,"---",option)
    option = int(input("> "))

    return options[option]

def edit_list(task):
    task.print_info()
    option = get_edit_list_option()
    clear_console()

    if option == "Change Name":
        task.name = input("new name: ")
    
    if option == "Change Description":
        task.description = input("new description")

    if option == "Change Time":
        task.time = input("New Time: ")

    if option == "Change Deadline":
        task.deadline = "new deadline: "

    if option == "Change Complete":
        if task.complete == False:
            task.complete = True

        else: task.complete = False

    if option == "View Subtasks":
        view_lists(task.subtasks)

    if option == "Add subtask":
        new_subtask = createTask()
        task.subtasks.append(new_subtask)

    if option == "Delete Sublist" and task.subtasks != []:
        del(task.subtasks[select_list()])

    if option == "Open Sub Task":
        selected = select_list(task.subtasks)
        task.subtasks[selected] = edit_list(task.subtasks[selected])
        
    return task

def main_menu_operation(option,lists):
    clear_console()
    if option == "View lists":
        view_lists(lists)

    if option == "New list":
        lists.append(createTask())

    if option == "Save and Quit":
        save_lists(lists)
        return lists
    
    if option == "Open List":
        list_index = select_list(lists)
        lists[list_index] = edit_list(lists[list_index])

    if option == "Delete list":
        list_index = select_list(lists)
        del(lists[list_index])
   
    return lists




lists = load_lists()
clear_console()
while True:
    option =  get_main_menu_option()
    print(option)
    lists = main_menu_operation(option,lists)