class Book:
    """ A class to represent a book """

    def __init__(self, id: int, author: str, title: str, is_favorite: bool = False):
        self.id = id
        self.author = author
        self.title = title
        self.is_favorite = is_favorite
