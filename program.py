def showMenu():
    print("\n\n1.   View tasks.")
    print("2.   Add tasks.")
    print("3.   Remove tasks.")
    print("4.   Update tasks.")
    print("5.   Clear all tasks.")
    print("6.   Exit tasks.")

def loadTasks():
    try:
        with open('taskslist.txt','r') as f:
            tasks=[line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks=[]
    return tasks

def saveNewTask(t):
    try:
        with open('taskslist.txt','a') as f:
            f.write(t+'\n')
            print("content added")
    except FileNotFoundError:
        with open('taskslist.txt','w') as f:
            f.write(t+'\n')
            print("file created and content added")

def saveTasks(tasks):
    
    with open('taskslist.txt','w') as f:
        for task in tasks:
            f.write(task+'\n')

def main():
    print("\n\n********** TO-DO LIST **********")
    
    while True:
        showMenu()
        choice=input("\n\nEnter your choice:    ")
        task=loadTasks()
        if choice=='6':
            print("\nExited.")
            break
        elif choice=='1':
            if not task:
                print("Empty File")
            else:
                print("\n"*3)
                print("The tasks are listed below:")
                for i,t in enumerate(task,start=1):
                    print(f"{i}. {t}")
                
        elif choice=='2':
            newtask=input("\nEnter the new task to add:\t")
            saveNewTask(newtask)
        elif choice=='3':
            if not task:
                print("\nEmpty File.")
            else:
                for i,taskValue in enumerate(task,start=1):
                    print(f'{i}. {taskValue}')
                index=int(input("\nEnter the index number of the item to remove:\t"))-1
                if 0<=index<len(task):
                    removedItem=task.pop(index)
                    saveTasks(task)
                    print(f"The value \"{removedItem}\" is removed.")
                else:
                    print("Invalid index number. ")

if __name__=="__main__":
    main()