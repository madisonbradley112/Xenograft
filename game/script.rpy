# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define puter = Character("Puter", window_background=Frame("images/textbox/green.png", 25, 25), namebox_background="images/textbox/green_namebox.png", who_xpos=200, who_ypos=20, color="#FFF")
define tunep = Character("Tunep", window_background=Frame("images/textbox/orange.png", 25, 25), namebox_background="images/textbox/orange_namebox.png", who_xpos=200, who_ypos=20, color="#FFF")
define jupiter = Character("Jupiter")
define neptune = Character("Neptune")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    "As you lay your head to sleep after a long day of "

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show puter scared
    show tunep base

    # These display lines of dialogue.

    tunep "what"


    # This ends the game.

    return
