PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

SPECIAL_OFFERS = {
    "DISCOUNTS": {"A": [(3, 130), (5, 200)], "B": [(2, 45)]},
    "FREE": {"E": [(2, "B", 1)]},
}


def get_item_counts(skus):
    """Count occurrences of each item in skus

    Args:
        skus (str): a string containing the SKUs of all the products in the basket

    Returns:
        dict: dictionary containing the amount of items in skus
    """
    item_counts = {}
    for sku in skus:
        # If sku is not in PRICES -> illegal input
        if sku not in PRICES:
            return -1
        item_counts[sku] = item_counts.get(sku, 0) + 1

    return item_counts


def apply_free_offers(item_counts):
    updated_counts = item_counts.copy()
    for item, offers in SPECIAL_OFFERS["FREE"].items():
        for offer in offers:
            buy_quantity_offer, free_item, free_quantity = offer
            buy_count = item_counts.get(item, 0)
            orig_free_item_count = item_counts.get(free_item, 0)
            reduced_free_item_count = (buy_count // buy_quantity_offer) * free_quantity
            new_free_item_count = max(0, orig_free_item_count - reduced_free_item_count)
            updated_counts[free_item] = new_free_item_count

    return updated_counts


def checkout(skus):
    """Calculate the total price of a number of items

    Args:
        skus (str): a string containing the SKUs of all the products in the basket

    Returns:
        int: an integer representing the total checkout value of the items, returns -1 if illegal input
    """
    item_counts = {}

    # If skus is None -> illegal input
    if skus is None:
        return -1

    # If skus is not a string -> illegal input
    if not isinstance(skus, str):
        return -1

    # Count occurrences of each in skus
    item_counts = get_item_counts(skus)

    total_price = 0

    # First check the items that could provide a free item if part of a special offer
    updated_counts = apply_free_offers(item_counts)

    # Process each item independently
    for item, count in updated_counts.items():
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




