from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import (Base, User, Book, Book_Read)

if __name__ == "__main__":

    engine = create_engine('sqlite:///book.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # do i need this ^ if i am using what's below: the Base.metadata
    Base.metadata.create_all(engine)

    session.query(Book).delete()
    session.query(User).delete()
    session.query(Book_Read).delete()

    # with Session(engine) as session:
    
    #books
    harrypotter = Book(title = "Harry Potter and the Sorcerer's Stone", author = "JK Rowling")
    untamed = Book(title = "Untamed", author = "Glennon Doyle")
    fouragreements = Book(title = "The Four Agreements", author = "Don Miguel Ruiz")
    twilight = Book(title = "Twilight", author = "Stephenie Meyer")
    session.add_all([
        harrypotter,
        untamed,
        fouragreements,
        twilight
    ])
    session.commit()

    #users
    stephen = User(firstname = "Stephen", lastname = "Lambert")
    sherina =User(firstname = "Sherina", lastname = "Buenaseda")
    shamim = User(firstname = "Shamim", lastname = "Sharifi")
    yesenia = User(firstname = "Yesenia", lastname = "Follingstag")
    session.add_all([
        stephen,
        sherina,
        shamim,
        yesenia
    ])
    session.commit()

    #create many to many relationships
    b1 = Book_Read(book_id = harrypotter.id, user_id = stephen.id)
    b2 = Book_Read(book_id = untamed.id, user_id = sherina.id)
    b3 = Book_Read(book_id = twilight.id, user_id = shamim.id)
    b4 = Book_Read(book_id = fouragreements.id, user_id = yesenia.id)
    
    session.add_all([
        b1,
        b2,
        b3,
        b4
    ])
    session.commit()

    print("end")