#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from db.models import (Base, User, Book, Book_Read)
from db.seed import engine
import pyfiglet

# goals of CLI
# 1.) greet the new user - welcome to your bookshelf!
# 2.) login to your account // see a list of the books you've read // add a new book to your bookshelf
# 3.) create a new account // add a new book to your account
# 4.) logout of your account, takes your back to the main menu
# ***Stretch Goal***: add a list of books you're reading


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()


    # banner with pyfiglet
    result = pyfiglet.figlet_format("BookWorm", font = "digital" )
    print(result)
    user_input = input("Hi BookWorm! Welcome to your bookshelf!\nPress Enter to Continue\n")
    # can I get these to display together?^^


    def display_menu(menu):
        for k, function in menu.items():
            print(k, function.__name__)
    
    def Create_Account():
        print("you have selected menu option one")
        input("Press Enter to Continue\n")


    def Login():
        # def test_user():
            find_user = input("Enter your name to find your bookshelf:")
            user = session.query(User).filter_by(firstname = find_user).first()
            if user:
                bookshelf_data = session.query(Book_Read).filter_by(user_id = user.id).all()
                if bookshelf_data:
                    print(f"Bookshelf data for user {user.firstname}:")
                    for book in bookshelf_data:
                        print(book.book_title)
            Login()
        # test_user()
            # print("you have selected menu option two")
            # input("Press Enter to Continue\n")

        # once you log in, you can see your bookshelf & add a new book


    def Exit():
        print("Goodbye")
        exit()


    def main():
        functions_names = [Create_Account, Login, Exit]
        menu_items = dict(enumerate(functions_names, start=1))

        while True:
            display_menu(menu_items)
            selection = int(
                input("Please enter your selection number: "))
            selected_value = menu_items[selection]
            selected_value() 


    if __name__ == "__main__":
        main()