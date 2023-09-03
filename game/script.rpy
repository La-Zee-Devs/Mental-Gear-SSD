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

    ## Intro EvaFG
    show evafg cat
    dev_evafg "Hi! I'm EvaFG!"


label credits:

    scene bg room
    
    # End Credits
    "Credits" "Backgrounds"

    scene bg bankrupt
    "Bankrupt" "Image by Nicola Barts"

    scene bg break_room
    "Break Room" "Image by Rachel Claire"

    scene bg hallway
    "Hallway" "Image by Pixabay"

    scene bg table_1
    "Table 1" "Image by Brett Sayles"
    
    scene bg table_2
    "Table 2" "Image by Karolina Grabowska"

    "Thanks for playing this game!"

    # This ends the game.
    return