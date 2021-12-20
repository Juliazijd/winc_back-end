# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line

# Part 1
scorer1 = "Ruud Gullit"
scorer2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = f"{scorer1} {goal_0}, {scorer2} {goal_1}"
report = f"{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute"

# Part 2
player = "Frank Rijkaard"
first_name = player[: player.find(" ")]
last_name = player[player.find(" ") + 1 :]
last_name_len = len(last_name)
name_short = f"{first_name[:1]}. {last_name}"
chant_len = len(first_name) - 1
chant = f"{first_name}! " * chant_len + f"{first_name}!"
good_chant = chant[:-1] != " "

print(chant)
