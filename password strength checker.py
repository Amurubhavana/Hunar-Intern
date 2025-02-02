import re

def evaluate_password_strength(password):
    
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_special):
        return "Okay"
    else:
        return "Weak"

password = input("Enter your password to evaluate its strength: ")
strength = evaluate_password_strength(password)
print(f"Your password is {strength}.")
