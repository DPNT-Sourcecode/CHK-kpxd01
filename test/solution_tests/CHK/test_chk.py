from solutions.CHK import checkout_solution as cs


def test_get_item_counts():
    # Check one input
    assert cs.get_item_counts("A") == {"A": 1}
    assert cs.get_item_counts("B") == {"B": 1}

    # Check multiple inputs
    assert cs.get_item_counts("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 1,
        "E": 1,
        "F": 1,
        "G": 1,
        "H": 1,
        "I": 1,
        "J": 1,
        "K": 1,
        "L": 1,
        "M": 1,
        "N": 1,
        "O": 1,
        "P": 1,
        "Q": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 1,
        "W": 1,
        "X": 1,
        "Y": 1,
        "Z": 1,
    }
    assert cs.get_item_counts("AA") == {"A": 2}
    assert cs.get_item_counts("ABABA") == {"A": 3, "B": 2}
    assert cs.get_item_counts("AB") == {"A": 1, "B": 1}
    assert cs.get_item_counts("BA") == {"A": 1, "B": 1}
    assert cs.get_item_counts("AC") == {"A": 1, "C": 1}

    # Check invalid inputs
    assert cs.get_item_counts("a") == {}
    assert cs.get_item_counts("Aa") == {}
    assert cs.get_item_counts("aA") == {}


def test_apply_free_offers():
    assert cs.apply_free_offers({"B": 0, "E": 2}) == {"B": 0, "E": 2}
    assert cs.apply_free_offers({"B": 1, "E": 2}) == {"B": 0, "E": 2}
    assert cs.apply_free_offers({"B": 2, "E": 2}) == {"B": 1, "E": 2}
    assert cs.apply_free_offers({"B": 1, "E": 4}) == {"B": 0, "E": 4}
    assert cs.apply_free_offers({"B": 2, "E": 4}) == {"B": 0, "E": 4}
    assert cs.apply_free_offers({"B": 3, "E": 4}) == {"B": 1, "E": 4}

    assert cs.apply_free_offers({"F": 2}) == {"F": 2}
    assert cs.apply_free_offers({"F": 3}) == {"F": 2}
    assert cs.apply_free_offers({"F": 4}) == {"F": 3}
    assert cs.apply_free_offers({"F": 5}) == {"F": 4}
    assert cs.apply_free_offers({"F": 6}) == {"F": 4}

    assert cs.apply_free_offers({"M": 1, "N": 2}) == {"M": 1, "N": 2}
    assert cs.apply_free_offers({"M": 1, "N": 3}) == {"M": 0, "N": 3}
    assert cs.apply_free_offers({"M": 1, "N": 4}) == {"M": 0, "N": 4}
    assert cs.apply_free_offers({"M": 2, "N": 3}) == {"M": 1, "N": 3}
    assert cs.apply_free_offers({"M": 3, "N": 6}) == {"M": 1, "N": 6}

    assert cs.apply_free_offers({"Q": 1, "R": 2}) == {"Q": 1, "R": 2}
    assert cs.apply_free_offers({"Q": 1, "R": 3}) == {"Q": 0, "R": 3}
    assert cs.apply_free_offers({"Q": 1, "R": 4}) == {"Q": 0, "R": 4}
    assert cs.apply_free_offers({"Q": 2, "R": 3}) == {"Q": 1, "R": 3}
    assert cs.apply_free_offers({"Q": 3, "R": 6}) == {"Q": 1, "R": 6}

    assert cs.apply_free_offers({"U": 3}) == {"U": 3}
    assert cs.apply_free_offers({"U": 4}) == {"U": 3}
    assert cs.apply_free_offers({"U": 5}) == {"U": 4}
    assert cs.apply_free_offers({"U": 6}) == {"U": 5}
    assert cs.apply_free_offers({"U": 7}) == {"U": 6}
    assert cs.apply_free_offers({"U": 8}) == {"U": 6}

    assert cs.apply_free_offers({"A": 2, "B": 3, "E": 4}) == {"A": 2, "B": 1, "E": 4}


def test_get_total_price():
    assert cs.get_total_price({"A": 1}) == 50
    assert cs.get_total_price({"B": 1}) == 30
    assert cs.get_total_price({"C": 1}) == 20
    assert cs.get_total_price({"D": 1}) == 15
    assert cs.get_total_price({"E": 1}) == 40
    assert cs.get_total_price({"F": 1}) == 10
    assert cs.get_total_price({"G": 1}) == 20
    assert cs.get_total_price({"H": 1}) == 10
    assert cs.get_total_price({"I": 1}) == 35
    assert cs.get_total_price({"J": 1}) == 60
    assert cs.get_total_price({"K": 1}) == 80
    assert cs.get_total_price({"L": 1}) == 90
    assert cs.get_total_price({"M": 1}) == 15
    assert cs.get_total_price({"N": 1}) == 40
    assert cs.get_total_price({"O": 1}) == 10
    assert cs.get_total_price({"P": 1}) == 50
    assert cs.get_total_price({"Q": 1}) == 30
    assert cs.get_total_price({"R": 1}) == 50
    assert cs.get_total_price({"S": 1}) == 30
    assert cs.get_total_price({"T": 1}) == 20
    assert cs.get_total_price({"U": 1}) == 40
    assert cs.get_total_price({"V": 1}) == 50
    assert cs.get_total_price({"W": 1}) == 20
    assert cs.get_total_price({"X": 1}) == 90
    assert cs.get_total_price({"Y": 1}) == 10
    assert cs.get_total_price({"Z": 1}) == 50

    assert cs.get_total_price({"A": 3}) == 130
    assert cs.get_total_price({"A": 4}) == 180
    assert cs.get_total_price({"A": 5}) == 200
    assert cs.get_total_price({"A": 6}) == 250
    assert cs.get_total_price({"A": 8}) == 330
    assert cs.get_total_price({"A": 10}) == 400
    assert cs.get_total_price({"B": 2}) == 45
    assert cs.get_total_price({"B": 3}) == 75
    assert cs.get_total_price({"B": 4}) == 90
    assert cs.get_total_price({"E": 2}) == 80
    assert cs.get_total_price({"E": 3, "B": 1}) == 120
    assert cs.get_total_price({"F": 2}) == 10
    assert cs.get_total_price({"F": 3}) == 10
    assert cs.get_total_price({"F": 4}) == 20
    assert cs.get_total_price({"H": 5}) == 45
    assert cs.get_total_price({"H": 7}) == 65
    assert cs.get_total_price({"H": 10}) == 80
    assert cs.get_total_price({"K": 2}) == 150
    assert cs.get_total_price({"K": 3}) == 230
    assert cs.get_total_price({"N": 3, "M": 1}) == 120
    assert cs.get_total_price({"N": 6, "M": 2}) == 240
    assert cs.get_total_price({"P": 5}) == 200
    assert cs.get_total_price({"P": 6}) == 250
    assert cs.get_total_price({"Q": 3}) == 80
    assert cs.get_total_price({"Q": 4}) == 110
    assert cs.get_total_price({"R": 3, "Q": 1}) == 150
    assert cs.get_total_price({"R": 6, "Q": 2}) == 300
    assert cs.get_total_price({"U": 3}) == 80
    assert cs.get_total_price({"U": 4}) == 120
    assert cs.get_total_price({"V": 2}) == 90
    assert cs.get_total_price({"V": 3}) == 130
    assert cs.get_total_price({"V": 4}) == 180

    assert cs.get_total_price({"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1}) == 165


def test_single_items():
    assert cs.checkout("A") == 50
    assert cs.checkout("B") == 30
    assert cs.checkout("C") == 20
    assert cs.checkout("D") == 15
    assert cs.checkout("E") == 40
    assert cs.checkout("F") == 10
    assert cs.checkout("G") == 20
    assert cs.checkout("H") == 10
    assert cs.checkout("I") == 35
    assert cs.checkout("J") == 60
    assert cs.checkout("K") == 80
    assert cs.checkout("L") == 90
    assert cs.checkout("M") == 15
    assert cs.checkout("N") == 40
    assert cs.checkout("O") == 10
    assert cs.checkout("P") == 50
    assert cs.checkout("Q") == 30
    assert cs.checkout("R") == 50
    assert cs.checkout("S") == 30
    assert cs.checkout("T") == 20
    assert cs.checkout("U") == 40
    assert cs.checkout("V") == 50
    assert cs.checkout("W") == 20
    assert cs.checkout("X") == 90
    assert cs.checkout("Y") == 10
    assert cs.checkout("Z") == 50


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
    assert cs.checkout("ABCDEF") == 165


def test_special_offer_discount():
    assert cs.checkout("AAA") == 130
    assert cs.checkout("AAAA") == 180
    assert cs.checkout("AAAAA") == 200
    assert cs.checkout("AAAAAA") == 250
    assert cs.checkout("AAAAAAA") == 300
    assert cs.checkout("BBBB") == 90
    assert cs.checkout("HHHHH") == 45
    assert cs.checkout("HHHHHH") == 55
    assert cs.checkout("HHHHHHHHHH") == 80
    assert cs.checkout("KK") == 150
    assert cs.checkout("PPPPP") == 200
    assert cs.checkout("QQQ") == 80
    assert cs.checkout("VV") == 90
    assert cs.checkout("VVV") == 130


def test_multiple_items_special_offers():
    assert cs.checkout("AAAC") == 150
    assert cs.checkout("AAAAD") == 195
    assert cs.checkout("AAABB") == 175
    assert cs.checkout("AAAABBB") == 255
    assert cs.checkout("AABBBCC") == 215
    assert cs.checkout("AAAAAACCCCC") == 350


def test_free_items():
    assert cs.checkout("EE") == 80
    assert cs.checkout("EEB") == 80
    assert cs.checkout("EEBB") == 110
    assert cs.checkout("FFFF") == 30
    assert cs.checkout("FFFFFF") == 40
    assert cs.checkout("UUU") == 120
    assert cs.checkout("UUUU") == 120
    assert cs.checkout("NNN") == 120
    assert cs.checkout("NNNM") == 120
    assert cs.checkout("RRR") == 150
    assert cs.checkout("RRRQ") == 150


def test_combined_discounts():
    assert cs.checkout("EEFFFF") == 110
    assert cs.checkout("AAABEE") == 210
    assert cs.checkout("AAAAABEE") == 280
    assert cs.checkout("AAAFFF") == 150
    assert cs.checkout("UUUBBB") == 155
    assert cs.checkout("NNNMMM") == 150
    assert cs.checkout("RRRQQQ") == 230
    assert cs.checkout("KKVVVVV") == 370
    assert cs.checkout("PPPPPGGG") == 260

