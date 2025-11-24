def validUsername(username):
    # Check if the length is 10 or less
    if len(username) > 10:
        return False
    # Check if the username contains only alphanumeric characters (isalnum() returns True if it does)
    # The original code should have checked if it is NOT alphanumeric
    elif not username.isalnum():
        return False
    # Check for specific disallowed characters
    elif "<" in username or ">" in username:
        return False
    # If all checks pass, the username is valid
    else:
        return True

def mainStuff():
    while True:
        user = input("Username > ")
        # Call the function and store the result in a variable
        is_valid = validUsername(user)
        # Check the boolean result
        if is_valid is False:
            print("Invalid")
        else:
            print("Valid")

# Start the program
mainStuff()