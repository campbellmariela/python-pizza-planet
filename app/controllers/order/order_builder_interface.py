from abc import abstractmethod


class OrderBuilderInterface():

    @abstractmethod
    def set_size(self, size_id: int):
        pass

    @abstractmethod
    def add_ingredients(self, ingredient_ids: list):
        pass

    @abstractmethod
    def add_beverages(self, beverage_ids: list):
        pass

    @abstractmethod
    def build(self):
        pass
