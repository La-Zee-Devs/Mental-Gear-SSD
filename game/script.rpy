# Main Character
define mc = Character("[name]")

# Side characters
define boss         = Character("Boss")
define colleague_1  = Character("Jack")
define colleague_2  = Character("Jane")
define mom          = Character("Mom")

# Developer characters
define dev_dpmon = Character("Dpmon")
define dev_evafg = Character("EvaFG")

# Splash screen
label splashscreen:
    scene black
    with Pause(1)

    show text " {size=40} La-Zee Devs presents... {/size} " with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    show text " {size=50} Mental Gear SSD {/size} " with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    return


# Start game
label start:
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Guy Shy"
    
    menu:
        "Start game":
            jump mc_intro

        "(Debug) see text_tags":
            jump text_tags

        "Credits":
            jump credits


# Debug
label text_tags:
    
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
    mc "Interpolate variables: [variable], interpolate raw variable text without rendering text tags: [variable!q]."
    mc "For example, this displays the [variable]."
 
    mc "Escaping in text:  \\: \\\\,  \': \\\',  \": \\\",  {{: {{{{,  [[: [[[["
    mc "Escaping in dialogue only (not text):  %%: %%%%"

    return


# Main
label mc_intro:
    mc "hi and bye"

    jump credits 




# Credits
label credits:
    scene black
    with Pause(1)

    centered "{size=+75}{cps=8}Credits{/cps}{/size}{p=2.0}{nw}" with dissolve

    menu:
        "Skip credits?"

        "Yes":
            jump credits_final
        "No":
            jump credits_devs
    
label credits_devs:
    scene black
    with Pause(1)

    centered "{size=+75}The devs{/size}{p=2.0}{nw}" with dissolve

    ## Intro Dpmon
    show dpmon lobster
    dev_dpmon "Hello! I'm Dpmon (aka Lobowoster)!"
    dev_dpmon "I did most of the storyboarding!"
    hide dpmon lobster

    ## Intro EvaFG
    show evafg cat
    dev_evafg "Hi! I'm EvaFG!"
    dev_evafg "I did all the art and sound resources!"

    jump credits_art

label credits_art:
    scene black
    with Pause(1)

    centered "{size=+75}Art resources{/size}{p=2.0}{nw}" with dissolve

    # Backgrounds
    "Backgrounds"

    scene bg table_1
    "Table 1" "Image by Brett Sayles"
    
    scene bg table_2
    "Table 2" "Image by Karolina Grabowska"

    scene bg break_room
    "Break Room" "Image by Rachel Claire"

    scene bg hallway
    "Hallway" "Image by Pixabay"

    scene bg bankrupt
    "Bankrupt" "Image by Nicola Barts"

    scene bg ded
    "Ded" "Image by EvaFG"


    # TODO: Assets

    jump credits_music

label credits_music:
    scene black
    with Pause(1)

    centered "{size=+75}Music resources{/size}{p=2.0}{nw}" with dissolve

    # TODO: Add Music resources credits
    "TODO"
    
    jump credits_final

label credits_final:
    "Thanks for playing this game!"

    jump end_game


label end_game:
    return