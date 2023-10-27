# BookWorm 📚🐛

Welcome to BookWorm, a literary app that helps track progress towards and achieve literary goals built with Python and SQLite. 

*** 

## Installation

1. Fork and clone this repo from Github to your local environment
2. Navigate into your local directory and open the contents in your preferred code editor
3. Run `pipenv install` to install dependencies 
4. Run `pipenv shell` to create virtual environment
5. CD into the `lib` file
6. CD into the `db` file
7. From the project directory, run `python seed.py` to populate the database with books
8. CD back into `lib`
9. Run `pipenv install pyfiglet` to install Pyfiglet
10. Run `pipenv install colorama` to install Colorama


## Use 
Ready to add a book? Here's how to get started: 
1. From the project directory, run `python cli.py`
2. Enter a number 1-4 from the menu. Start with 1 to register as a new player. 
3. Follow the resulting prompts
4. Type `"3"` or `"exit"` to end the program

## Features 

🐛 Create a new account <br>
- Enter your first name and last name to register and be eligible to track your progress

🐛 Log into your account <br>
- Enter your first name, make sure to capitalize the first letter of your name.

🐛 Create a new book <br>
- Enter a book to keep a history of the books you've read

## Data tables
😀 user <br>
- Stores readers with their **username**

😀 book <br>
- Stores books with their **title** and **author**

😀 book_read <br>
- Stores results with their **book_id, user_id, books,** and **users**


## References 
[Pyfiglet](https://pypi.org/project/pyfiglet/) <br>
[Figlet](http://www.figlet.org/)

## License
[MIT](https://choosealicense.com/licenses/mit/)