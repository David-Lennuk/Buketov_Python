# task_list = []

# def add_task(task):
#     task_list.append(task)
#     return task_list

# def remove_task(task):
#     if task in task_list:
#         task_list.remove(task)
#     else:
#         print("Task not found.")

# def review_tasks():
#     if task_list:
#         print("Here are your tasks:")
#         for i, task in enumerate(task_list, 1):
#             print(f"{i}. {task}")
#     else:
#         print("No tasks available.")

# def main():
#     while True:
#         print("1 - Add task\n2 - Remove task\n3 - Review tasks\n4 - Exit")
#         user_input = input("What would you like to do? ")
        
#         if user_input == '1':
#             task = input("Enter the task: ")
#             add_task(task)
#         elif user_input == '2':
#             task = input("Enter the task to remove: ")
#             remove_task(task)
#         elif user_input == '3':
#             review_tasks()
#         elif user_input == '4':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid input, please try again.")

import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Todo list")

def add_task():
    task = st.text_input("Sisesta uus ülesanne", key)
