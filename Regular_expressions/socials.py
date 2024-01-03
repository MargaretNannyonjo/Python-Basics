ass Profile:
    def __init__(self, name, bio, friends):
        self.name = name
        self.bio = bio
        self.friends = friends
my_profile = Profile("Mary", "Loves Tech", ["Ethan","Winnie", "Jackie", "Ray", "Calvin", "Maggie", "Fred", "Lydia", "Patrick", "Jess"]) 
print("Name:", my_profile.name)
print("Bio:", my_profile.bio)
print("Friends:", my_profile.friends)
print()

print(my_profile.friends[3])
my_profile.friends.append("Wills")
print(my_profile.friends)
