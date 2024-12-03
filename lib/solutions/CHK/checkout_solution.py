import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "pricing_config.json")
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)


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
        if sku not in config["prices"]:
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
    for item, offers in config["specialOffers"]["freeItems"].items():

        if item in updated_counts:

            # For each item, we go through all the potential offers
            for offer in offers:

                # An free offer consists of the quantity of required items bought to trigger the offer,
                # the item which becomes free and the amount of items that become free per offer
                buy_quantity = offer["buyQuantity"]
                free_item = offer["freeItem"]
                free_quantity = offer["freeQuantity"]
                buy_count = updated_counts.get(item, 0)
                orig_free_item_count = updated_counts.get(free_item, 0)

                # Compute the times we can use the offer and then the total quantity of free items
                reduced_free_item_count = (buy_count // buy_quantity) * free_quantity

                # The count cannot go under 0
                new_free_item_count = max(
                    0, orig_free_item_count - reduced_free_item_count
                )

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
    single_discounts = config["specialOffers"]["singleDiscounts"]
    grouped_discounts = config["specialOffers"]["groupedDiscounts"]

    for grouped_discount in grouped_discounts:
        group_items = grouped_discount["itemsIncluded"]
        group_quantity = grouped_discount["quantity"]
        group_price = grouped_discount["price"]

        group_counts = [(item, item_counts.get(item, 0)) for item in group_items]
        sorted_group_counts = sorted(group_counts, key=lambda x: x[1], reverse=True)

        total_items_group = sum(count for _, count in group_counts)
        total_groups = total_items_group // group_quantity

        total_remaining = total_groups * group_quantity
        for item, count in sorted_group_counts:
            if total_remaining == 0:
                break

            items_used = min(count, total_remaining)
            total_remaining -= items_used
            item_counts[item] -= items_used

        total_price += total_groups * group_price

    for item, count in item_counts.items():
        remaining = count

        # If the item is in the special offers, process special offer first
        if item in single_discounts:
            offers = single_discounts[item]

            # Sort the orders from the most favorable to the least favorable
            sorted_offers = sorted(offers, key=lambda x: x["price"] / x["quantity"])
            for offer in sorted_offers:
                offer_quantity = offer["quantity"]
                offer_price = offer["price"]

                # Compute the amount of possible times we can use this offer
                n_offers = remaining // offer_quantity
                total_price += offer_price * n_offers
                remaining = remaining % offer_quantity

        total_price += remaining * config["prices"][item]

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

