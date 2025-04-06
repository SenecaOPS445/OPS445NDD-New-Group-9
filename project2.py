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



if __name__ == "__main__":
    print (list_users())
