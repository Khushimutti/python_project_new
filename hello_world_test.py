import pytest

def capital_case(x):
    return x.capitalize()
@pytest.mark.skip("reason=Skipping this test case")
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
