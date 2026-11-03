import json
import os

print("=============== TASK TRACKER ===============\n")

choice='0'
def display_tasks():
    if not tasks:
        print('No tasks found\n')
    else:
        print('Your Tasks:')
        for index,elt in enumerate(tasks, start=1):
            display_single_task(index,elt)
        print('')

def search_tasks():
    x = input('Enter task to search: ').strip().lower()
    if not x:
        print('Please enter keywords to search a task\n')
    else:
        found=False
        for index,elt in enumerate(tasks, start=1):
            if x in elt['title'].lower():
                found=True
                display_single_task(index,elt)
        if not found:
            print('No matching tasks found.')
        print('')

def display_pending_tasks():
    print('Pending Tasks:')
    found=False
    for index,elt in enumerate(tasks, start=1):
        if not elt['completed']:
            found=True
            display_single_task(index,elt)
    if not found:
        print('No Pending Tasks')
    print('')

def display_completed_tasks():
    print('Completed Tasks:')
    found=False
    for index,elt in enumerate(tasks, start=1):
        if elt['completed']:
            found=True
            display_single_task(index,elt)
    if not found:
        print('No Completed Tasks')
    print('')

def display_single_task(index,elt):
    if not elt['completed']:
        print(f"{index}. {elt['title']} [Pending]")
    else:
        print(f"{index}. {elt['title']} [Completed]")

def edit_tasks():
    if not tasks:
        print('No tasks available to edit.')
    else:
        display_tasks()
        try:
            task_no=int(input('Enter the task number you want to edit: '))
            if task_no>=1 and task_no<=len(tasks):
                new_title= input('Enter the new task title: ').strip()
                if not new_title:
                    print("New task title can't be empty")
                else:
                    duplicate=False
                    for i,task in enumerate(tasks,start=1):
                        if i != task_no: 
                            if new_title.lower()==task['title'].lower():
                                duplicate=True
                                print('This task is already present.')
                                break
                    if not duplicate:
                        tasks[task_no-1]['title']=new_title
                        save_tasks()
                        print('Task edited successfully')
            else:
                print('Invalid task number.')
        except ValueError:
            print('Enter a valid task number.')
    print('')

def task_summary():
    print('\nTASK SUMMARY')
    total_tasks = len(tasks)
    completed_tasks=0
    for elt in tasks:
        if elt['completed']:
            completed_tasks+=1
    pending_tasks = total_tasks - completed_tasks
    print(f'Total tasks: {total_tasks}')
    print(f'Completed tasks: {completed_tasks}')
    print(f'Pending tasks: {pending_tasks}')
    print('')

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks=json.load(file)
    except FileNotFoundError:
        tasks=[]
    except json.JSONDecodeError:
        print('Error: The tasks file contains invalid JSON data.')
        os.rename("tasks.json", "tasks_backup.json")
        tasks=[]

load_tasks()
while choice!='5':
    print('1. Add a task')
    print('2. View all tasks')
    print('3. Mark a task as completed')
    print('4. Delete a task')
    print('5. Exit')
    print('6. View task summary')
    print('7. Search Tasks')
    print('8. View Pending Tasks')
    print('9. View Completed Tasks')
    print('10. Edit Tasks\n')
    choice= input('Enter a choice: ') 

    if choice=='1':
        task = input('Enter your task: ').strip()
        if not task:
            print('Task cannot be empty!\n')
        
        else:
            duplicate=False
            for elt in tasks:
                if task.lower()==elt['title'].lower():
                    duplicate=True
                    print('This task is already present.\n')
                    break

            if not duplicate:
                tasks.append({'title': task, 'completed': False})
                save_tasks()
                print('Task successfully added\n')

    elif choice=='2':
        display_tasks()

    elif choice=='3':
        display_tasks()
        try:
            task_num = int(input('Enter the task number you want to mark as completed: '))
            if task_num >= 1 and task_num <= len(tasks):
                if tasks[task_num-1]['completed']==True:
                    print('This task is already completed\n')
                else:
                    tasks[task_num-1]['completed']=True
                    print('Task marked as completed\n')
                    save_tasks()
            else:
                print('Invalid task number\n')
        except ValueError:
            print('Please enter a valid number.\n')
        

    elif choice=='4':
        display_tasks()
        if tasks:
            try:
                task_del_num = int(input('Enter the task number you want to delete: '))
                if task_del_num >= 1 and task_del_num <= len(tasks):
                    confirm=input('Are you sure you want to delete this task? (y/n): ').strip().lower()
                    if confirm=='y':
                        tasks.pop(task_del_num-1)
                        print('Task deleted successfully\n')
                        save_tasks()
                    elif confirm=='n':
                        print('Task Deletion cancelled\n')
                    else:
                        print('Deletion confirmation failed!\n')
                else:
                    print('Invalid task number\n')
            except ValueError:
                print('Please enter a valid number.\n')
        
    
    elif choice=='5':
        print('Goodbye!')

    elif choice=='6':
        task_summary()

    elif choice=='7':
        search_tasks()

    elif choice=='8':
        display_pending_tasks()

    elif choice=='9':
        display_completed_tasks()

    elif choice=='10':
        edit_tasks()

    else:
        print('Invalid choice. Please try again.')