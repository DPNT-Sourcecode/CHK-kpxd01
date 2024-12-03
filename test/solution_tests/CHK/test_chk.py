from solutions.CHK import checkout_solution as cs


def test_get_item_counts():
    # Check one input
    assert cs.get_item_counts("A") == {"A": 1}
    assert cs.get_item_counts("B") == {"B": 1}

    # Check multiple inputs
    assert cs.get_item_counts("ABCDE") == {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 1,
        "E": 1,
    }
    assert cs.get_item_counts("AA") == {"A": 2}
    assert cs.get_item_counts("ABABA") == {"A": 3, "B": 2}
    assert cs.get_item_counts("AB") == {"A": 1, "B": 1}
    assert cs.get_item_counts("BA") == {"A": 1, "B": 1}
    assert cs.get_item_counts("AC") == {"A": 1, "C": 1}

    # Check invalid inputs
    assert cs.get_item_counts("F") == {}
    assert cs.get_item_counts("AF") == {}
    assert cs.get_item_counts("FA") == {}


def test_apply_free_offers():
    assert cs.apply_free_offers({"B": 0, "E": 2}) == {"B": 0, "E": 2}
    assert cs.apply_free_offers({"B": 1, "E": 2}) == {"B": 0, "E": 2}
    assert cs.apply_free_offers({"B": 2, "E": 2}) == {"B": 1, "E": 2}
    assert cs.apply_free_offers({"B": 1, "E": 4}) == {"B": 0, "E": 4}
    assert cs.apply_free_offers({"B": 2, "E": 4}) == {"B": 0, "E": 4}
    assert cs.apply_free_offers({"B": 3, "E": 4}) == {"B": 1, "E": 4}
    assert cs.apply_free_offers({"A": 2, "B": 3, "E": 4}) == {"A": 2, "B": 1, "E": 4}

    assert cs.apply_free_offers({"F": 2}) == {"F": 2}
    assert cs.apply_free_offers({"F": 3}) == {"F": 2}
    assert cs.apply_free_offers({"F": 4}) == {"F": 3}


def test_get_total_price():
    assert cs.get_total_price({"A": 1}) == 50
    assert cs.get_total_price({"B": 1}) == 30
    assert cs.get_total_price({"C": 1}) == 20
    assert cs.get_total_price({"D": 1}) == 15
    assert cs.get_total_price({"E": 1}) == 40

    assert cs.get_total_price({"A": 3}) == 130
    assert cs.get_total_price({"A": 4}) == 180
    assert cs.get_total_price({"A": 5}) == 200
    assert cs.get_total_price({"A": 6}) == 250
    assert cs.get_total_price({"A": 8}) == 330
    assert cs.get_total_price({"A": 10}) == 400
    assert cs.get_total_price({"B": 2}) == 45
    assert cs.get_total_price({"B": 3}) == 75
    assert cs.get_total_price({"B": 4}) == 90

    assert cs.get_total_price({"A": 1, "B": 1, "C": 1, "D": 1, "E": 1}) == 155


def test_single_items():
    assert cs.checkout("A") == 50
    assert cs.checkout("B") == 30
    assert cs.checkout("C") == 20
    assert cs.checkout("D") == 15
    assert cs.checkout("E") == 40


def test_invalid_input():
    assert cs.checkout(None) == -1
    assert cs.checkout(0) == -1
    assert cs.checkout("a") == -1
    assert cs.checkout("0") == -1
    assert cs.checkout("Aa") == -1
    assert cs.checkout("aA") == -1


def test_empty_basket():
    assert cs.checkout("") == 0


def test_multiple_items_no_special_offers():
    assert cs.checkout("AB") == 80
    assert cs.checkout("ABCDE") == 155


def test_special_offer_discount():
    assert cs.checkout("AAA") == 130
    assert cs.checkout("AAAAA") == 200
    assert cs.checkout("BB") == 45

    assert cs.checkout("AAAA") == 180
    assert cs.checkout("AAAAAA") == 250
    assert cs.checkout("AAAAAAAA") == 330
    assert cs.checkout("AAAAAAAAA") == 380
    assert cs.checkout("AAAAAAAAAA") == 400
    assert cs.checkout("BBB") == 75

    assert cs.checkout("AAAC") == 150
    assert cs.checkout("AAAAAD") == 215
    assert cs.checkout("AAAAAAAAE") == 370
    assert cs.checkout("AAABB") == 175
    assert cs.checkout("AAAABBB") == 255
    assert cs.checkout("AAAABBB") == 255


def test_multiple_items_special_offers():
    assert cs.checkout("AAAC") == 150
    assert cs.checkout("AAAAD") == 195
    assert cs.checkout("AAABB") == 175
    assert cs.checkout("AAAABBB") == 255


def test_free_items():
    assert cs.checkout("EE") == 80
    assert cs.checkout("EEB") == 80
    assert cs.checkout("EEBB") == 110
    assert cs.checkout("EEEEB") == 160
    assert cs.checkout("EEEEBB") == 160
    assert cs.checkout("EEEEBBB") == 190


def test_mixed_offers():
    assert cs.checkout("AAABEE") == 210
    assert cs.checkout("AAAAABEE") == 280
    assert cs.checkout("BBBEE") == 125

