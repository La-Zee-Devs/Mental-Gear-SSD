label chapter_1:
    show text " {size=40} Chapter 1 {/size} " with dissolve
    with Pause(1)
    call .mc_intro
    return


# Helpers
label .work_menu:
    menu:
        "[menu_string]"
        
        "R&D":
            "I'll send this chip off to R&D"
            $ kooftuks_score        += rnd_kooftuks_score
            $ profits               += rnd_profit
        "Resale":
            "I'll send this chip off to be resold"
            $ kooftuks_score        += resale_kooftuks_score
            $ profits               += resale_profit
        "Format":
            $ kooftuks_score        += format_kooftuks_score
            $ profits               += format_profit
            $ blank_chips           += 1
            "I'll format this chip - I have [blank_chips] chips now"
        "Duplicate" if blank_chips > 0:
            call .work_menu_handle_duplicates
    
    return
    
label .work_menu_handle_duplicates:
    # Dupe more chips
    "I have [blank_chips] blank chip(s)."
    $ num_duplicates = int(renpy.input("How many chips to duplicate?"))
    if num_duplicates < 1:
        "I'll be assuming you meant 1 duplicate"
        $ num_duplicates = 1
    if num_duplicates > blank_chips:
        "I'll be assuming you meant [blank_chips] duplicate(s)"
        $ num_duplicates = blank_chips
    
    $ num_duplicates        += 1 # Initial chip
    $ kooftuks_score        += duplicate_kooftuks_score * num_duplicates
    $ profits               += duplicate_profit * num_duplicates
    $ blank_chips           -= num_duplicates

    menu:
        "Send a chip to R&D? No point sending more than one, after all."
        "Yes":
            $ kooftuks_score        += rnd_kooftuks_score
            $ profits               += rnd_profit
            $ num_duplicates -= 1 
            "All right, sent it off. I have [num_duplicates] more copies remaining"
        "No":
            "Yeah, might as well reserve it for resale."
    
    if num_duplicates > 0:
        $ num_resell = int(renpy.input("How many chips to resell?"))
        if num_resell < 1:
            "No need to resell when I can just format these chips"
        else:
            if num_duplicates < num_resell:
                "I'll be assuming you meant [num_duplicates] chip(s)"
                $ num_resell = num_duplicates

            $ kooftuks_score        += resale_kooftuks_score
            $ profits               += resale_profit
            $ num_duplicates        -= num_resell
    
    if num_duplicates > 0:
        "I'll format all the remaining ones again"
        $ kooftuks_score        -= duplicate_kooftuks_score * num_duplicates
        $ profits               -= duplicate_profit * num_duplicates
        $ blank_chips           += num_duplicates

    return


# Main
label .mc_intro:
    scene black

    mc "New assignment, huh?"
    centered "{size=+10}Hello ${{applicant_name},\n\nWe are pleased to offer you a role as a Microchip analyst in the new government Logistics department.\n\nYour annual salary will be paid monthly at teh rate of 15,000 Koofbucks per annum. If you make great contributions, you may be eligible to recieve an additional bonus at such a time.\n\n You agree that you are employed on an \"at-will\" basis. Your employment may be terminated by the government at any time for any reason, subject to any applicable notice policies or provisions.\n\nSincerely,\nEugene Krabs\nLogistics chair\nNew Koofling Tukstra Empire advisory board{/size}" with dissolve
    mc "\"${{applicant_name}\"... Ah well, at least I'm not getting promoted to customer. I should get a good night's sleep tonight."

    jump .office_1

label .office_1:
    scene bg hallway
    mc "Oh great, this is in the old building. At least it looks recently refurbished..."

    scene bg break_room
    mc "Break room looks nice too. Limited seating though, real subtle."
    mc "And no coffee machine here, how do they expect me to work in these conditions?"
    mc "Oh well, I should go introduce myself to my boss first."

    scene bg hallway
    "{i}You find yourself wandering the unmarked hallways, unable to find any office that looks to be of import{/i}"
    mc "This place is like the backrooms, why aren't any of these offices labelled?"
    mc "Ah, here we go. \"Bret Barts\"'s office."
    boss "Are you here to pay rent? I'm at work, shoo I'll stop by later."
    mc "I'm [player_name], I've been hired on as a Microchip analyst?"
    boss "Ah, right. After the recent acquisi- {i}Erm{/i} Governmental policy changes, we have a surplus of old microchips that we're looking to liquidate."
    boss "Weed out the ones that we can sell off to the masses, and reserve any interesting ones for R&D. All the rest go into the scrapper."
    boss "If that's all, get to work! I'm expecting prompt results!"

    jump .work_1
    
label .work_1:
    scene bg table_1
    "You make your way to your assigned desk, finding your equipment to be old - 2030s, maybe even 2020s equipment. Barely adequate for your needs."

    mc "Joy."
    "You work through the chips, discarding broken ones into the scrapheap and putting any seemingly working chips aside to inspect later."
    "You keep going until you have quite a pile of working chips, after which you start plugging them into your provided PC."
    
    mc "Hm, this one's got corrupted software but the hardware's sound. I can format it and duplicate another chip onto it."
    $ blank_chips += 1

    show microchip
    mc "Interesting, this chip looks like it's got a pretty sophisticated laser tag aimbot on it. Bet they got banned for hip-firing circles around the other team lol"
    $ menu_string               = "R&D might get some mileage out of this, but really, it's a laser tag biochip, it's probably useless outside the arena.\nWhich pile do I put this in?"
    $ rnd_kooftuks_score        = 1
    $ rnd_profit                = 0
    $ resale_kooftuks_score     = -1
    $ resale_profit             = 1
    $ format_kooftuks_score     = 0
    $ format_profit             = -1
    $ duplicate_kooftuks_score  = 0
    $ duplicate_profit          = 0
    call .work_menu

    jump .break_room

label .break_room:    
    "I'm gonna take a quick break, this is giving me a headache"

    scene bg break_room
    colleague_1 "Hey there, you're the chips guy right?"
    mc "Yep that's me!"
    colleague_1 "Heard about you, I work up in R&D and they say you'll be sending us some goodies to play around with, yeah?"
    mc "Haha I'll certainly try! Some of these chips are so damaged they're just paperweights."
    colleague_1 "Haha that's true of course. But just remember, the more you can send us the more friends you'll make up in R&D, you get me?"
    mc "Sounds good dude!"

    jump .work_2

label .work_2:
    scene bg table_1
    show microchip
    mc "Hm, this one's a chess algorithm on some real nice custom hardware. Some collector'll pay top dollar for this one I bet. Resale pile it goes."
    $ profits += 1

    mc "Ahh, this one looks good, it's a martial arts chip with some sweet Matrix decals on it. Literally an \"I know kung fu\" chip."
    $ menu_string               = "I wish I could nab this one for myself... It's not exactly military grade CQC though, so who knows if anyone besides a collector would pay for it."
    $ rnd_kooftuks_score        = 0
    $ rnd_profit                = 0
    $ resale_kooftuks_score     = -2
    $ resale_profit             = 1
    $ format_kooftuks_score     = 0
    $ format_profit             = 0
    $ duplicate_kooftuks_score  = 0
    $ duplicate_profit          = 0
    call .work_menu
    
    jump .end


label .end:
    "End of Chapter 1"
    return
