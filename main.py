from datetime import date 

def showMenu () :
    print("""choose what you want to do : \n
          1. add a task \n 
          2. remove a task \n 
          3. finishing task\n
          4. show all tasks\n 
          5. remove all done \n""")


def showAllTasks (tasks) :
    if len(tasks) == 0 :
        print("""
              TASKS :
              there is nothing to do ! \n""")
    else :
        number = 1
        for task in tasks :
            description = task.get("description")
            status = "◼" if task.get("status") else "◻"
            finishingTime = date.today() if task.get("status") else " "
            print(f"{status}⸽ {number} : {description} ⸽ {finishingTime}")
            number +=1


def removeAllDones (tasks) :
    for task in tasks[:] :
        if task["status"] :
            tasks.remove(task)
    print("Done")


def addTask (tasks) :
    runAdding = True
    print("enter 'x' if you are finished !")
    while runAdding :
        taskDescription = input("enter task description : ")
        if taskDescription == "x" :
            runAdding = False
            continue
        task = {
            "description" : taskDescription ,
            "status" : False 
        }
        tasks.append(task)
    print("task adding done !\n")


def removeTask (tasks):
    print("enter '0' if you are finished !")
    runRemoving = True
    while runRemoving :
        choice = int(input("which number do you want to remove ? : "))
        if choice == 0 :
            runRemoving = False
            continue
        elif 1 <= choice <= len(tasks): 
                for i, task in enumerate(tasks) :
                    if choice == i + 1 :
                        tasks.pop(i)
                        break
        else :
                print("please select a valid number")
    print("Done")


def finishingTask (tasks):
    print("enter '0' if you are finished !")
    runDoning = True
    while runDoning :
        choice = int(input("which one : "))
        if choice == 0 :
            runDoning = False
            continue
        elif 1<= choice <= len(tasks):
            for i , task in enumerate(tasks) :
                if choice == i + 1 :
                    task["status"] = True
                    break
        else:
            print("enter a valide number")
    print("Done")




def main():
    run = True
    tasks = []
    while run:
        showAllTasks(tasks)
        showMenu()
        selection = input("select a number : ")
        try :
            match int(selection) :
                case 1 :
                    addTask(tasks)
                case 2 :
                    removeTask(tasks)
                case 3:
                    finishingTask(tasks)
                case 4 :
                    continue
                case 5 :
                    removeAllDones(tasks)
                case _ :
                    print(" it's not a valid choise ! \n")

        except ValueError :
            print("we need a number from 1 to 5 !")

main()
