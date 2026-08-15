# Password Generator

A simple and secure command-line password generator built with Python as part of the **Auspify Technologies Python Development Internship**.

## Features

* Generate secure random passwords
* Customize password length
* Include letters, numbers, and symbols
* Generate multiple passwords in one run
* Validate password length
* Validate number of passwords
* Handle invalid user input
* Guarantee at least one letter, one number, and one symbol in each generated password

## Technologies Used

* Python 3.14+
* `secrets` — secure random password generation
* `string` — predefined letters, digits, and punctuation characters

## Project Structure

```text
Task-1-Password-Generator/
│
├── password_generator.py
├── README.md
├── .gitignore
└── .venv/
```

> `.venv/` is a local virtual environment and is excluded from Git using `.gitignore`.

## How to Run

### 1. Clone the repository

```bash
git clone git@github.com:shivangtrivedi87/auspify-python-task-1-password-generator.git
```

### 2. Navigate to the project

```bash
cd auspify-python-task-1-password-generator
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

### 5. Run the application

```bash
python password_generator.py
```

## Example

```text
Enter password length: 12
How many passwords do you want to generate? 3

Password 1: x7@Kp2#Lm9$q
Password 2: A4!zT8&nP5*w
Password 3: m9$Qe3@Rx7#v
```

The generated passwords will be different each time because secure random selection is used.

## Input Validation

The application validates:

* Password length must be at least 3 characters.
* Number of passwords must be greater than 0.
* Non-numeric input is rejected with an appropriate error message.

## Internship Task

**Program:** Python Development Internship
**Organization:** Auspify Technologies
**Task:** Task 1 — Password Generator

The project implements the requirements specified in the internship task guidelines.

## Author

**Shivang Trivedi**

GitHub: `https://github.com/shivangtrivedi87`
