from app.controllers import (BeverageController, IngredientController,
                             OrderController, SizeController)
from app.data.generate_data import (generate_beverages, generate_ingredients,
                                    generate_orders, generate_sizes)


def create_sizes():
    sizes_data = generate_sizes()
    sizes = [SizeController.create(data)[0] for data in sizes_data]
    return sizes


def create_ingredients():
    ingredients_data = generate_ingredients()
    ingredients = [IngredientController.create(data)[0] for data in ingredients_data]
    return ingredients


def create_beverages():
    beverages_data = generate_beverages()
    beverages = [BeverageController.create(data)[0] for data in beverages_data]
    return beverages


def create_orders(sizes, ingredients, beverages):
    orders = generate_orders(sizes, ingredients, beverages)
    for order_data in orders:
        OrderController.create(order_data)


def populate_database():
    sizes = create_sizes()
    ingredients = create_ingredients()
    beverages = create_beverages()
    create_orders(sizes, ingredients, beverages)
