# Characters
## Main Character
define mc = Character("[player_name]")

## Side characters
define boss         = Character("Boss")
define colleague_1  = Character("Jack")
define colleague_2  = Character("Jane")
define mom          = Character("Mom")

## Developer characters
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
        player_name = renpy.input("What's your name?")
        player_name = player_name.strip() or "Guy Shy"
    
    menu:
        "Start game":
            call main

        "(Debug) see text_tags":
            call debug

        "Credits":
            call credits

    jump end_game


# Main
label main:
    call chapter_1


label end_game:
    return