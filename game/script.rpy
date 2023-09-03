init:
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

    # Variables:
    $ kooftuks_score    = 0  
    $ profits           = 0
    $ blank_chips       = 0

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

        "Debug":
            call debug

        "Credits":
            call credits

    jump end_game


# Main
label main:
    call chapter_1
    "Due to time limitations, Skipping a few planned chapters"
    "Chapter 2 plot would have been how you notice signs of dissent among the populace, the news and media being controlled more and more over time."
    "Some hints will also be dropped on recent history in the country: tldr the old govt was a monarcy called the Koofling Tukstra Empire, but it was overthrown"
    "and a massive national conglomerate called the United Corporations of Kooftuks put a puppet emperor in power, and started replacnig entire branches of govt."
    "Chapter 3 plot would have been how foreign influences are being increasingly more present, and the media is somehow brought back to being less controlled and more free"
    "due to corporate infighting, internal dissent and foreign involvement."
    "Chapter 4 starts with a news story of a riot and a conversation with your mom and family, followed by talks with your pro-govt and pro-resistance friends."
    "Depending on your actions earlier, a foreign spy might reach out to you as well with a proposition."
    "Chapter 5, you return to work and find: \nIf your actions were pro-govt and you earned lots of profits: you were promoted to be a factory manager"
    "If your actions were pro-govt and you didn't earn profits: you lose the job and your debts catch up to you"
    "There is a secret ending where anti-govt actions from you allow a revolution which brings the country to anarchy, after which the country is annexed by the neighboring countries."
    call credits
    jump end_game


label end_game:
    return