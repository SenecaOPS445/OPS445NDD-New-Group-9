#!/usr/bin/env python3
#Nawaf Rihani

import os
import sys

def list_users():
    "Returns all user accounts from the /etc/passwd file"   
    users = []  #initialize emtpy list to store usernames
    with open("/etc/passwd", "r") as f: #opens and reads passwd file
        for line in f: #iterate through each line in file
            parts = line.split(":") #split line using : delimteter
            username = parts[0] #username is the first field
            uid = int(parts[2])  #UID is the 3rd field
            if uid >= 1000 and uid != 65534: #filter out non user accounts and "nobody" account
                users.append(username) #append usernames to list
    return users

def add_user(username):
    "Adds a new user using the adduser linux command"
    os.system(f"adduser {username}")

def change_password(username):
    "Changes password using the passwd linux command"
    os.system(f"passwd {username}")

def add_to_group(username, groupname):
    "Changes what group user belongs to with usermod linux command"
    os.system(f"usermod -aG {groupname} {username}")

def user_delete(username):
    "Deletes user account with confirmation"
    confirm = input(f"Are you sure you want to delete {username}? (y/n): ")
    if confirm.lower() == "y":
        os.system(f"userdel {username}")
    else:
        print ("User not deleted")


def menu():
    "Interactive menu for user management"
    while True:     #while true to keep menu looping after selection
        print("\nUser Management Menu:")    #interactive menu formatting
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. List Users")
        print("5. Add to Group")
        print("6. Exit")
        choice = input("Enter your choice(Number): ")   #retrieve user input

        if choice == "1":
            username = input("Enter new username: ")
            add_user(username)
        elif choice == "2":
            users = list_users() #retrieves list of users
            index = 1   #initialize index for numbering
            for user in users: #loop through all the users
                print(f"{index}. {user}")   #display username with a number
                index += 1 #increment number by 1
            user_index = int(input("Select user number to delete: ")) -1 #retrieve user selection
            if 0 <= user_index < len(users): #validate that the selection is valid
                user_delete(users[user_index]) #calls function
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
            user_index = int(input("Select number to add to group: ")) -1
            if 0 <= user_index < len(users):
                groupname = input("Which group would you like to add the user to?: ")
                #second selection that asks user to input group name
                add_to_group(users[user_index], groupname)
        elif choice == "6":
            print("Goodbye")
            sys.exit(0)     #exits program
        else:
            print("Invalid choice. Try again")


if __name__ == "__main__":
    menu()
