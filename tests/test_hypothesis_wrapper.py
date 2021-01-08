"""Democritus functions to interact with Hypothesis."""

import ipaddress

from hypothesis.provisional import ip4_addr_strings

from democritus_hypothesis import hypothesis_get_strategy_results


def is_ip_address(text: str) -> bool:
    """Determine whether or not the given text is an ip address."""
    try:
        ipaddress.ip_address(text)
    except ValueError:
        return False
    else:
        return True


def test_hypothesis_get_strategy_results_dates():
    results = hypothesis_get_strategy_results(ip4_addr_strings)
    assert len(results) == 10
    for result in results:
        assert is_ip_address(result)

    # try specifying a specific number
    results = hypothesis_get_strategy_results(ip4_addr_strings, n=12)
    assert len(results) == 12
    for result in results:
        assert is_ip_address(result)
