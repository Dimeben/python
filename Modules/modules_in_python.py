"""Modules"""

from datetime import datetime
import random
from decimal import Decimal

# Sets variable as the current date & time in the following format: 2025-03-01 07:23:03.520673
current_time = datetime.now()

# randint() takes 2 arguments and will pick a random value within that range
random_list = [random.randint(1, 100) for i in range(101)]
# choice() takes an argument and will pick a random element within that range
randomer_number = random.choice(random_list)

numbers_a = range(1, 13)
# sample() takes 2 arguments (sequence, k) and returns a k length new list of elements chosen from the sequence
numbers_b = random.sample(range(1000), 12)

# Fix the floating point math below:
two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points)
