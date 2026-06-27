"""
TodoList Application

A command-line todo list manager that allows users to:
- Add tasks
- Remove tasks
- Mark tasks as complete
- View all tasks
- Remove completed tasks
"""

from datetime import date
import json

def get_data_from_file():
    with open("data.json" , "r", encoding="utf-8") as file :
        data = json.load(file)
        return data

def write_data_to_file(data):
    with open("data.json" , "w", encoding="utf-8") as file :
        json.dump(data,file)


def show_menu():
    print("""choose what you want to do : \n
          1. add a task \n 
          2. remove a task \n 
          3. finishing task\n
          4. remove all done \n""")


def show_all_tasks(tasks):
    if len(tasks) == 0 :
        print("""
              TASKS :
              there is nothing to do ! \n""")
    else :
        number = 1
        for task in tasks :
            title = task.get("title")
            status = "◼" if task.get("status") else "◻"
            finishing_date = date.today() if task.get("status") else " "
            print(f"{status}⸽ {number} : {title} ⸽ {finishing_date}")
            number +=1


def remove_all_done(tasks):
    for task in tasks[:] :
        if task["status"] :
            tasks.remove(task)
    write_data_to_file(tasks)
    print("Done")


def add_task(tasks):
    run_adding = True
    print("enter 'x' if you are finished !")
    while run_adding :
        task_title = input(" task title : ")
        if task_title == "x" :
            run_adding = False
            continue
        task = {
            "title" : task_title ,
            "status" : False 
        }
        tasks.append(task)
        write_data_to_file(tasks)
    print(" TASKS ADDED !\n")

def remove_task(tasks):
    run_removing = True
    choice_input = input("list of removes separated by , : ")
    while run_removing :
        
        if choice_input.strip() == "0" :
            run_removing = False
            break
        
        try :
            choices = [int(x.strip()) for x in choice_input.split(",")]
            choices.sort(reverse=True)
            for choice in choices:
                if 1 <= choice <= len(tasks):
                    tasks.pop(choice - 1)
                else:
                    print(f"Invalid number: {choice}")
                    break
                run_removing = False
            write_data_to_file(tasks)
            print("Tasks removed!")
                
        except ValueError:
            print("Please enter numbers separated by commas (e.g., 1,2,3)")
            choice_input = input("list of removes separated by , : ")
    print("Done")

def finishing_task(tasks):
    run_doing = True
    choice_input = input("list of done separated by , : ")
    while run_doing :
        
        if choice_input.strip() == "0" :
                run_doing = False
                continue
            
        try:
            choices = [int(x.strip()) for x in choice_input.split(",") ]
            choices.sort(reverse=True)
            for choice in choices:
                if 1 <= choice <= len(tasks):
                   tasks[choice-1]["status"] = True
                else:
                    print(f"Invalid number: {choice}")
                    break
                run_doing = False
                   
            write_data_to_file(tasks)
            print("Tasks done!")
                
        except ValueError:
            print("Please enter numbers separated by commas (e.g., 1,2,3)")
            choice_input = input("list of done separated by , : ")
    print("Done")


def main():
    run = True
    while run:
        data = get_data_from_file()
        show_all_tasks(data)
        show_menu()
        selection = input("select a number : ")
        try :
            match int(selection) :
                case 1 :
                    add_task(data)
                case 2 :
                    remove_task(data)
                case 3:
                    finishing_task(data)
                case 4 :
                    remove_all_done(data)
                case _ :
                    print(" it's not a valid choise ! \n")

        except ValueError :
            print("we need a number from 1 to 5 !")

main()
