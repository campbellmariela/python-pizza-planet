import pytest


def test_get_report(client, create_orders, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    report = response.json
    pytest.assume('most_requested_ingredient' in report)
    pytest.assume('month_with_most_revenue' in report)
    pytest.assume('top_customers' in report)
    pytest.assume(isinstance(report['most_requested_ingredient'], dict))
    pytest.assume(isinstance(report['month_with_most_revenue'], dict))
    pytest.assume(isinstance(report['top_customers'], list))
