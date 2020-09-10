#Wayne Swamber Jr
#1419882

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))

servings = float(input('How many servings does this make?\n'))

print("\nLemonade ingredients - yields",'{:.2f}'.format(servings),"servings")
print('{:.2f}'.format(lemon_juice_cups),"cup(s) lemon juice")
print('{:.2f}'.format(water_cups),"cup(s) water")
print('{:.2f}'.format(agave_nectar_cups),"cup(s) agave nectar")

servings_wanted = float(input('\nHow many servings would you like to make?\n'))

required_ingri_serving = servings_wanted/servings

lemon_juice_cups = lemon_juice_cups*required_ingri_serving
water_cups = water_cups*required_ingri_serving
agave_nectar_cups = agave_nectar_cups*required_ingri_serving

print("\nLemonade ingredients - yields",'{:.2f}'.format(servings_wanted),"servings")
print('{:.2f}'.format(lemon_juice_cups),"cup(s) lemon juice")
print('{:.2f}'.format(water_cups),"cup(s) water")
print('{:.2f}'.format(agave_nectar_cups),"cup(s) agave nectar")

x = lemon_juice_cups / 16
gallon = x

y = water_cups / 16
gallon = y

z = agave_nectar_cups / 16
gallon = z

print("\nLemonade ingredients - yields",'{:.2f}'.format(servings_wanted),"servings")
print('{:.2f}'.format(x),"gallon(s) lemon juice")
print('{:.2f}'.format(y),"gallon(s) water")
print('{:.2f}'.format(z),"gallon(s) agave nectar")