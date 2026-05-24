label lookuptable(index):
    #index is equal to a global variable that keeps track of where in the script you are
    #the test index is -1. if the index is null or 0, nothing happens.
    #it looks like we'll be manually setting the regions in which a phone interaction will trigger a dialogue.
    if index == -1:
        n "This is Niecy telling you to get off that damn phone!"
        return
    elif index== 1:
        n "Cas?{w=0.2} Did you hear me?"
        n "How long is this going to take?"
        $ renpy.pop_call()
        jump start.phonereturn1
        
    else:
        $ renpy.notify("No problem here.") #empty this out to nothing
        return

    return

label repeatcheck:
    #flags will change the specifics of who says what
    $ repeat_active = False #disable the repeat that button

    if since_last_repeat <= 4:
        n "What?{w=0.2} No!{w=0.2} Pay attention."
        $ since_last_repeat = 0
        $ repeat_active = True #reeneable the repeat that button
        return

    elif since_last_repeat > 4:
        n "Sure,{w=0.2} I can do that."
        call screen history(_with_none=False) as menu with dissolve 
        with dissolve
    
    $ since_last_repeat = 0
    $ repeat_active = True #reeneable the repeat that button

    #player can currently rollback into the history screen. 
    #prevent player from accessing rollback when game is closer to finished
    return

#ending
label theguy:
    c "I got the guy."
    n "You got the guy?" #Speaker depends on who's on screen right now. 
    c "I got the guy! {w=0.25}Oh my god,{w=0.25} I got the guy!"
    return

label postguy:
    "It's a lazy Saturday at the Spelltower,{w=0.25} and Cassiopeia is nowhere to be found."
    "Last week on Sunday,{w=0.25} when he tried to log in,{w=0.25} he got an error message saying the game needed to be updated."
    "Cassiopeia was sure his game was up-to-date,{w=0.25} but since he didn't know how to fix this error,{w=0.25} he had no choice but to set the game aside."
    "Well,{w=0.25} he hasn't thought about that game for a while."
    "He's on a date with Niecy right now and he couldn't be happier."
    return