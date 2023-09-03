label chapter_1:
    call .mc_intro
    return

label .mc_intro:
    scene black

    mc "New assignment, huh?"
    centered "{size=+10}Hello [player_name],\n\nWe are pleased to offer you a role as a Microchip analyst in the new government Logistics department.\n\nYour annual salary will be paid monthly at teh rate of 15,000 Koofbucks per annum. If you make great contributions, you may be eligible to recieve an additional bonus at such a time.\n\n You agree that you are employed on an \"at-will\" basis. Your employment may be terminated by the government at any time for any reason, subject to any applicable notice policies or provisions.\n\nSincerely,\nEugene Krabs\nLogistics chair\nNew Koofling Tukstra Empire advisory board{/size}" with dissolve
    mc "???"
    jump .end


label .end:
    "End of Chapter 1"
    return
