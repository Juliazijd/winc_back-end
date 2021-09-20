# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer1 + ' ' + str(goal_0), scorer2 + ' ' +  str(goal_1)
report = f'{scorer1} scored in the {goal_0}nd minute \n{scorer2} scored in the {goal_1}th minute'

print (scorer1, scorer2)
print(goal_0, goal_1)
print(scorers)
print(report)

# Part 2
player = 'Frank Rijkaard'
first_name = player[:5]
last_name = player[6:]
last_name_len = len(last_name)
name_short = f'{first_name[:1]}. {last_name}'
chant = f'{first_name}! ' * 5

print(player)
print(first_name)
print(last_name)
print(last_name_len)
print(name_short)
print(chant)
