class Details:
   def __init__(self, name, age, occupation, country):
      self.name = name
      self.age = age
      self.occupation = occupation
      self.country = country
my_details = Details("Mary", 20, "Developer", "Uganda")
print("Name:", my_details.name)
print("Age:", my_details.age)
print("Occupation", my_details.occupation)
print("Country:", my_details.country)
print()

my_details = Details("Lean", 24, "Secetary", "Kenya")
print("Name:", my_details.name)
print("Age:", my_details.age)
print("Occupation", my_details.occupation)
print("Country:", my_details.country)

