import random
from datetime import datetime

from faker import Faker

from app.data.utils import beverages, ingredients, sizes

faker = Faker()


def generate_client_data():
    client_data = {
        'client_name': faker.name(),
        'client_dni': faker.ssn(),
        'client_address': faker.address(),
        'client_phone': faker.phone_number()
    }

    return client_data


def generate_sizes():
    sizes_list = [{'name': size, 'price': round(random.uniform(5, 20), 1)} for size in sizes]
    return sizes_list


def generate_ingredients():
    ingredients_list = [{'name': ingredient, 'price': round(
        random.uniform(0.5, 5), 1)} for ingredient in ingredients]
    return ingredients_list


def generate_beverages():
    beverages_list = [{'name': beverage, 'price': round(random.uniform(1, 10), 1)} for beverage in beverages]
    return beverages_list


def generate_orders(sizes, ingredients, beverages):
    customers = [generate_client_data() for _ in range(15)]
    orders = []
    for _ in range(100):
        customer = random.choice(customers)
        size = random.choice(sizes)
        ingredient_ids = [ingredient['_id']
                          for ingredient in random.sample(ingredients, random.randint(2, 4))]
        beverage_ids = [beverage['_id'] for beverage in random.sample(beverages, random.randint(1, 3))]
        order_data = {
            **customer,
            'date': faker.date_time_between(start_date=datetime(2024, 1, 1), end_date="now"),
            'size_id': size['_id'],
            'ingredients': ingredient_ids,
            'beverages': beverage_ids,
        }

        orders.append(order_data)
    return orders
