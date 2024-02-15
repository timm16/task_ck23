if __name__ == "__main__":
    class drug:
        """
        Базовый класс для лекарств.
        """

        def __init__(self, name: str, dose: float):
            self._name = name  # Инкапсуляция: название лекарства не должно изменяться напрямую
            self.dose = dose

        def __str__(self) -> str:
            return f"Лекарство: {self._name}, дозировка: {self.dose} мг"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}('{self._name}', {self.dose})"

        def use(self) -> None:
            """
            Метод для имитации приема лекарства.
            """
            print(f"Принято лекарство {self._name} в дозировке {self.dose} мг")


    class aspirin(drug):
        """
        Класс для Аспирина, наследуется от Лекарство.
        """

        def __init__(self, dose: float, form: str):
            super().__init__("Аспирин", dose)
            self.form = form  # Например, таблетки или порошок

        def __str__(self) -> str:
            return super().__str__() + f", форма: {self.form}"

        def use(self, with_water: bool = True) -> None:
            """
            Метод для имитации приема Аспирина, перегружен для добавления информации о приеме с водой.
            """
            additional_info = "с водой" if with_water else "без воды"
            print(f"Принято лекарство Аспирин в дозировке {self.dose} мг, {additional_info}")


    class paracetamol(drug):
        """
        Класс для Парацетамола, наследуется от Лекарство.
        """

        def __init__(self, dose: float, for_children: bool):
            super().__init__("Парацетамол", dose)
            self.for_children = for_children

        def __str__(self) -> str:
            category = "для детей" if self.for_children else "для взрослых"
            return super().__str__() + f", категория: {category}"

        def use(self) -> None:
            """
            Метод для имитации приема Парацетамола, унаследован от базового класса без изменений.
            """
            super().use()


    class coniferous_tree:
        """
        Базовый класс для хвойных деревьев.
        """

        def __init__(self, view: str, height: float):
            self.view = view
            self.height = height

        def __str__(self) -> str:
            return f"Хвойное дерево: {self.view}, высота: {self.height} м"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}('{self.view}', {self.height})"

        def grow(self) -> None:
            """
            Метод для имитации роста дерева.
            """
            self.height += 0.5
            print(f"{self.view} выросло до {self.height} м")


    class fir(coniferous_tree):
        """
        Класс для Ели, наследуется от ХвойноеДерево.
        """

        def __init__(self, height: float):
            super().__init__("Ель", height)

        def grow(self) -> None:
            """
            Метод для имитации роста Ели, перегружен для учета большей скорости роста.
            """
            self.height += 1
            print(f"Ель выросла до {self.height} м")


    class pine_tree(coniferous_tree):
        """
        Класс для Сосны, наследуется от ХвойноеДерево.
        """

        def __init__(self, height: float):
            super().__init__("Сосна", height)

        # Сосна использует метод расти без изменений от базового класса ХвойноеДерево.


    class hockey_League:
        """
        Базовый класс для хоккейных лиг.
        """

        def __init__(self, name: str, number_of_teams: int):
            self.name = name
            self.number_of_teams = number_of_teams

        def __str__(self) -> str:
            return f"Хоккейная лига: {self.name}, количество команд: {self.number_of_teams}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}('{self.name}', {self.number_of_teams})"

        def add_command(self) -> None:
            """
            Метод для имитации добавления команды в лигу.
            """
            self.number_of_teams += 1
            print(f"В лигу {self.name} добавлена новая команда. Теперь команд: {self.number_of_teams}")


    class SKA(hockey_League):
        """
        Класс для команды СКА, наследуется от ХоккейнаяЛига.
        """

        def __init__(self, number_players: int):
            super().__init__("СКА", number_players)

        # СКА использует методы базового класса без изменений.


    class AkBars(hockey_League):
        """
        Класс для команды Ак Барс, наследуется от ХоккейнаяЛига.
        """

        def __init__(self, number_players: int):
            super().__init__("Ак Барс", number_players)

        # Ак Барс использует методы базового класса без изменений.
    pass
