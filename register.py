user_list = []
from pprint import pprint

while True:
    print("""
    reg -> to register user
    del -> to delete user
    edit -> to change user info
    """)
    command = input('Enter a command ')
    if command == "reg":
        user_id = 0
        for user_info in user_list:
            if user_info['id']:
                if user_info['id'] > user_id:
                    user_id = user_info['id']

        name = input('Enter name ')
        username = input('Enter username ')
        password = input('Enter password ')
        age = int(input('Enter age '))

        info = {
            'id': user_id + 1,
            'name': name,
            "username": username,
            "password": password,
            "age": age
        }
        exist = False
        for user in user_list:
            if user['username'] == username:
                exist = True
        if exist:
            print(f'This username: {username} already exists')
        else:
            user_list.append(info)
    elif command == "del":
        if user_list:
            pprint(user_list)
            user_id = int(input("Enter id of user "))
            del user_list[user_id]
            print("User deleted")
        else:
            print("No users")
    elif command == "edit":
        if user_list:
            pprint(user_list)
            user_id = int(input("Enter id of user "))
            name = input('Enter name ')
            username = input('Enter username ')
            password = input('Enter password ')
            age = input('Enter age ')
            for user in user_list:
                if user['id'] == user_id:
                    if name:
                        user['name'] = name
                    if username:
                        user['username'] = username
                    if password:
                        user['password'] = password
                    if age:
                        age = int(age)
                        user['age'] = age
            print("User is changed")
        else:
            print("No users")
    pprint(user_list)
