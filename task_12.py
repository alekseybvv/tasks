class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name  
        self._calories = calories

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_calories(self):
        return self._calories

    def set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        if self._calories is not None and self._calories < 200:
            return True
        return False

    def is_delicious(self):
        return True


# Класс JellyBean, расширяющий класс Dessert
class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)  # Инициализируем родительский класс
        self._flavor = flavor

    # Геттер для flavor
    def get_flavor(self):
        return self._flavor

    # Сеттер для flavor
    def set_flavor(self, flavor):
        self._flavor = flavor

    # Переопределение метода is_delicious
    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True


jellybean = JellyBean("Jelly Bean", 150, "black licorice")

print("Название:", jellybean.get_name())
print("Калорийность:", jellybean.get_calories())
print("Вкус:", jellybean.get_flavor())
print(jellybean.is_healthy())  # True
print(jellybean.is_delicious())  # False
