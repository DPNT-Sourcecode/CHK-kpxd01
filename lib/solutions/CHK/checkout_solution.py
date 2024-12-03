PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

SPECIAL_OFFERS = {
    "DISCOUNTS": {"A": [(3, 130), (5, 200)], "B": [(2, 45)]},
    "FREE": {"E": [(2, "B", 1)], "F": [(3, "F", 1)]},
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
            return {}
        item_counts[sku] = item_counts.get(sku, 0) + 1

    return item_counts


def apply_free_offers(item_counts):
    """Update the number of items based on free offers

    Args:
        item_counts (dict): dictionary containing the amount of items

    Returns:
        dict: dictionary containing the amount of items after applying free offers
    """
    # Copy the item counts as we will change the counts
    updated_counts = item_counts.copy()

    # Check only the items which can provide free items
    for item, offers in SPECIAL_OFFERS["FREE"].items():

        # For each item, we go through all the potential offers
        for offer in offers:

            # An free offer consists of the quantity of required items bought to trigger the offer,
            # the item which becomes free and the amount of items that become free per offer
            buy_quantity_offer, free_item, free_quantity = offer
            buy_count = item_counts.get(item, 0)
            orig_free_item_count = item_counts.get(free_item, 0)

            # Compute the times we can use the offer and then the total quantity of free items
            reduced_free_item_count = (buy_count // buy_quantity_offer) * free_quantity

            # The count cannot go under 0
            new_free_item_count = max(0, orig_free_item_count - reduced_free_item_count)

            # Update the count for the free item
            updated_counts[free_item] = new_free_item_count

    return updated_counts


def get_total_price(item_counts):
    """Return the total price for all the items, applying potential discounts

    Args:
        item_counts (dict): dictionary containing the amount of items

    Returns:
        int: an integer representing the total checkout value of the items
    """
    total_price = 0
    for item, count in item_counts.items():
        remaining = count

        # If the item is in the special offers, process special offer first
        if item in SPECIAL_OFFERS["DISCOUNTS"]:
            offers = SPECIAL_OFFERS["DISCOUNTS"][item]

            # Sort the orders from the most favorable to the least favorable
            sorted_offers = sorted(offers, key=lambda x: x[1] / x[0])
            for offer in sorted_offers:
                offer_quantity, offer_price = offer

                # Compute the amount of possible times we can use this offer
                n_offers = remaining // offer_quantity
                total_price += offer_price * n_offers
                remaining = remaining % offer_quantity

        total_price += remaining * PRICES[item]

    return total_price


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
    if len(skus) == 0:
        return 0

    item_counts = get_item_counts(skus)
    if len(item_counts) == 0:
        return -1

    # First check the items that could provide a free item if part of a special offer
    updated_counts = apply_free_offers(item_counts)

    # Process each item independently
    total_price = get_total_price(updated_counts)

    return total_price

