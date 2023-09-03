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

    jump test

label intro:
    scene bg room

    # Intro devs
    "Introducing the devs"

    ## Intro Dpmon
    show dpmon lobster
    dev_dpmon "Hello! I'm Dpmon (aka Lobowoster)!"
    dev_dpmon "I did most of the storyboarding!"
    hide dpmon lobster

    ## Intro EvaFG
    show evafg cat
    dev_evafg "Hi! I'm EvaFG!"
    dev_evafg "I did all the art and sound resources!"

label test:
    
    "Text tags:"
    mc "{b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, {u}underlined{/u}, {alpha=.5}translucent{/alpha}, {color=#0080c0}color{/color}."
    mc "{a=https://www.renpy.org}link to a website{/a} or {a=jump:credits}jump to a label{/a}."
    mc "The cps tag controls text typing speed:\nIt can type {cps=25}as an absolute value{/cps}"
    mc "Or it can type relative to the default speed - {cps=*2}doubling the default speed{/cps} or {cps=*0.5}halving the default speed{/cps}."
    mc "{font=DejaVuSans-Bold.ttf}DejaVuSans-Bold.ttf{/font}."
    mc "Kerning: {k=-.5}closer together{/k} or {k=.5}farther apart{/k}."
    mc "Size: {size=30}Absolute size{/size} or relative size - {size=+10}bigger{/size} or {size=-10}smaller{/size}."
    mc "Horizontal space in text: {space=30} and {vspace=30}Vertical space between lines."
    mc "Wait tag (click): {w} (time) {w=.5} final text."
    mc "Paragraph break = wait tag but with newline - Click: {p}Time: {p=1.5}Newline text."

    mc "No wait tag to skip slow text{nw}"
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    with flashbulb
    extend " to the next statement."

    $ variable = "{i}variable value{/i}"
    mc "For example, this displays the [variable]."
 
    mc "Escaping: {{: {{{{,  \\: \\\\,  \': \\\', \": \\\""


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