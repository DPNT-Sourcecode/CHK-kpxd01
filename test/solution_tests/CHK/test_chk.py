from solutions.CHK import checkout_solution as cs


def test_single_items():
    assert cs.checkout("A") == 50
    assert cs.checkout("B") == 30
    assert cs.checkout("C") == 20
    assert cs.checkout("D") == 15


def test_invalid_input():
    assert cs.checkout(None) == -1
    assert cs.checkout("E") == -1
    assert cs.checkout(0) == -1
    assert cs.checkout("a") == -1
    assert cs.checkout("Aa") == -1
    assert cs.checkout("aA") == -1


def test_empty_string():
    assert cs.checkout("") == 0


def test_multiple_items_no_special_offers():
    assert cs.checkout("AB") == 80
    assert cs.checkout("ABCD") == 115



