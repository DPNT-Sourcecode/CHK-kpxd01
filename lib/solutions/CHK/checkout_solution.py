PRICES = {"A": 50, "B": 30, "C": 20, "D": 15}

SPECIAL_OFFERS = {"A": (3, 130), "B": (2, 45)}


def checkout(skus):
    # Count occurrences of each item in skus
    item_counts = {}

    # If skus is None -> illegal input
    if skus is None:
        return -1

    # If skus is not a string -> illegal input
    if not isinstance(skus, str):
        return -1

    for sku in skus:
        # If sku is not in PRICES -> illegal input
        if sku not in PRICES:
            return -1
        item_counts[sku] = item_counts.get(sku, 0) + 1

    total_price = 0

    # Process each item independently
    for item, count in item_counts.items():
        # If the item is in the special offers, process special offer first
        if item in SPECIAL_OFFERS:
            offer_quantity, offer_price = SPECIAL_OFFERS[item]

            # Compute the amount of possible special offers for this item
            n_offers = count // offer_quantity
            total_price += offer_price * n_offers

            # Add the remaining items not included in the special offer if necessary
            remaining = count % offer_quantity
            total_price += remaining * PRICES[item]
        # Process the item with no special offer
        else:
            total_price += count * PRICES[item]

    return total_price


