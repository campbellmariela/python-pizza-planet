from typing import Any, Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError

from app.repositories.managers import ReportManager


class ReportController:
    manager = ReportManager

    @classmethod
    def get_report(cls) -> Tuple[Any, Optional[str]]:
        try:
            return {
                "most_requested_ingredient": cls.get_most_requested_ingredient(),
                "month_with_most_revenue": cls.get_month_with_most_revenue(),
                "top_customers": cls.get_top_customers()
            }, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_most_requested_ingredient(cls):
        result = cls.manager.get_most_requested_ingredient()
        return {
            'ingredient_name': result[0],
            'total_orders': result[1]
        }

    @classmethod
    def get_month_with_most_revenue(cls):
        result = cls.manager.get_month_with_most_revenue()
        return {
            'month': result[0],
            'revenue': round(result[1], 2)
        }

    @classmethod
    def get_top_customers(cls):
        result = cls.manager.get_top_customers()
        return [
            {
                'client_name': row[0],
                'total_orders': row[1]
            } for row in result
        ]
