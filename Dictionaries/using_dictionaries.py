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


"""
Delete A Key
"""


"""
Get All Keys
"""


"""
Get All Values
"""


"""
Get All Items
"""
