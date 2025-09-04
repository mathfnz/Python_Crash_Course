#  5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.
#  • Make a list of five or more usernames called current_users.
#  • Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
#  • Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
#  • Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
# current_users containing the lowercase versions of all existing users.)

# A list of existing usernames.
current_users: list[str] = ["matheus", "felipe", "kaina", "gustavo", "leticia"]

# A list of new usernames to be checked.
new_users: list[str] = ["MATHEUS", "douglas", "eugenio", "santiago", "kaina"]

# For a truly case-insensitive and efficient comparison, it is optimal to create 
# a secondary collection containing the lowercase versions of all existing usernames.
# Using a set provides superior performance for membership testing (the 'in' keyword).
current_users_lower: set[str] = {user.lower() for user in current_users}

# Iterate through the list of new usernames.
for new_user in new_users:
    # Check if the lowercase version of the new username exists in the set of lowercase current usernames.
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' has already been taken. Please select an alternative. 🧐")
    else:
        print(f"The username '{new_user}' is available. ✅")
