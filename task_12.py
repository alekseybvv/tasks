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
        if self._calories is not None:
            try:
                calories = float(self._calories)  
                if calories < 200:
                    return True
            except (ValueError, TypeError): 
                pass
        return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor

    def set_flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True



