class Car:
    """
    Базовый класс для автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Конструктор класса Car.

        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        """
        self.__brand = brand  # Инкапсуляция для защиты данных
        self.__model = model  # Инкапсуляция для защиты данных
        self.__year = year   # Инкапсуляция для защиты данных

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строка с информацией о автомобиле
        """
        return f"{self.__brand} {self.__model} ({self.__year})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.

        :return: Официальная строка с информацией о классе и атрибутах
        """
        return f"Car(brand={self.__brand!r}, model={self.__model!r}, year={self.__year!r})"

    def get_info(self) -> str:
        """
        Получить информацию о автомобиле.

        :return: Строка с информацией о автомобиле
        """
        return f"{self.__brand} {self.__model}, {self.__year} года выпуска."


class PassengerCar(Car):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, seats: int) -> None:
        """
        Конструктор класса PassengerCar.

        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param seats: Количество мест в легковом автомобиле
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.__seats = seats  # Инкапсуляция для защиты данных

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строка с информацией о легковом автомобиле
        """
        return f"{super().__str__()} | Мест: {self.__seats}"

    def get_info(self) -> str:
        """
        Получить информацию о легковом автомобиле.

        :return: Строка с информацией о легковом автомобиле
        """
        base_info = super().get_info()  # Вызов метода базового класса
        return f"{base_info}, {self.__seats} мест."


class CargoCar(Car):
    """
    Дочерний класс для грузовых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Конструктор класса CargoCar.

        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param capacity: Грузоподъемность автомобиля в тоннах
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.__capacity = capacity  # Инкапсуляция для защиты данных

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        :return: Строка с информацией о грузовом автомобиле
        """
        return f"{super().__str__()} | Грузоподъемность: {self.__capacity} т"

    def get_info(self) -> str:
        """
        Получить информацию о грузовом автомобиле. Переопределяет метод базового класса.

        Переопределяем этот метод, чтобы добавить информацию о грузоподъемности.

        :return: Строка с информацией о грузовом автомобиле
        """
        base_info = super().get_info()  # Вызов метода базового класса
        return f"{base_info}, грузоподъемность {self.__capacity} тонн."


if __name__ == "__main__":
    # Создание экземпляров легкового и грузового автомобиля
    passenger_car = PassengerCar(brand="Toyota", model="Camry", year=2022, seats=5)
    cargo_car = CargoCar(brand="MAN", model="TGS", year=2021, capacity=18.0)

    # Печать информации об автомобилях
    print(passenger_car)
    print(cargo_car)