from flask import Blueprint

from app.common.http_methods import GET, POST, PUT
from app.services.base import BaseService

from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return BaseService.create(SizeController)


@size.route('/', methods=PUT)
def update_size():
    return BaseService.update(SizeController)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return BaseService.get_by_id(SizeController, _id)


@size.route('/', methods=GET)
def get_sizes():
    return BaseService.get_all(SizeController)
