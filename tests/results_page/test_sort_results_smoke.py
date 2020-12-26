import pytest
from pages.results_page import ResultsPage


@pytest.fixture(scope='module')
def setup(driver_setup):
    results_page = ResultsPage(driver_setup)
    return results_page


@pytest.mark.parametrize("sort_by",
                         [pytest.param('Relevance', marks=pytest.mark.tcid10),
                          pytest.param('Newness', marks=pytest.mark.tcid11),
                          pytest.param('Price Ascending', marks=pytest.mark.tcid12),
                          pytest.param('Price Descending', marks=pytest.mark.tcid13),
                          ])
def test_sort_results_by(setup, sort_by):
    results_page = setup
    product_name = "shirt"
    results_page.search(product_name)
    results_page.sort_results(by=sort_by)
    assert results_page.verify_sorted(by=sort_by)
    if AssertionError:
        results_page.driver.take_screenshot(name="test_sort_results_by")