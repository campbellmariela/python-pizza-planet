from app.repositories.managers import (BeverageManager, IngredientManager,
                                       SizeManager)

from .order_builder_interface import OrderBuilderInterface


class OrderBuilder(OrderBuilderInterface):
    def __init__(self):
        self.size_id = None
        self.ingredients = []
        self.beverages = []
        self.size_price = 0
        self.ingredients_price = 0
        self.beverages_price = 0

    def set_size(self, size_id: int):
        size = SizeManager.get_by_id(size_id)
        self.size_id = size_id
        self.size_price = size.get('price')
        return self

    def add_ingredients(self, ingredient_ids: list):
        self.ingredients = IngredientManager.get_by_id_list(ingredient_ids)
        self.ingredients_price = sum(ingredient.price for ingredient in self.ingredients)
        return self

    def add_beverages(self, beverage_ids: list):
        self.beverages = BeverageManager.get_by_id_list(beverage_ids)
        self.beverages_price = sum(beverage.price for beverage in self.beverages)
        return self

    def calculate_total_price(self):
        total_price = round(self.size_price + self.ingredients_price + self.beverages_price, 2)
        return total_price

    def build(self):
        order_data = {
            'size_id': self.size_id,
            'total_price': self.calculate_total_price()
        }
        return order_data, self.ingredients, self.beverages
