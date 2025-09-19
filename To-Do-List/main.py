def main():
    print("Welcome to the To-Do List application! \n")
    

    to_do_list = [] # Initialize an empty to-do list

    while True:
        print("\n----Menu----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Select an option: ")
        
        if choice == '1':
           task_num = input("Enter the task number: ")
           for i in range(task_num):
               task = input(f"Enter Task {i+1}: ")
               to_do_list.append({"Task": task, "completed": False})
               print(f"✅ Task '{task}' added.")

        elif choice == '2':
              if not to_do_list:
                print("\n📌 No tasks found!")
              else:
                print("\nYour Tasks:")
                for index, task in enumerate(to_do_list, start=1):
                 status = "✔ Completed" if task["completed"] else "⏳ Pending"
                 print(f"{index}. {task['Task']} - {status}")
                
        elif choice == '3':
            if not to_do_list:
                print("\n⚠ No tasks to mark!")
            else:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= task_index < len(to_do_list):
                    to_do_list[task_index]["completed"] = True
                    print(f"✅ Task '{to_do_list[task_index]['task']}' marked as completed.")
                else:
                    print("❌ Invalid task number.")

        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()

