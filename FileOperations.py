from ContactBook_class import *

#本文件是cbl部分的文件读写
def write_user_to_file(user, filename):
    with open(filename, 'a') as file:
        file.write(f"{user.name},{user.phone_number},{user.__class__.__name__}\n")

def read_users_from_file(filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            name, phone_number, user_type = line.strip().split(',')
            if user_type == 'Classmate':
                user = Classmate(name,1 ,phone_number,1,1,1)
            elif user_type == 'Teacher':
                user = Teacher(name, 1,phone_number,1,1,1,1)
            elif user_type == 'Colleague':
                user = Colleague(name,1, phone_number,1,1)
            elif user_type == 'Friend':
                user = Friend(name, 1,phone_number,1,1)
            elif user_type == 'Relative':
                user = Relative(name, 1,phone_number,1,1)
            users.append(user)
    return users

def delete_user_from_file(username, filename):
    # Read all users from the file
    users = read_users_from_file(filename)

    # Find the user with the specified name
    users = [user for user in users if user.name != username]

    # Rewrite the updated user list to the file
    with open(filename, 'w') as file:
        for user in users:
            file.write(f"{user.name},{user.phone_number},{user.__class__.__name__}\n")

def modify_data(filename, target_name, new_data):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Assuming the name is in the first column
            if line.split(',')[0].strip() == target_name:
                # Modify the line with new data
                lines[i] = f"{new_data}\n"

        with open(filename, 'w') as file:
            file.writelines(lines)