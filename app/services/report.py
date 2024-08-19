from flask import Blueprint

from app.common.http_methods import GET
from app.services.base import BaseService

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return BaseService.get_report(ReportController)
