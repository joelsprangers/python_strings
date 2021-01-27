# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_one = "Gullit"
player_two = "Van Basten"
goal_0 = 32
goal_1 = 54

player = 'Erwin Koeman'
first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:]
last_name_len = len(last_name)
name_short = f'{player[1].upper()}. {last_name}'
chant = (f'{first_name}! ' * len(first_name))[:-1]
good_chant = chant[-1] != ' '

scorers = player_one + " " + str(goal_0)+ ", " + player_two + " " + str(goal_1)

report = f'{player_one} scored in the {goal_0}th minute \n{player_two} scored in the {goal_1}th minute'

print(scorers)
print(report)

print(first_name)
print(last_name)
print(name_short)
print(chant)
print(good_chant)

