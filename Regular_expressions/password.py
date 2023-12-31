import re

def check_password_strength(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,}$'
    return bool(re.match(pattern, password))

# Test the function
passwords = ["Abcdefg1!", "weakpassword", "Strong123", "noSpecialChar8"]
for password in passwords:
    print(f"{password}: {check_password_strength(password)}")

