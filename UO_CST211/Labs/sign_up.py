"""
Tyler Taormina
Lab 8
Sign-up Interface: Using regular expressions to validate an email address
05.19.2021
"""

import re

def validate_email(email: str) -> bool:
    """Email cannot start with a digit.
    Can only contain one @ sign.
    Must end with either .com or .edu.
    """
    if re.match(r'\D[^@]*@[^@]*((\.edu)|(\.com))$', email):
        return True
    return False


def validate_password(password: str) -> bool:
    """Must contain 10 characters
    Must contain at least 1 digit
    Must contain at least one special symbol (non-alphanumeric)
    """
    if len(password) >= 10 and re.match(r'(.*\d.*\W.*)|(.*\W.*\d.*)', password):
        return True
    return False

def main():
    email = input("Please enter an email address: ")
    while not validate_email(email):
        email = input("That is an invalid email. \n"
                      "As a reminder, your email must not start with \n"
                      "a digit, can only contain 1 '@' sign, \n"
                      "and must end in either '.edu' or '.com'. \n"
                      "Please enter another: ")
    password = input("Please enter a password: ")
    while not validate_password(password):
        password = input("That is an invalid password.\n"
                         "As a reminder your password must contain at \n"
                         "least 10 characters, at least 1 digit, and \n"
                         "at least one special symbol. \n"
                         "  Please enter another: ")
    print("Congratulations! You have signed up successfully.")
    return None



if __name__ == '__main__':
    main()
