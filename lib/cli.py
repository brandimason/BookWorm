#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from db.models import (User, Book_Read, Book)
import pyfiglet
import sys
from os import system

# goals of CLI
# 1.) greet the new user - welcome to your bookshelf!
# 2.) login to your account // see a list of the books you've read // add a new book to your bookshelf
# 3.) create a new account // add a new book to your account
# 4.) logout of your account, takes your back to the main menu
# ***Stretch Goal***: add a list of books you're reading


if __name__ == "__main__":
    engine = create_engine('sqlite:///db/book.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # banner with pyfiglet
    result = pyfiglet.figlet_format("BookWorm", font = "digital" )
    print(result)
    print("Hi BookWorm! Welcome to your bookshelf!\n")

##displays login Menu
def display_menu(menu):
        for k, function in menu.items():
            # print("in dislay menu function")
            print(k, function.__name__)

def Create_Account():
    # print("in create account function")
    create_user_firstname = input("Enter a first name:")
    create_user_lastname = input("Enter a last name:")
    new_user = User(firstname=create_user_firstname , lastname=create_user_lastname)
    session.add(new_user)
    session.commit()
    input("Your account has been created!\n")
    Add_New_Book()

def Login():
    # print("in login function")
    find_user = input("Enter your name to find your bookshelf: ")
    user = session.query(User).filter_by(firstname = find_user).first()
    books = []
    if user:
        user_relationships = session.query(Book_Read).filter_by(user_id = user.id).all() #=>list of all relationships
        if user_relationships:
            print(f"Bookshelf data for user {user.firstname}:")
            for relationship in user_relationships: #for each relationship we have, query for the related book
                read_book = session.query(Book).filter_by(id = relationship.book_id).first()
                books.append(read_book)
            for n in books:
                # print(n)
                print(f"{n.title} by {n.author} {n.id}")
            return 
        else:
            print("User does not have any books.\n")
            Add_New_Book()
            return
    else: 
        print("Error: please input a correct name")
    Login()

# once you log in, you can see your bookshelf & add a new book

def Add_New_Book():
    print("Add a new Book")
    create_book_title = input("Enter book title: ")
    create_book_author = input("Enter book author: ")
    new_book = Book(title=create_book_title, author=create_book_author)
    session.add(new_book)
    session.commit()
    print("Your book has been added!")
    input("Would you like to add another book? Y/N: ")


def Exit():
    print("Goodbye!")
    sys.exit()


def main():
    # print("in main function")
    functions_names = [Create_Account, Login, Exit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        # print("in while loop")
        selection = int(
            input("Please enter your selection number: "))
        selected_value = menu_items[selection]
        selected_value() 


if __name__ == "__main__":
    # print("in ifmain at bottom")
    main()