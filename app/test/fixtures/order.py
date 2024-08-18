import pytest

from app.controllers.order.order_builder import OrderBuilder

from ..utils.functions import (get_random_phone, get_random_sequence,
                               get_random_string, shuffle_list)


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_phone()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def mock_order_builder(create_size, create_ingredients, create_beverages):
    size = create_size.json
    ingredients = create_ingredients
    beverages = create_beverages

    size_id = size['_id']
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients]
    beverage_ids = [beverage['_id'] for beverage in beverages]

    order_builder = OrderBuilder()
    order_builder.set_size(size_id)
    order_builder.add_ingredients(ingredient_ids)
    order_builder.add_beverages(beverage_ids)
    return {
        'order_builder': order_builder,
        'size': size,
        'ingredients': ingredients,
        'beverages': beverages
    }


@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_size, create_beverages) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    size_id = create_size.json.get('_id')
    beverages = [beverage.get('_id') for beverage in create_beverages]
    order = client.post(order_uri, json={
        **client_data_mock(),
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverages
    })
    return order


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_sizes, create_beverages) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    sizes = [size.get('_id') for size in create_sizes]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'ingredients': shuffle_list(ingredients)[:5],
            'size_id': shuffle_list(sizes)[0],
            'beverages': shuffle_list(beverages)[:5]
        })
        orders.append(new_order)
    return orders
