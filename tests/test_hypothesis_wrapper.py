"""Democritus functions to interact with Hypothesis."""

from hypothesis.strategies import dates
from democritus_dates import is_date

from democritus_hypothesis import hypothesis_get_strategy_results


def test_hypothesis_get_strategy_results_dates():
    results = hypothesis_get_strategy_results(dates)
    assert len(results) == 10
    for result in results:
        assert is_date(result)

    # try specifying a specific number
    results = hypothesis_get_strategy_results(dates, n=12)
    assert len(results) == 12
    for result in results:
        assert is_date(result)
