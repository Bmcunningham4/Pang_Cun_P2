# Exercise: Create a Task Manager!

class Task: 
    def __init__(self, title, description, completed=0, priority=0):
        self.title = title
        self.description = description 
        self.completed = completed # 0 = no conplete, 1 = complete
        self.priority = priority   # 0 - 5: least priority to top priority

class TaskManager:
    def __init__(self):
        self.task_list = []
    
    def add_task(self, new_task):
        self.task_list.append(new_task)

    def display_tasks(self):
        for task in self.task_list:
            status = "Complete" if task.completed == 1 else "Incomplete"
            print(f"Title: {task.title}, Description: {task.description}, Status: {status}, Priority: {task.priority}") # This line here has fixed my code!
            # print(task) = This would just print the instance of the object in form: <__main__.Task object at 0x100da1a00>

    def complete_task(self, title):
        for task in self.task_list:
            if task.title == title:
                task.completed = 1

    def remove_task(self, title):
        for task in self.task_list:
            if task.title == title:
                self.task_list.remove(task)

    def display_incomplete(self):
        print("Here are your incomplete tasks: ")
        for task in self.task_list:
            if task.completed == 0:
                print(f"Title: {task.title}, Description: {task.description}, Priority: {task.priority}")


task_manager1 = TaskManager()

# Menu
while True:
    try:
        user_input = int(input(("""Hi welcome to your personal Task Manager!
      
        Please select from the following options:
        - To add a task press (1)
        - To display all tasks press (2)
        - To mark a task as completed press (3)
        - To remove a task press (4)
        - To Display only incomplete tasks press (5)
      
        if you would like to exit please press (0)
""")))
    
        if user_input == 0:
            break

        elif user_input == 1:
            user_title = input("What is the title of the task you would like to add? ")
            user_description = input("What are the details of the task? ")
            user_complete = int(input("Is this task complete? (1 for yes, 0 for no) "))
            user_priority = int(input("What is the priority of this task out of 5, 5 being the highest priority? "))

            user_task = Task(user_title, user_description, user_complete, user_priority)
            task_manager1.add_task(user_task)

        elif user_input == 2:
            task_manager1.display_tasks()

        elif user_input == 3:
            user_title2 = input("What is the title of the task you would like to complete? ")
            task_manager1.complete_task(user_title2)

        elif user_input == 4:
            user_title3 = input("What is the title of the task you would like to remove? ")
            task_manager1.remove_task(user_title3)
        
        elif user_input == 5:
            task_manager1.display_incomplete()
        else:
            print(f"Sorry {user_input} is not a valid input, chose again fool!", '\n')
        
    except ValueError:
        print(f"{user_input} is not valid try again!")
    



print("Thanks for using your Fancy To Do list, please come again!")

# Practice calling
    # task_manager1 = TaskManager()

    # task1 = Task("King", "Get shit done", 0, 5)
    # task_manager1.add_task(task1)
    # task_manager1.display_incomplete()            



# I'm a goat have a look at this when I come back almost there!!!!