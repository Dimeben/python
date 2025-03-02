"""
Get A Key
"""

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"],
}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])
"""
Get An Invalid Key
"""
zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

"""
Safely Get A Key
"""
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384,
}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)

"""
Delete A Key
"""
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30,
}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

"""
Get All Keys
"""
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18,
}
users = user_ids.keys()
lessons = num_exercises.keys()

"""
Get All Values
"""
total_exercises = 0

for num in num_exercises.values():
    total_exercises += num

"""
Get All Items
"""
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9,
}

for occupation, pct in pct_women_in_occupation.items():
    print(f"Women make up {pct} percent of {occupation}s.")

biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8,
}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars. ")
