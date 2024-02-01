
class HockeyTeam:
    """
    Класс, описывающий хоккейную команду.

    Атрибуты:
    - name (str): название команды
    - city (str): город, в котором базируется команда

    Методы:
    - get_roster(): получить список игроков команды
    - add_player(name: str, position: str) -> None: добавить игрока в команду
    - remove_player(name: str) -> None: удалить игрока из команды
    """

    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city

    def get_roster(self):
        ...

    def add_player(self, name: str, position: str) -> None:
        ...

    def remove_player(self, name: str) -> None:
        ...


class Car:
    """
    Класс, описывающий автомобиль.

    Атрибуты:
    - brand (str): марка автомобиля
    - model (str): модель автомобиля
    - year (int): год выпуска автомобиля

    Методы:
    - start_engine(): запустить двигатель автомобиля
    - stop_engine(): остановить двигатель автомобиля
    - drive(distance: float) -> None: проехать определенное расстояние на автомобиле
    """

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        ...

    def stop_engine(self):
        ...

    def drive(self, distance: float) -> None:
        ...


class WeatherForecast:
    """
    Класс, описывающий прогноз погоды.

    Атрибуты:
    - date (str): дата прогноза
    - temperature (float): температура воздуха
    - description (str): описание погодных условий

    Методы:
    - get_date(): получить дату прогноза
    - get_temperature() -> float: получить температуру воздуха
    - get_description() -> str: получить описание погодных условий
    """

    def __init__(self, date: str, temperature: float, description: str):
        self.date = date
        self.temperature = temperature
        self.description = description

    def get_date(self):
        ...

    def get_temperature(self) -> float:
        ...

    def get_description(self) -> str:
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()


"Пример проверки с помощью doctest:"

def add_player(self, name: str, position: str) -> None:
    """
    Добавляет игрока в команду.

    Аргументы:
    - name (str): имя игрока
    - position (str): позиция игрока

    Пример использования:
    >>> team = HockeyTeam("Ак Барс", "Казань")
    >>> team.add_player("Александр Радулов", "нападающий")

    ['Александр Радулов - нападающий']
    """
    ...
