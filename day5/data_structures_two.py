class PhoneBook(object):

    """
    A Simple PhoneBook.

    This is implemented in two ways, using a `list` and a `dict`
    and then used to compare the efficiency of each.
    """

    def __init__(self, book):
        """Initialize a phone book using the provided source as a datastore."""
        self.book = book

    def add_contact(self, username, phone_number):
        """Add a record into the phone book."""
        if isinstance(self.book, dict):
            self.book[username] = phone_number
        else:
            self.book.append([username, phone_number])

    def search(self, username):
        """
        Search for a record and profile the search.

        Return a `dict` with the phone number and number of loop counts.
        The loop counts is the number of times the phone book was iterated over
        before the key was found.

        e.g {'counts': 3, 'phone_number': '9083'}
        """
        if isinstance(self.book, list):
            counts = 0
            for u, p in self.book:
                counts += 1
                if u == username:
                    return {'counts': counts, 'phone_number': p}

            return {'phone_number': None, 'counts': counts}
        else:
            result = {'phone_number': self.book.get(username), 'counts': 1}
            return result


class PhoneBookList(PhoneBook):

    """This PhoneBook employs `list` datastructure in managing phone contacts."""

    def __init__(self):
        """Initialize a phone book that uses a `list` as a datastore."""
        super(PhoneBookList, self).__init__([])


class PhoneBookDict(PhoneBook):

    """This PhoneBook employs `dict` data structure in managing phone contacts."""

    def __init__(self):
        """Initialize a phone book that uses a `dict` as a datastore."""
        super(PhoneBookDict, self).__init__({})
