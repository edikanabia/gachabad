label lookuptable(index):
    #index is equal to a global variable that keeps track of where in the script you are
    return

label repeatcheck:
    #flags will change the specifics of who says what
    if repeat_active:
        n "Sure."
        $ repeat_active = False
        call screen history

    else:
        n "I'm not doing that."
    return