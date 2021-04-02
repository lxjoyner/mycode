#!/usr/bin/env python3
"""Alta3 Research | Script to test dice agme"""

# All imports needed for script
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

# Create variable for each player
cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

# Function for cheaters to roll dice.
cheater1.roll()
cheater2.roll()

# function for each player.
cheater1.cheat()
cheater2.cheat()

# Print out dice being rolled
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

# Compare cheater 1 to cheater 2 see if both have same dice roll number
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

# Compare to see if cheater1 is higher than cheater2
elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  # Print out cheater 1 wins if cheater  1 dice is higher than cheater 2  
  print("Cheater 1 wins!")

# Print out cheater 2 wins if cheater2 dice is higher than cheater2
else:
  print("Cheater 2 wins!")

