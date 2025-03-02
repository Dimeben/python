from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Get current date and time
date_time_now = dt.now()
print(f"The current date & time is: {date_time_now}")

# Calculate the time travel cost
current_year = dt.now().year
target_year = randint(1900, 2100)  # Random year between 1900 and 2100
year_difference = abs(target_year - current_year)

base_cost = Decimal("100.00")
cost_multiplier = Decimal(year_difference) / Decimal("10")
total_cost = base_cost * cost_multiplier
total_cost = total_cost.quantize(Decimal("0.00"))  # Format to two decimal places

# Random selections
destinations = ["Ancient Rome", "Medieval Europe", "Future Mars", "Renaissance Italy"]
selected_destination = choice(destinations)

# Using the custom module
message = custom_module.generate_time_travel_message(
    target_year, selected_destination, total_cost
)
print(message)
