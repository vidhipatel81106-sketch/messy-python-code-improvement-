"""Readable version of the item-quantity example."""


def total_quantity(items):
    """Add the quantities from a list of (item_name, quantity) pairs."""
    return sum(quantity for _item_name, quantity in items)


if __name__ == "__main__":
    items = [("pen", 2), ("book", 3), ("bag", 1)]
    quantity = total_quantity(items)
    print(f"Total quantity: {quantity}")
