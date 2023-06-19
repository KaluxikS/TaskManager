# Task Manager

Description
----
The application was created as part of a group project for the subject PPY. Task Manager is software used for task management. In short, it is a basic TODO list.

Usage
----
To run the application, use the following command (while being in the project folder): python main.py

The following menu should appear on the screen:

![image](https://github.com/KaluxikS/TaskManager/assets/128908183/cfabc7d9-a624-4791-b38f-32fd9c9f54c2)


1. Add new task - adds a new task to the database. After selecting this option, a corresponding form will appear. Once the form is filled out, the task will be added with the current creation date.
2. Display tasks - this option allows you to display tasks from the database, with the ability to sort and filter them by their status.
3. Search tasks by title or description - the user is prompted to enter a search phrase, and the program then searches for that phrase in the titles and descriptions of all tasks.
4. Edit task - allows you to edit a specific task. If you don't want to edit a particular record, simply press enter and proceed to the next one.
5. Delete task - deletes a task based on the provided ID.

Each task has a unique ID, which is used to identify task data in operations such as Edit task and Delete task. You can find information about which task has which ID by using the Display tasks or Search tasks by title or description options.

Error Handling
----
The application is capable of detecting errors or incorrect instructions provided by the user. If the user enters an incorrect option in the menu or provides an ID that is not assigned to any task, the application will display an appropriate message and cancel the operation.
