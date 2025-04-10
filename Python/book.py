class Book:
    def __init__(self, title, author, genre, is_checked_out = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = is_checked_out

    def __str__(self):
        return self.title + " by " + self.author + " (" + self.genre + ")" + ": " + str(self.is_checked_out)
    
    def check_out(self):
        if self.is_checked_out == True:
            print("This book is already checked out.")
        else:
            self.is_checked_out = True
    
    def return_book(self):
        if self.is_checked_out == False:
            print("This book is not currently checked out.")
        else:
            self.is_checked_out = False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre
    
    def is_checked_out(self):
        return self.is_checked_out

    

    