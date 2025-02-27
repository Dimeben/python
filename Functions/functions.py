# Built-in Functions
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# max() function finds the greatest value
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(f"max_price = {max_price}")

# min() function finds the smallest value
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(f"min_price = {min_price}")

# round() return number rounded to ndigits precision after the decimal point
rounded_price = round(tshirt_price, 1)
print(f"rounded_price = {rounded_price}")


# Variable Access
# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"


def print_count_locations():
    print("There are 3 locations")


# This function will print the favorite locations
def show_favorite_locations():
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations()


# Returns
current_budget = 3500.75
shirt_expense = 9


def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))


print_remaining_budget(current_budget)


def deduct_expense(budget, expense):
    return budget - expense


new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


# Multiple Returns
def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)
