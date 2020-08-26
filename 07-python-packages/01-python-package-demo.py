# import the start module
import Game.Level.start


# start module contains a function named select_difficulty(), 
# we must use the full name to reference it.
Game.Level.start.select_difficulty(2)

# import only start module
from Game.Level import start
start.select_difficulty(3)


# importing just the required function (or class or variable) from a module within a package
from Game.Level.start import select_difficulty
select_difficulty(4)