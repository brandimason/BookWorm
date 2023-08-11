from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    
    # books= relationship('Book', secondary="books_read", backref='users')

class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    def __repr__(self):
        return f"\n \
            The book '{self.title}' was written by the author {self.author}."

    # users = relationship('User', secondary="books_read", backref='books')

class Book_Read(Base):
    
    __tablename__ = 'books_read'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    books = relationship("Book", backref="books_read")
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("User", backref="books_read")



