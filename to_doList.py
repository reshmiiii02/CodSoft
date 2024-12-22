def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append({"task": task, "done": False})
            print("Task added!")
           
        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks in the list.")
            else:
                for i in range(len(tasks)):
                    task = tasks[i]
            if task["done"]:
                status = "Done"
            else:
                status = "Not Done"
            print(f"{i + 1}. {task['task']} - {status}")


        elif choice == '3':
            task_number = int(input("Enter task number to mark as done: "))
            tasks[task_number - 1]["done"] = True
            print("Task marked as done!")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

#if __name__ == "__main__":
    main()
