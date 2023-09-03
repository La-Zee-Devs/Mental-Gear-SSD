# Credits
label credits:
    scene black
    with Pause(1)

    centered "{size=+75}{cps=8}Credits{/cps}{/size}{p=2.0}{nw}" with dissolve

    menu:
        "Skip credits?"

        "Yes":
            jump .final
        "No":
            jump .devs
    
label .devs:
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

    jump .art

label .art:
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

    jump .music

label .music:
    scene black
    with Pause(1)

    centered "{size=+75}Music resources{/size}{p=2.0}{nw}" with dissolve

    # TODO: Add Music resources credits
    "TODO"
    
    jump .final

label .final:
    "Thanks for playing this game!"

    return
