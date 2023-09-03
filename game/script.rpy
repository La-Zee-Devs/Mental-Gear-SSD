# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Developer characters
define dev_dpmon = Character("Dpmon")
define dev_evafg = Character("EvaFG")

# Main Character
define mc = Character("Main_Character")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # Intro devs
    "Introducing the devs"

    ## Intro Dpmon
    show dpmon lobster
    dev_dpmon "Hello! I'm Dpmon (aka Lobowoster)!"
    hide dpmon lobster

    ## Intro EvaFG
    show evafg cat
    dev_evafg "Hi! I'm EvaFG!"
    show dpmon lobster at right
    dev_dpmon "hoya"

    # This ends the game.
    return
