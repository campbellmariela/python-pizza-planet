from sqlalchemy.exc import SQLAlchemyError

from app.common.utils import check_required_keys
from app.controllers.base import BaseController
from app.controllers.order.order_builder import OrderBuilder
from app.repositories.managers import OrderManager


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        ingredient_ids = current_order.pop('ingredients', [])
        beverage_ids = current_order.pop('beverages', [])

        try:
            order_builder = OrderBuilder()
            order_builder.set_size(size_id)
            order_builder.add_ingredients(ingredient_ids)
            order_builder.add_beverages(beverage_ids)
            built_order, ingredients, beverages = order_builder.build()
            return cls.manager.create(
                {**current_order, **built_order},
                ingredients,
                beverages
            ), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
