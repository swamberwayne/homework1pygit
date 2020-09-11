#Wayne Swamber Jr
#1419882

import math

paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height*wall_width
print("Wall area:",wall_area,"square feet")

gallons_paint = wall_area/350
print("Paint needed:",('{:.2f}'.format(gallons_paint)),"gallons")

cans_needed = round(gallons_paint)
print("Cans needed:",cans_needed,"can(s)")

color_choice = input("\nChoose a color to paint the wall:\n")
cost_of_paint = cans_needed*paint_colors[color_choice]
print("Cost of purchasing", color_choice ,"paint: $"+str(cost_of_paint))