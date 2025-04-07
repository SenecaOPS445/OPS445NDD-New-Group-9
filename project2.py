#!/usr/bin/env python3

import os
import sys

def list_users():
    users = []
    with open("/etc/passwd", "r") as f:
        for line in f:
            parts = line.split(":")
            username = parts[0]
            uid = int(parts[2])
            if uid >= 1000 and uid != 65534:
                users.append(username)
    return users

def add_user(username):
    os.system(f"adduser {username}")

def change_password(username):
    os.system(f"passwd {username}")

def add_to_group(username, groupname):
    os.system(f"usermod -aG {groupname} {username}")

def user_delete(username):
    confirm = input(f"Are you sure you want to delete {username}? (y/n): ")
    if confirm.lower() == "y":
        os.system(f"userdel {username}")
    else:
        print ("User not deleted")


def menu():
    while True:
        print("\nUser Management Menu:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. List Users")
        print("5. Add to Group")
        print("6. Exit")
        choice = input("Enter your choice(Number): ")

        if choice == "1":
            username = input("Enter new username: ")
            add_user(username)
        elif choice == "2":
            users = list_users()
            index = 1
            for user in users:
                print(f"{index}. {user}")
                index += 1
            user_index = int(input("Select user number to delete: ")) -1 
            if 0 <= user_index < len(users):
                user_delete(users[user_index])
        elif choice == "3":
            users = list_users()
            index = 1
            for user in users:
                print(f"{index}. {user}")
                index += 1
            user_index = int(input("Select number to reset password: ")) -1 
            if 0 <= user_index < len(users):
                change_password(users[user_index])
        elif choice == "4":
            users = list_users()
            print("\nRegisterd Users: ")
            index = 1
            for user in users:
                print(f"{index}. {user}")
                index += 1
        elif choice == "5":
            users = list_users()
            index = 1 
            for user in users:
                print(f"{index}. {user}")
                index += 1
            user_index = int(input("Select number to add to group")) -1 
            if 0 <= user_index < len(users):
                groupname = input("Which group would you like to add the user to?: ")
                add_to_group(users[user_index], groupname)
        elif choice == "6":
            print("Goodbye")
            sys.exit(0)
        else:
            print("Invalid choice. Try again")


if __name__ == "__main__":
    menu()

