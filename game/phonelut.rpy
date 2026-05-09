label lookuptable(index):
    #index is equal to a global variable that keeps track of where in the script you are
    return

label repeatcheck:
    #flags will change the specifics of who says what
    $ repeat_active = False #disable the repeat that button

    if since_last_repeat <= 4:
        $ since_last_repeat = 0
        n "What? No! Pay attention."
        $ repeat_active = True #reeneable the repeat that button
        return
    elif since_last_repeat > 4:
        n "Sure, I can do that."
        $ since_last_repeat = 0
        call screen history(_with_none=False) as menu with dissolve 
        with dissolve

    $ repeat_active = True #reeneable the repeat that button

    #player can currently rollback into the history screen. 
    #prevent player from accessing rollback when game is closer to finished
    return