# 🔐 Password Manager

A simple Password Manager built using Python and Streamlit.

## Features

- Generate random passwords.
- Store website passwords.
- View saved passwords.
- Update existing passwords.
- Delete stored passwords.
- Store data using Python file handling.

## Tech Stack

- Python
- Streamlit
- File Handling
- Random and String Modules

## Project Structure

```text
PasswordBook/
│
├── password_app.py
├── main_logic.py
├── requirements.txt
├── .gitignore
└── README.md
```

main_logic.py is the file where main logic for the Password Book application exists.

Run password_app.py file using the command: streamlit run password_app.py in step 4.

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate into the project:

```bash
cd PasswordBook
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run password_app.py
```

## Security Note

This is an educational project. Passwords are currently stored in a local text file without encryption. Do not use it for storing real credentials.

## Future Improvements

- Password encryption.
- Master password authentication.
- Password visibility toggle.
- Copy-to-clipboard functionality.
- Database integration.

## Author

Hunaiza Sultan

Computer Systems Engineering Student
