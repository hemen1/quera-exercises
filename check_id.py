import os

project_list = os.listdir('src')

project_id = input("Enter id: ")
while project_id.isdigit():
    if project_id in project_list:
        print(True)
    else:
        print(False)
    project_id = input("Enter id: ")
