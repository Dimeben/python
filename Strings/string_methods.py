"""Formatting Methods"""

poem_title = "spring storm"
poem_author = "William Carlos Williams"

# Title case makes the first letter of each word capital
poem_title_fixed = poem_title.title()

poem_author_fixed = poem_author.upper()

"""Splitting Strings"""

line_one = "The sky has given over"
# No delimiter uses whitespace as default
line_one_words = line_one.split()

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Creates a list with each element consisting of a first name and last name.
author_names = authors.split(",")
# Creates a list by iterating through the author_names list, splitting each element into a 2D list and taking the last value (last name)
author_last_names = [name.split()[-1] for name in author_names]

# \n Newline - allows us to split a multi-line string by line breaks
# \t Horizontal Tab - allows us to split a string by tabs
spring_storm_text = """The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

# Creates a list where each element is a line from spring_storm_text
spring_storm_lines = spring_storm_text.split("\n")

"""Joining Strings"""
# Syntax - 'delimiter'.join(list_you_want_to_join)

reapers_line_one_words = [
    "Black",
    "reapers",
    "with",
    "the",
    "sound",
    "of",
    "steel",
    "on",
    "stones",
]
reapers_line_one = " ".join(reapers_line_one_words)

winter_trees_lines = [
    "All the complicated details",
    "of the attiring and",
    "the disattiring are completed!",
    "A liquid moon",
    "moves gently among",
    "the long branches.",
    "Thus having prepared their buds",
    "against a sure winter",
    "the wise trees",
    "stand sleeping in the cold.",
]

# Using the \n delimiter will join the string together with each element put on a new line
winter_trees_full = "\n".join(winter_trees_lines)

""".strip()"""
#:.strip() Eliminates any trailing spaces at the beginning and end of a string. Specific characters can be passed in as an argument to be removed instead.
love_maybe_lines = [
    "Always    ",
    "     in the middle of our bloodiest battles  ",
    "you lay down your arms",
    "           like flowering mines    ",
    "\n",
    "   to conquer me home.    ",
]

love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]
love_maybe_full = "\n".join(love_maybe_lines_stripped)

""".replace()"""
# Replace a specific substring with another substring.

toomer_bio = """
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")


""".find()"""
# Takes in a substring (and optionally start/end index), returns the index number of the first occurrence of the substring inside a string. It is case sensitive.
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")

""".format()"""
# Replaces empty brace ({}) placeholders in the string with its arguments


def poem_title_card(title, poet):
    return "The poem {} is written by {}.".format(title, poet)


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        publishing_date=publishing_date,
        author=author,
        title=title,
        original_work=original_work,
    )
    return poem_desc


my_beard_description = poem_description(
    author="Shel Silverstein",
    title="My Beard",
    original_work="Where the Sidewalk Ends",
    publishing_date="1974",
)
