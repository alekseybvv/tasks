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


dessert = Dessert("twix", 200)

print("Название:", dessert.get_name())
print("Калорийность:", dessert.get_calories())

print(dessert.is_healthy())  
print(dessert.is_delicious())  
