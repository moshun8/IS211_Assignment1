#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Part 2"""


class Book(object):
    '''
    Takes 2 string attributes:
    Book author
    Book title
    Prints sentence with attribute info
    '''

    def __init__(self, author='', title=''):
        self.author = author
        self.title = title

    def display(self):
        '''
        Prints out sentence with provided book title and author
        '''

        print "{0}, written by {1}".format(self.title, self.author)
        # print (self.title, ", written by " self.author)

if __name__ == "__main__":
    BK1 = Book("Steinbeck", "Of Mice and Men")
    BK2 = Book("Harper Lee", "To Kill a Mockingbird")
    print BK1.display()
    print BK2.display()