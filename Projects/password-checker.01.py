import re
import random
import string

user_pass = input("Please enter your password...")
num = len(user_pass)
length = random.randint(7, 10)
missing = []

# Check what char types are present
upper = bool(re.search(r'[A-Z]', user_pass))
lower = bool(re.search(r'[a-z]', user_pass))
digit = bool(re.search(r'[0-9]', user_pass))
symbol = bool(re.search(r'[!@#$%&]', user_pass))

# Characters from user's password for better suggestions if their password was weak
user_uppers = [c for c in user_pass if c.isupper()]
user_lowers = [c for c in user_pass if c.islower()]
user_digits = [c for c in user_pass if c.isdigit()]
user_symbols = [c for c in user_pass if c in "!@#$%&"]

all_chars = user_uppers + user_lowers + user_digits + user_symbols

# Character suggestion in case user's password missing some type
help_upper = string.ascii_uppercase
help_lower = string.ascii_lowercase
help_digit = string.digits
help_symbol = "!@#$%&"

# Pick characters for suggestions
def pick_char(chars, helps):
    if chars:
        return random.choice(chars)
    else:
        return random.choice(helps)


def generate_suggestion():
    suggestion_chars = []
    # Ensure it's taken from all categories
    suggestion_chars.append(pick_char(user_uppers, help_upper))
    suggestion_chars.append(pick_char(user_lowers, help_lower))
    suggestion_chars.append(pick_char(user_digits, help_digit))
    suggestion_chars.append(pick_char(user_symbols, help_symbol))
    
    # Fill the rest of the length randomly from user's password
    while len(suggestion_chars) < length:
        suggestion_chars.append(random.choice(user_pass))


extra1 = generate_suggestion()
extra2 = generate_suggestion()

if all([upper, lower, digit, symbol]):
    if num < 4:
        print("Too short!")
    elif num < 6: 
        print(f"Weak, how about {extra1} or {extra2} ?") 
    elif num < 8:
        print("Medium")
    elif num < 13:
        print("Strong")
    else:
        print("Too long!")
else: 
    if not upper:
        missing.append("an uppercase letter")
    if not lower:
        missing.append("a lowercase letter")
    if not digit:
        missing.append("a digit")
    if not symbol:
        missing.append("a special symbol (!@#$%&)")
    print("Your password is missing:", ", ".join(missing))
