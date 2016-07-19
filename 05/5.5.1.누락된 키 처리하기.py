# setdefault()
periodic_table = {"hydrogen": 1, "Helium": 2}
print(periodic_table)

carbon = periodic_table.setdefault("Carbon", 12)
print(carbon)
print(periodic_table)

helium = periodic_table.setdefault("Helium", 256)
print(helium)
print(periodic_table)

print("===================================")

# defaultdict()
from collections import defaultdict
periodic_table = defaultdict(int)

print(periodic_table)
periodic_table["Hydrogen"] = 1;
periodic_table["Lead"]

print(periodic_table)

print("===================================")

def no_idea():
	return "Huh?"

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['C']

print(bestiary)

print("===================================")

#lamda
bestiary = defaultdict(lambda: 'Huh?')
bestiary['E']

print(bestiary)

print("===================================")

# counter
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
	food_counter[food] += 1

for food, count in food_counter.items():
	print(food, count)