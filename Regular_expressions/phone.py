#!/usr/bin/python3
phoneBook = {
   "Angie": "2783849", "Marie": "4569656", "Nick": "05853636", "Rain": "458868", "Pasco": "7485746"
}
phoneBook["Vin"] = "4657532"
del phoneBook["Angie"]

for key, value in phoneBook.items():
   print(key + ":" + value)
print()
sorted_keys = sorted(phoneBook.keys())


for key in sorted_keys:
   print(key)
print()

sorted_values = sorted(phoneBook.values())
for value in sorted_values:
   print(value)
