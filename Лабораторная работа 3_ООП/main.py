class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.name} by {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', author='{self.author}')"

class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для установки значения

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, Pages: {self.pages}"

class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для установки значения

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float) or value <= 0.0:
            raise ValueError("Duration must be a positive float")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, Duration: {self.duration} hours"