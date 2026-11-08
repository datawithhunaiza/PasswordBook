#Streamlit application for password Book

import streamlit as st
import random
import string
import os

# Page configuration
st.set_page_config(
    page_title="Password Book",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Book")
st.write("Generate and manage your passwords in one place.")

FILE_NAME = "password.txt"

# Load passwords from file
def load_passwords():
    passwords = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if ":" in line:
                    site, pwd = line.split(":", 1)
                    passwords[site] = pwd

    return passwords


# Save passwords to file
def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site}:{pwd}\n")


# Generate random password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@$%&*"
    pwd = ''.join(random.choice(characters) for _ in range(12))
    return pwd

# Load stored passwords
if "passwords" not in st.session_state:
    st.session_state.passwords = load_passwords()


passwords = st.session_state.passwords

# Sidebar menu
st.sidebar.title("Menu")

choice = st.sidebar.radio(
    "Select an operation:",
    [
        "Generate Password",
        "View Passwords",
        "Store Password",
        "Update Password",
        "Delete Password"
    ]
)


# 1. Generate Password
if choice == "Generate Password":

    st.subheader("Generate a New Password")

    site = st.text_input("Enter website name")

    if st.button("Generate Password"):

        if site.strip():
            pwd = generate_password()

            passwords[site] = pwd
            save_passwords(passwords)

            st.success(f"Password generated for {site}!")

            st.code(pwd)

        else:
            st.warning("Please enter a website name.")


# 2. View Passwords
elif choice == "View Passwords":

    st.subheader("Your Stored Passwords")
    if passwords:
        for site, pwd in passwords.items():
            st.write(f"**Website:** {site}")
            st.code(pwd)

    else:
        st.info("No passwords stored yet.")

# 3. Store Password
elif choice == "Store Password":

    st.subheader("Store a New Password")

    site = st.text_input("Website name")
    pwd = st.text_input("Enter password", type="password")

    if st.button("Save Password"):

        if site.strip() and pwd:
            passwords[site] = pwd
            save_passwords(passwords)

            st.success(f"Password for {site} saved successfully!")

        else:
            st.warning("Website name and Password both are required.")


# 4. Update Password
elif choice == "Update Password":

    st.subheader("Update Existing Password")

    if passwords:

        site = st.selectbox(
            "Select website",
            list(passwords.keys())
        )

        new_pwd = st.text_input(
            "Enter new password",
            type="password"
        )

        if st.button("Update Password"):

            if new_pwd:
                passwords[site] = new_pwd
                save_passwords(passwords)

                st.success(f"Password for {site} updated!")

            else:
                st.warning("Please enter a new password.")

    else:
        st.info("No passwords available to update.")


# 5. Delete Password
elif choice == "Delete Password":

    st.subheader("Delete Stored Password")

    if passwords:

        site = st.selectbox(
            "Select website to delete",
            list(passwords.keys())
        )

        if st.button("Delete Password"):
            
            del passwords[site]
            save_passwords(passwords)

            st.success(f"Password for {site} deleted!")

    else:
        st.info("No passwords available to delete.")
