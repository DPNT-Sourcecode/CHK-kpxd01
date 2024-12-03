PRICES = {"A": 50, "B": 30, "C": 20, "D": 15}

SPECIAL_OFFERS = {"A": (3, 130), "B": (2, 45)}


def checkout(skus):
    item_counts = {}
    for sku in skus:
        if sku not in PRICES:
            return -1
        item_counts[sku] = item_counts[sku].get(sku, 0) + 1

    total_price = 0

    for item, count in item_counts.items():
        if item in SPECIAL_OFFERS:
            offer_quantity, offer_price = SPECIAL_OFFERS[item]
            n_offers = count // offer_quantity
            total_price += offer_price * n_offers
            remaining = count % offer_quantity
            total_price += remaining * PRICES[item]
        else:
            total_price += count * PRICES[item]

    return total_price

