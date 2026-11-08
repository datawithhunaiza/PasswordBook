#Main logic for the Password Book application

import random
import string

password = {}

#error handling
try:
    with open("password.txt", "r") as file:
        for line in file:
            site, pwd = line.strip().split(":")
            password[site] = pwd
except FileNotFoundError:
    pass

#function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%&*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

#loop to interact with the user
while True:
    print("-----------Password Manager-----------")
    print("Enter 1 to Generate a new password")
    print("Enter 2 to View stored password")
    print("Enter 3 to Store a new password")
    print("Enter 4 to Update an existing password")
    print("Enter 5 to Delete a stored password")
    print("Enter 6 to Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter the website name: ")
        pwd = generate_password()
        password[site] = pwd
        print(f"Generated password for {site}: {pwd}")

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

    if choice == "2":
        if not password:
            print("No passwords stored.")
        else:
            for site, pwd in password.items():
                print(f"{site}: {pwd}")

    if choice == "3":
        site = input("Enter the website name: ")
        pwd = input("Enter the password: ")
        password[site] = pwd
        print(f"Password for {site} stored successfully.")

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")       

    if choice == "4":
        site = input("Enter the website name: ")
        if site in password:
            pwd = input("Enter the new password: ")
            password[site] = pwd
            print(f"Password for {site} updated successfully.")
        else:
            print(f"No password found for {site}")

    if choice == "5":
        site = input("Enter the website name: ")
        if site in password:
            del password[site]
            print(f"Password for {site} deleted successfully.")
        else:
            print(f"No password found for {site}")

    if choice == "6":
        break

