label chapter_1:
    call .mc_intro
    return


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
    mc "And to coffee machine here, how do they expect me to work in these conditions?"
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
    "You keep going until you have quite a pile of working chips, after which you start plugging them into your provided PC"
    "Many of them have corrupted software, so you start a new pile of chips to format, load new tech on and resell."
    

    show microchip
    mc "Interesting, this chip looks like it's got a pretty sophisticated laser tag aimbot on it. Bet they got banned for hip-firing circles around the other team lol"
    menu:
        "R&D might get some mileage out of this, but really, it's a laser tag biochip, it's probably useless outside the arena.\nWhich pile do I put this in?"
        
        "R&D":
            $ FLAG_SOLD_LASER_TAG    = False
            $ kooftuks_score        += 1
            $ profits               += 0
        "Resale":
            $ FLAG_SOLD_LASER_TAG    = True
            $ kooftuks_score        += -1
            $ profits               += 1
    

    mc "Hm, this one's an AI chess algorithm. Some collector'll pay top dollar for this one I bet. Resale pile it goes."
    $ profits += 1

    menu:
        "R&D might get some mileage out of this, but really, it's a laser tag biochip, it's probably useless outside the arena.\nWhich pile do I put this in?"
        
        "R&D":
            $ FLAG_SOLD_LASER_TAG = False
        "Resale":
            $ FLAG_SOLD_LASER_TAG = True
    
    

label .end:
    "End of Chapter 1"
    return
