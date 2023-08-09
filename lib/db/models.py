from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    
    books_read = relationship('Book_Read', backref=('user'))

class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    books_read = relationship('Book_Read', backref=('book'))

class Book_Read(Base):
    
    __tablename__ = 'books_read'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))


