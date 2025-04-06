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
    os.system(f"usermod =aG {groupname} {username}")








if __name__ == "__main__":
    change_password("banana")
