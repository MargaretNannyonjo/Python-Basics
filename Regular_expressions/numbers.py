import re

text = "Hello, this is a sample text with numbers 12345 and symbols !@#."

# Find all numbers in the text
numbers = re.findall(r'\d+', text)
print(numbers)

