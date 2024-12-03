from solutions.CHK import checkout_solution


def test_single_items():
    assert checkout_solution.checkout("A") == 50
    assert checkout_solution.checkout("B") == 30
    assert checkout_solution.checkout("C") == 20
    assert checkout_solution.checkout("D") == 15
