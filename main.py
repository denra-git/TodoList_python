
def show_menu () :
    print("""choose what you want to do : \n 
          1. add a task \n 
          2. remove a task \n 
          3. finishing task\n
          4. show all tasks\n 
          5. remove all done \n""")


def show_all_tasks (tasks) :
    if len(tasks) == 0 :
        print("""
              TASKS :
              there is nothing to do ! \n""")
    else :  
        for task in tasks :
            number = tasks.index(task)+1
            description = task.get("description")
            status = "◼" if task.get("status") else "◻"
            print(f"{status}⸽{number} : {description}")
    

def remove_all_dones (tasks) :
    for task in tasks :
        if task["status"] :
            tasks.remove(task)
    print("Done")
      

def add_task (tasks) :
    run_adding = True
    print("enter 'x' if you are finished !")
    while run_adding :
        task_description = input("enter task description : ")
        if task_description == "x" :
            run_adding = False
            continue
        task = {
            "description" : task_description ,
            "status" : False 
        }
        tasks.append(task)
    print("task adding done !\n")


def remove_task (tasks) :
    print("enter '0' if you are finished !")
    run_removing = True
    while run_removing :
        choice = int(input("which number do you want to remove ? : "))
        if choice == 0 :
            run_removing = False
            continue
        for task in tasks:
            if choice == tasks.index(task)+1 :
                tasks.remove(task)
    print("Done")


def finishing_task (tasks) :
    print("enter '0' if you are finished !")
    run_doning = True
    while run_doning :
        choice = int(input("which one : "))
        if choice == 0 :
            run_doning = False
            continue
        for task in tasks :
           if choice == tasks.index(task)+1 :
                task["status"] = True
    print("Done")




def main() :
    run = True
    tasks = []
    while(run):
        show_all_tasks(tasks)
        show_menu()
        selection = int(input("select a number : "))
        match selection :
            case 1 : 
                add_task(tasks)
            case 2 :
                remove_task(tasks)
            case 3:
                finishing_task(tasks)
            case 4 :
                show_menu()
            case 5 :
                remove_all_dones(tasks)
            case _ :
                print(" it's not a valid choise ! \n")
        
main()