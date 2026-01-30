"""The purpose of this notebook is to manage fruit data for our distribution center
We will be defining tuples, storing and updating fruit details with dictionaries,
tracking out-of-stock fruits with sets, and adjusting pricing"""

#Define the fruit tuples

fruit_batch = ("apples", "bananas", "oranges", "kiwis", "pears")

print(fruit_batch)

#Store and update fruit details with dictionaries

fruit_details = {
    "apples": {"price_per_lb": 2.50, "color": "red", "in_stock": True},
    "bananas": {"price_per_lb": 1.20, "color": "yellow", "in_stock": True},
    "oranges": {"price_per_lb": 3.00, "color": "orange", "in_stock": True},
    "kiwis": {"price_per_lb": 4.50, "color": "brown", "in_stock": True},
    "pears": {"price_per_lb": 3.15, "color": "green", "in_stock": True}
}

print(fruit_details)

out_of_stock = set()
out_of_stock.add("kiwis")
fruit_details["kiwis"]["in_stock"] = [True]
print(out_of_stock)

out_of_stock.pop()
out_of_stock.add("apples")

fruit_details["apples"]["in_stock"] = [False]
print(out_of_stock)
print(fruit_details)

fruit_details["bananas"]["price_per_lb"] = 1.1
print(fruit_details)