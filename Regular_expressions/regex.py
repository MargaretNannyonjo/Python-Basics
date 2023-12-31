mport re

def validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Test the function
emails = ["test@example.com", "invalid_email", "user@mail", "another@mail.co.uk"]
for email in emails:
    print(f"{email}: {validate_email(email)}")
