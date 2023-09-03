# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Developer characters
define dev_dpmon = Character("Dpmon")
define dev_evafg = Character("EvaFG")

# Main Character
define mc = Character("Main_Character")

# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text " La-Zee Devs presents... " with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    show text "Mental Gear SSD" with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    return


label start:

    # TODO: Add scene here

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    "Text tags:"
    mc "{b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, {u}underlined{/u}, {alpha=.5}translucent{/alpha}."
    mc "{a=https://www.renpy.org}link to a website{/a} or {a=jump:credits}jump to a label{/a}."
    mc "{color=#0080c0}color{/color}"
    mc "The cps tag controls text typing speed."
    mc "It can type {cps=25}as an absolute value{/cps}"
    mc "Or it can type relative to the default speed - {cps=*2}doubling the default speed{/cps} or {cps=*0.5}halving the default speed{/cps}."
 
    # 
    # 


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