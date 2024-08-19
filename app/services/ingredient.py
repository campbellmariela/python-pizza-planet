from flask import Blueprint

from app.common.http_methods import GET, POST, PUT
from app.services.base import BaseService

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return BaseService.create(IngredientController)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return BaseService.update(IngredientController)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return BaseService.get_by_id(IngredientController, _id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return BaseService.get_all(IngredientController)
