# Import datetime from datetime below:
from datetime import datetime
import random

current_time = datetime.now()
print(current_time)

random_list = [random.randint(1, 100) for i in range(101)]
print(random_list)

randomer_number = random.choice(random_list)
print(randomer_number)
