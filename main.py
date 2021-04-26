<<<<<<< HEAD
# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = (player_0)+' '+str(goal_0)+', '+(player_1)+' '+ str(goal_1)
print(scorers)
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)
player = 'Gerald Vanenburg'
first_name = player[0:player.find(' ')]
print(first_name)
last_name_len = len(player[player.find(' ')+1:len(player)])
print(last_name_len)
name_short = player[0:1]+'. '+player[player.find(' ')+1:len(player)]
print(name_short)
# chant = (player[0:player.find(' ')]+'! ')*len(player[0:player.find(' ')])[:-1]
chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')]))[:-1]
print(chant)
good_chant = (chant[-1] != ' ')
print(good_chant)
=======
# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = (player_0)+' '+str(goal_0)+', '+(player_1)+' '+ str(goal_1)
print(scorers)
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)
player = 'Gerald Vanenburg'
first_name = player[0:player.find(' ')]
print(first_name)
last_name_len = len(player[player.find(' ')+1:len(player)])
print(last_name_len)
name_short = player[0:1]+'. '+player[player.find(' ')+1:len(player)]
print(name_short)
chant = (player[0:player.find(' ')]+'! ')*len(player[0:player.find(' ')-1])+(player[0:player.find(' ')]+'!')
print(chant)
good_chant = (chant[-1] != ' '  )
print(good_chant)
>>>>>>> 47ad2d14cafc1c8136a2d163e1e5fdb5197bbe7c
print(chant[-1])