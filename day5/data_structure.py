"""
A Simple PhoneBook.

This is implemented in two ways, using a `list` and a `dict`
and then used to compare the efficiency of each.
"""


class PhoneBookList(object):

    """This PhoneBook employs `list` datastructure in managing phone contacts."""

    def __init__(self):
        self.book = []

    def add_contact(self, username, phone_number):
        self.book.append([username, phone_number])
