label chapter_1:
    call .mc_intro
    return

label .mc_intro:
    mc "hi and bye"
    jump .end


label .end:
    "End of Chapter 1"
    return

