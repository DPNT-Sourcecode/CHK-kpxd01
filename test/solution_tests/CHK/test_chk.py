from solutions.CHK import checkout_solution as cs


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


def test_apply_free_offers():
    assert cs.apply_free_offers({"B": 0, "E": 2}) == {"B": 0, "E": 2}
    assert cs.apply_free_offers({"B": 1, "E": 2}) == {"B": 0, "E": 2}
    assert cs.apply_free_offers({"B": 2, "E": 2}) == {"B": 1, "E": 2}
    assert cs.apply_free_offers({"B": 1, "E": 4}) == {"B": 0, "E": 4}
    assert cs.apply_free_offers({"B": 2, "E": 4}) == {"B": 0, "E": 4}
    assert cs.apply_free_offers({"B": 3, "E": 4}) == {"B": 1, "E": 4}
    assert cs.apply_free_offers({"A": 2, "B": 3, "E": 4}) == {"A": 2, "B": 1, "E": 4}


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





