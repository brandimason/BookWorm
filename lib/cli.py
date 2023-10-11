#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from db.models import (User, Book_Read, Book)
import pyfiglet
import sys
from os import system
from colorama import init, Fore, Back, Style
init(autoreset=True)

# goals of CLI
# 1.) greet the new user - welcome to your bookshelf!
# 2.) login to your account // see a list of the books you've read // add a new book to your bookshelf
# 3.) logout of your account, takes your back to the main menu
# ***Stretch Goal***: 
# 4.) create a new account // add a new book to your account
# 5.) add a list of books you're reading


if __name__ == "__main__":
    engine = create_engine('sqlite:///db/book.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # banner with pyfiglet
    result = pyfiglet.figlet_format("BookWorm", font = "big" )
    print(result)
    print("\033[1;35m Wadddduppp. Welcome to your bookshelf!\n")



def Add_New_Book(user):
    print("\033[1;35mPerfect! Let's do it!")
    create_book_title = input("\033[1;35mEnter book title: ")
    create_book_author = input("\033[1;35mEnter book author: ")
    new_book = Book(title=create_book_title, author=create_book_author)
    session.add(new_book)
    session.commit()
    add_to_bookshelf = Book_Read(book_id= new_book.id, user_id=user.id)
    session.add(add_to_bookshelf)
    session.commit()
    print("\033[1;35mWoooo! Your book has been added!")
    response = input("\033[1;35mWould you like to add another book? Y/N: ")
    if response.lower() == 'y':
        Add_New_Book()
    else:
        print("\033[1;35mTTFN! Come back soon!")
        exit()


##displays login Menu
def display_menu(menu):
        for k, function in menu.items():
            print(k, function.__name__)

def Exit():
    print("\033[1;35m\nSo long,\nfarewell,\nauf Wiedersehen,\nand goodbye.\nGoodbye,\ngoodbye,\ngoodbye.\nGoodbyeeeee!\n")
    sys.exit()

def Create_Account():
    print("\nWow, can I just say I'm so happy you want to be apart of this!\n~do your thing~")
    create_user_firstname = input("\nEnter your first name: ")
    create_user_lastname = input("Enter your last name:  ")
    new_user = User(firstname=create_user_firstname , lastname=create_user_lastname)
    session.add(new_user)
    session.commit()
    print("\nYay! It's ~ *official* ~ \nWelcome to the club!\n")
    Login()
    

def Login():
    find_user = input("\033[1;35mEnter your name to find your bookshelf: ")
    user = session.query(User).filter_by(firstname = find_user).first()
    books = []
    if user:
        user_relationships = session.query(Book_Read).filter_by(user_id = user.id).all() #=>list of all relationships
        if user_relationships:
            print(f"{user.firstname}'s Bookshelf:")
            for relationship in user_relationships: #for each relationship we have, query for the related book
                read_book = session.query(Book).filter_by(id = relationship.book_id).first()
                books.append(read_book)
            for n in books:
                # print(n)
                print(f"{n.title}'s by {n.author}")
            response = input("\033[1;35mWould you like to add a book? Y/N: ")
            if response.lower() == 'y':
                Add_New_Book(user)
            else:
                print("\033[1;35mTTFN! Come back soon!")
                exit()
        else:
            print("\033[1;35m\nYou have not logged any books yet!")
            response = input("\033[1;35mWould you like to add a book? Y/N: ")
            if response.lower() == 'y':
                Add_New_Book(user)
            else:
                print("\033[1;35mTTFN! Come back soon!")
                exit()
    else: 
        print("\033[1;35mWhoops! Can you please try again? (p.s. it is case sensitive)")
    Login()


def main():
    functions_names = [Create_Account, Login, Exit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("\n\033[1;35mPlease enter your selection number: "))
        selected_value = menu_items[selection]
        selected_value() 


if __name__ == "__main__":
    main()