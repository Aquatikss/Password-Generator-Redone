# Password Generator

A Python-based password generator application that creates secure, customizable passwords based on user preferences.

## Features

* Generate passwords with customizable length
* Include or exclude:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*, etc.)
* Copy generated password to clipboard
* User-friendly GUI interface

## Requirements

* Python 3.x
* Tkinter library (usually comes with Python installation)
* pyperclip library for clipboard functionality

## Installation

1. Clone the repository:
```
bash git clone [https://github.com/Aquatikss/Password-Generator-Redone.git](https://github.com/Aquatikss/Password-Generator-Redone.git)
``` 

2. Navigate to the project directory:
```
bash cd Password-Generator-Redone
``` 

3. Install required dependencies:
```
bash pip install pyperclip
``` 

## Usage

Run the program:
```
bash python main.py
``` 

1. Select desired password criteria using checkboxes
2. Choose password length using the slider
3. Click "Generate" to create a new password
4. Use the "Copy" button to copy the password to clipboard

## License

This project is open source and available under the MIT License.

You can save this as README.md in your project directory and then commit it:
``` bash
# Create the README file (On Windows CMD)
echo # Password Generator > README.md

# Add and commit the README
git add README.md
git commit -m "Add README.md"

# Try pushing again (after pulling as mentioned in previous message)
git pull --rebase origin main
git push -u origin main
```
