import pytest

from app.controllers.report import ReportController


def test_get_report(client, create_orders, create_beverages, create_ingredients, create_sizes):
    report, error = ReportController.get_report()
    pytest.assume(error is None)
    pytest.assume(report)
    pytest.assume('most_requested_ingredient' in report)
    pytest.assume('month_with_most_revenue' in report)
    pytest.assume('top_customers' in report)


def test_get_most_requested_ingredient(client, create_orders, create_ingredients):
    most_requested_ingredient = ReportController.get_most_requested_ingredient()
    pytest.assume(most_requested_ingredient)
    pytest.assume('ingredient_name' in most_requested_ingredient)
    pytest.assume('total_orders' in most_requested_ingredient)


def test_get_month_with_most_revenue(client, create_orders):
    month_with_most_revenue = ReportController.get_month_with_most_revenue()
    pytest.assume(month_with_most_revenue)
    pytest.assume('month' in month_with_most_revenue)
    pytest.assume('revenue' in month_with_most_revenue)


def test_get_top_customers(client, create_orders):
    top_customers = ReportController.get_top_customers()
    pytest.assume(isinstance(top_customers, list))
    pytest.assume(len(top_customers) > 0)
    for customer in top_customers:
        pytest.assume('client_name' in customer)
        pytest.assume('total_orders' in customer)
