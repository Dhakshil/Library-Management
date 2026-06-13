class Library:

    def __init__(self, books = None, members = None, transactions = None):

        if books is None:
            self.books = []
        else:
            self.books = books
        
        if members is None:
            self.members = []
        else:
            self.members = members

        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions