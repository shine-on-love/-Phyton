
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


# Пример использования
paper_book = PaperBook("1984", "George Orwell", 328)
audio_book = AudioBook("1984", "George Orwell", 11.5)

print(paper_book)  # Использует __str__ из базового класса
print(repr(paper_book))  # Использует перегруженный __repr__

print(audio_book)  # Использует __str__ из базового класса
print(repr(audio_book))  # Использует перегруженный __repr__

# Попытка изменить name или author вызовет ошибку
# paper_book.name = "New Name"  # AttributeError: can't set attribute

# Попытка установить недопустимое значение для pages или duration
# paper_book.pages = -10  # ValueError: Количество страниц должно быть положительным целым числом
# audio_book.duration = -5.0  # ValueError: Продолжительность должна быть положительным числом