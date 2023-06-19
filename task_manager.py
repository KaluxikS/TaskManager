import sqlite3
import datetime


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('tasks.db')
        print("Connected to database")
    except sqlite3.Error as e:
        print(e)

    return connection


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title varchar(100) NOT NULL,
                        description varchar(250),
                        status varchat(30) NOT NULL,
                        priority INTEGER,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                """)
        connection.commit()
        print("Table created")
    except sqlite3.Error as e:
        print(e)


def add_task(connection):
    title = input("Enter the new task title: ")
    description = input("Enter the new task description: ")

    while True:
        priority = input("Enter the priority: ")
        if not priority.isdigit():
            print("Invalid priority. Please enter an integer.")
        else:
            break

    try:
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "to do"
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tasks (title, description, status, priority, created_at) VALUES (?, ?, ?, ?, ?)",
                       (title, description, status, priority, created_at))
        connection.commit()
        print("Task added")
    except sqlite3.Error as e:
        print(e)


def display_tasks(connection, sort_by=None, filter_by_status=None):
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM tasks"

        if filter_by_status in ["to do", "in progress", "completed"]:
            query += f" WHERE LOWER(status) = LOWER('{filter_by_status}')"

        if sort_by in ["title", "status", "priority", "created_at"]:
            print(sort_by)

            if sort_by == "title":
                query += " ORDER BY title"
            elif sort_by == "status":
                query += " ORDER BY status"
            elif sort_by == "priority":
                query += " ORDER BY priority"
            elif sort_by == "created_at":
                query += " ORDER BY created_at"
            else:
                print("Invalid sorting criterion.")
                return

        cursor.execute(query)
        tasks = cursor.fetchall()

        if len(tasks) == 0:
            print("No tasks found")
        else:
            for task in tasks:
                print(
                    f"Id: {task[0]}, Title: {task[1]}, Description: {task[2]}, Status: {task[3]}, Priority: {task[4]}, Created at: {task[5]}")

    except sqlite3.Error as e:
        print(e)


def edit_task(connection, id:int):

    cursor = connection.cursor()

    query = f"SELECT * FROM tasks WHERE id = {id} "
    cursor.execute(query)

    task = cursor.fetchone()
    if task == None:
        print("No tasks with this ID")
        return
    else:
        print("Task to edit:")
        print(f"Id: {task[0]}, Title: {task[1]}, Description: {task[2]}, Status: {task[3]}, Priority: {task[4]}, Created at: {task[5]}")
    
    title = input("Enter the new task title: ")
    if title == "":
        title = task[1]

    description = input("Enter the new task description: ")
    if description == "":
        description = task[2]

    statuses = ["to do", "in progress", "completed"]
    while True:
        status = input(f"Statuses: {statuses}\nEnter the new status: ")
        if not status.lower() in statuses:
            print("Invalid status.")
        else:
            break

    while True:
        priority = input("Enter the priority: ")
        if priority != "" and not priority.isdigit():
            print("Invalid priority. Please enter an integer.")
        else:
            break
    if priority == "":
        priority = task[4]

    query = f"UPDATE tasks SET title = ?, description = ?, status = ?, priority = ? WHERE id = ?"
    try:
        cursor.execute(query, (title, description, status, priority, id))
        connection.commit()
        print("Task updated")
    except sqlite3.Error as e:
        print(e)


def delete_task(connection, id:int):
    cursor = connection.cursor()

    query = f"SELECT * FROM tasks WHERE id = {id}"
    cursor.execute(query)

    tasks = cursor.fetchall()
    if len(tasks) == 0:
        print("No tasks with the provided ID")
    else:
        if input(f"Are you sure you want to delete the task '{tasks[0][1]}'? (y/n) ").lower() == "n":
            return

        try:
            cursor.execute(f"DELETE FROM tasks WHERE id = {id}")
            connection.commit()
            print(f"Task {tasks[0][1]} deleted successfully")
        except sqlite3.Error as e:
            print(e)


def search(connection, s:str=""):
    cursor = connection.cursor()
    s = s.lower()
    query = f"SELECT * FROM tasks WHERE LOWER(title) like '%{s}%' OR LOWER(description) like '%{s}%'"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if len(tasks) == 0:
        print("No tasks found")
    else:
        print("Found tasks:")
        for task in tasks:
            print(f"Id: {task[0]}, Title: {task[1]}, Description: {task[2]}, Status: {task[3]}, Priority: {task[4]}, Created at: {task[5]}")
    
