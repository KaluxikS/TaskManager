import task_manager as tm


def print_menu():
    print("Menu:")
    print("1. Add new task")
    print("2. Display tasks")
    print("3. Search tasks by title or description")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Exit")


def get_menu_choice():
    choice = input("Choose an option: ")
    return choice


def main():
    connection = tm.create_connection()
    tm.create_table(connection)

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == "1":
            tm.add_task(connection)
        elif choice == "2":
            answer = input("Do you want to sort the results? (y/n): ")

            if answer == "y":
                sort_by = input("Enter the sorting parameter (title, status, priority, created_at): ")
                filter_by_status = input("Enter the status to filter by (optional:"
                                         " \"to do\", \"in progress\", \"completed\"): ")
                tm.display_tasks(connection, sort_by, filter_by_status=filter_by_status)
            else:
                filter_by_status = input("Enter the status to filter by (optional:"
                                         " \"to do\", \"in progress\", \"completed\"): ")
                tm.display_tasks(connection, filter_by_status=filter_by_status)
        elif choice == "3":
            query = input("Enter a word to search in titles and descriptions: ")
            tm.search(connection, s=query)
        elif choice == "4":
            id = int(input("Enter the task ID to update: "))
            tm.edit_task(connection, id=id)
        elif choice == "5":
            id = int(input("Enter the task ID to delete: "))
            tm.delete_task(connection, id=id)
        elif choice == "6":
            break
        else:
            print("Invalid option")

    connection.close()
    print("Application terminated")


if __name__ == "__main__":
    main()
