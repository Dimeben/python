# Introduction To Strings
favorite_word = "Paroxysm"

# They're All Lists!
my_name = "Ben"
first_initial = my_name[0]

# Cut Me A Slice Of String
slice_first_name = "Rodrigo"
slice_last_name = "Villanueva"
# Slices the first 5 characters of last_name
slice_new_account = slice_last_name[:5]
# Slices the 3rd - 6th characters of last_name
slice_temp_password = slice_last_name[2:6]

# Concatenating Strings
concat_first_name = "Julie"
concat_last_name = "Blevins"


# Takes two inputs, concatenates the first three letters of each and then returns the new account name.
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]


new_account = account_generator(concat_first_name, concat_last_name)

# More and More String Slicing (How Long is that String?)
more_sliced_first_name = "Reiko"
more_sliced_last_name = "Matsuki"


# Takes two inputs, concatenates the last three letters of each and then returns the new password.
def password_generator(first_name, last_name):
    return first_name[len(first_name) - 3 :] + last_name[len(last_name) - 3 :]


temp_password = password_generator(more_sliced_first_name, more_sliced_last_name)

# Negative Indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# Strings are Immutable
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[1:]

# Escape Characters
password = 'theycallme"crazy"91'


# Iterating through Strings - Finds length without using len()
def get_length(string):
    count = 0
    for char in string:
        count += 1
    return count


# Strings and Conditionals
# This function should return True if the word contains the letter and False if it does not.
def letter_check(word, letter):
    for char in word:
        if char == letter:
            return True
    return False


print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False
print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True


# This function takes two arguments, big_string and little_string and returns True if big_string contains little_string.
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    return False


# This function takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
def common_letters(string_one, string_two):
    common_letters_list = []
    for char in string_one:
        if char in string_two and char not in common_letters_list:
            common_letters_list.append(char)
    return common_letters_list
