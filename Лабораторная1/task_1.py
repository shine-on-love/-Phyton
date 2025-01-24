from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, material: str, dimensions: tuple):
        """Инициализирует объект Furniture.

        :param material: Материал, из которого изготовлена мебель.
        :param dimensions: Размеры мебели в виде кортежа (длина, ширина, высота).
        :raises ValueError: Если материал является пустой строкой или размеры не являются положительными числами.
        """
        if not material:
            raise ValueError("Материал не должен быть пустой строкой.")
        if any(d <= 0 for d in dimensions):
            raise ValueError("Размеры должны быть положительными числами.")

        self.material = material
        self.dimensions = dimensions


    def assemble(self) -> None:
        """Сборка мебели."""
        pass


    def disassemble(self) -> None:
        """Разборка мебели."""
        pass


class Plant(ABC):
    def __init__(self, species: str, height: float, age: int):
        """Инициализирует объект Plant.

        :param species: Вид растения.
        :param height: Высота растения в сантиметрах.
        :param age: Возраст растения в годах.
        :raises ValueError: Если species является пустой строкой, height не положительное число или age отрицательное число.
        """
        if not species:
            raise ValueError("Вид растения не должен быть пустой строкой.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом.")

        self.species = species
        self.height = height
        self.age = age


    def water(self, amount: float) -> None:
        """Полив растения.

        :param amount: Количество воды в миллилитрах.
        :raises ValueError: Если amount не положительное число.
        """
        pass


    def fertilize(self) -> None:
        """Удобрение растения."""
        pass


class SocialMedia(ABC):
    def __init__(self, platform_name: str, user_count: int):
        """Инициализирует объект SocialMedia.

        :param platform_name: Название социальной сети.
        :param user_count: Количество пользователей.
        :raises ValueError: Если platform_name является пустой строкой или user_count отрицательное число.
        """
        if not platform_name:
            raise ValueError("Название социальной сети не должно быть пустой строкой.")
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом.")

        self.platform_name = platform_name
        self.user_count = user_count


    def create_post(self, content: str) -> None:
        """Создание поста в соцсети.

        :param content: Содержимое поста.
        :raises ValueError: Если content является пустой строкой.
        """
        pass


    def delete_post(self, post_id: int) -> None:
        """Удаление поста по ID.

        :param post_id: ID поста.
        """
        pass
