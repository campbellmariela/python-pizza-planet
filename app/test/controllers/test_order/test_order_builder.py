import pytest


def test_set_size(mock_order_builder):
    order_builder = mock_order_builder['order_builder']
    size = mock_order_builder['size']

    pytest.assume(order_builder.size_id == size['_id'])
    pytest.assume(order_builder.size_price == size['price'])


def test_add_ingredients(mock_order_builder):
    order_builder = mock_order_builder['order_builder']
    ingredients = mock_order_builder['ingredients']

    pytest.assume(len(order_builder.ingredients) == len(ingredients))
    pytest.assume(order_builder.ingredients_price == sum(ingredient['price'] for ingredient in ingredients))


def test_add_beverages(mock_order_builder):
    order_builder = mock_order_builder['order_builder']
    beverages = mock_order_builder['beverages']

    pytest.assume(len(order_builder.beverages) == len(beverages))
    pytest.assume(order_builder.beverages_price == sum(beverage['price'] for beverage in beverages))


def test_calculate_total_price(mock_order_builder):
    order_builder = mock_order_builder['order_builder']
    size = mock_order_builder['size']
    ingredients = mock_order_builder['ingredients']
    beverages = mock_order_builder['beverages']

    expected_total_price = round(
        size['price'] +
        sum(ingredient['price'] for ingredient in ingredients) +
        sum(beverage['price'] for beverage in beverages), 2
    )

    pytest.assume(order_builder.calculate_total_price() == expected_total_price)
