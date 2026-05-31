#game mechanic
label lookuptable(index):
    #index is equal to a global variable that keeps track of where in the script you are
    #the test index is -1. if the index is null or 0, nothing happens.
    #it looks like we'll be manually setting the regions in which a phone interaction will trigger a dialogue.

    if index == -1:
        $ story_index = 0
        #test index
        n "This is Niecy telling you to get off that damn phone!"
        return
    elif index == 1:
        $ story_index = 0
        #in start, after Niecy asks how long he's gonna play the game
        $ will_capture_click = False
        $ renpy.pop_call()
        n "Cas?{w=0.25} Did you hear me?"
        n "How long is this going to take?"
        c "Huh!?"
        jump start.phonereturn1
    elif index == 2:
        #Gabriel appearing for the first time
        $ story_index = 0
        $ renpy.pop_call()
        g "Cassiopeia!"
        jump gabriel1.ignore1
    elif index == 3:
        #time out
        $ story_index = 0
        $ renpy.pop_call()
        g "Are you kidding me!?"
        n "He's been glued to this thing for hours,{w=0.25} apparently.{w=0.25} Don't mind him."
        jump gabriel1.ignore2
    elif index == 4:
        #time out
        $ story_index = 0
        $ renpy.pop_call()
        e "How many fingers am I holding up?"
        n "Leave the man alone,{w=0.25} Ed."
        e "Whatever."
        jump quieres.ignore
    elif index == 5:
        $ story_index = 0
        $ renpy.pop_call()
        g "Unbelievable!"
        return
    elif index == 6:
        $story_index = 0
        $ will_capture_click = False
        $ renpy.pop_call()
        jump evenwhile
    else:
        $ renpy.notify("No problem here.") #empty this out to nothing
        return

    return


#game mechanic
label repeatcheck:
    #flags will change the specifics of who says what
    $ repeat_requests += 1
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

#game mechanic
label facecover:
    n confuse "..." #shocked
    n concern "{size=*0.5}At least pretend to pay attention...{/size}"
    return

label roll(pulls):
    $ can_pull = False
    $ gems_to_spend = pulls * pull_cost
    if gems_to_spend > gems:
        #show text "Not enough gems!"
        #hide text with dissolve
        $ can_pull = True
        return
    $ gems -= gems_to_spend

    $ iterator = 0
    while iterator < pulls:
        $ current_guy = gacha_puller.pull_guy()
        $ list_of_pulls.append(current_guy)

        #show guy with dissolve
        #show text "the guy's name"
        
        #hide guy with dissolve
        #hide text with dissolve
        #it might help to end the pulls early and jump out of the loop the moment cassiopeia pulls the guy
        #if current_guy.is_the_guy:
            #$ guy_end = True
            #but as of right now, jumping directly from the loop,
            #$ renpy.pop_call()
            #jump theguy
            #return
        $ iterator += 1
    show screen showguy (list_of_pulls)
    $ can_pull = True
    if will_capture_click:
        $renpy.pop_call()
        call lookuptable(story_index)
    return

