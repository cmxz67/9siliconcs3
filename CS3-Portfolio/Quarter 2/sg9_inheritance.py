# parent class
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # getter methods para makuha yung values
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # setter methods para mapalitan yung values
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # ipakita yung publication info
    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


# book class na nag-iinherit from publication
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_of_pages)

    # kunin yung number of pages
    def get_number_of_pages(self):
        return self.__number_of_pages

    # check muna kung positive yung pages
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    # ipakita yung book info pati pages
    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


# magazine class na nag-iinherit din from publication
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    # kunin yung issue number
    def get_issue_number(self):
        return self.__issue_number

    # check kung positive yung issue number
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    # ipakita yung magazine info
    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)


# gumawa ng dalawang publication objects
publication1 = Publication("Introduction to Science", "John Smith")
publication2 = Publication("World History", "Maria Santos")

# gumawa ng dalawang book objects
book1 = Book("Noli Me Tangere", "Jose Rizal", 400)
book2 = Book("The Little Prince", "Antoine de Saint-Exupery", 96)

# gumawa ng dalawang magazine objects
magazine1 = Magazine("National Geographic", "Various Authors", 25)
magazine2 = Magazine("Science Today", "Science Editors", 12)


# display ng publication info
print("=== PUBLICATIONS ===")
publication1.display_info()
print()
publication2.display_info()

# display ng book info
print("\n=== BOOKS ===")
book1.display_info()
print()
book2.display_info()

# display ng magazine info
print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()
