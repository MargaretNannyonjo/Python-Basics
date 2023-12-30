Bot = {
   "age": "20", "weight": "60kgs", "country": "Rwanda", "sex": "Male"
}

Bot["hobby"] = "reading"

for key, value in Bot.items():
   print(key + ":" + value)
   print()

sorted_keys = sorted(Bot.keys())
for key in sorted_keys:
   print(key)

print()
sorted_values = sorted(Bot.values())
for value in sorted_values:
   print(value)
