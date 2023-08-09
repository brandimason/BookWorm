from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import (Base, User, Book, Book_Read)

if __name__ == "__main__":

    engine = create_engine('sqlite:///book.db')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        #books
        harrypotter = Book(title = "Harry Potter and the Sorcerer's Stone", author = "JK Rowling")
        untamed = Book(title = "Untamed", author = "Glennon Doyle")
        fouragreements = Book(title = "The Four Agreements", author = "Don Miguel Ruiz")
        twilight = Book(title = "Twilight", author = "Stephenie Meyer")
        #users
        stephen = User(firstname = "Stephen", lastname = "Lambert")
        sherina =User(firstname = "Sherina", lastname = "Buenaseda")
        shamim = User(firstname = "Shamim", lastname = "Sharifi")
        yesenia = User(firstname = "Yesenia", lastname = "Follingstag")
        #create many to many relationships
        b1 = Book_Read(user_id = stephen.id, book_id = harrypotter.id)
        b2 = Book_Read(user_id = sherina.id, book_id = untamed.id)
        b3 = Book_Read(user_id = shamim.id, book_id = twilight.id)
        b4 = Book_Read(user_id = yesenia.id, book_id = fouragreements.id)
        
        session.add_all([
            harrypotter,
            untamed,
            fouragreements,
            twilight,
            stephen,
            sherina,
            shamim,
            yesenia,
            b1,
            b2,
            b3,
            b4
            ])
        session.commit()