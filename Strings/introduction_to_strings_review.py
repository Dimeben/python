def username_generator(first_name, last_name):
    #Check if first_name is less 3 letters or last_name is less than 4 letters
    if len(first_name) < 3 or len(last_name) < 4:
    #If it is, return the concatenated first_name + last_name
        return first_name + last_name
    #If first_name is 3+ and last_name is 4+ then return first 3 letters[:3] of first_name and first4 letters[:4] of last_name
    else:
        return first_name[:3] + last_name[:4]

#Shifts all the letters of user_name one to the right.  
def password_generator(user_name):
    password = ""
    for i in range(len(user_name)):
    #Adds the letter at the previous index of user_name to password with each pass of the loop.  
        password += user_name[i-1]
    return password