#game mechanic
label lookuptable(index):
    #index is equal to a global variable that keeps track of where in the script you are
    #the test index is -1. if the index is null or 0, nothing happens.
    #it looks like we'll be manually setting the regions in which a phone interaction will trigger a dialogue.
    if renpy.get_screen("timed_menu")!= None:
        hide screen timed_menu
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
        g "Cassiopeia!"
        jump gabriel2.thereturn
        return
    elif index == 6:
        $story_index = 0
        $ will_capture_click = False
        $ renpy.pop_call()
        jump evenwhile
    elif index==7:
        $ story_index=0
        $ will_capture_click = False
        $ renpy.pop_call()
        jump niecynomoney.iwish
    elif index ==8:
        $ story_index=0
        $ will_capture_click = False
        $ renpy.pop_call()
        jump niecynomoney.stopclick        
    else:
        $ renpy.notify("No problem here.") #empty this out to nothing
        return

    return


#game mechanic
label repeatcheck:
    #flags will change the specifics of who says what
    $ repeat_requests += 1
    $ repeat_active = False #disable the repeat that button
    if gabriel_present:
        g "Absofuckinglutely not."
        return

    if block_repeat:
        n "Not now,{w=0.25} Cassiopeia."

    if since_last_repeat <= 4:
        n "You can't have forgotten that quickly.{w=0.25} C'mon,{w=0.25} man."
        $ since_last_repeat = 0
        $ repeat_active = True #reeneable the repeat that button
        return

    elif repeat_requests >= 10:
        if repeat_requests == 10:
            n "Cas...{w=0.25} I feel like you ask me to repeat everything these days."
            $ niecy_irritation +=1
        else:
            n "Fine..."
        call screen history (_with_none=False) as menu with dissolve
        with dissolve

    elif since_last_repeat > 4:
        n "Hm?" 
        n "Sure.{w=0.25} So what I was saying was..."
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


label gabrielcheck:
    if renpy.get_screen("timed_menu")!= None:
        hide screen timed_menu
    $ block_spontaneous = True
    $ story_index = 0
    $ gabriel_triggered = False
    if gabrieltriggercount <= 0:
        $ gabrieltriggercount+=1
        call gabriel1
    elif money_spent >=300:
        jump gabriel3
    elif gabrieltriggercount == 1:
        $ gabrieltriggercount +=1
        call gabriel2
    elif gabrieltriggercount ==2:
        $ gabrieltriggercount +=1
        call gabriel4
    else:
        return
        

label roll(pulls=0):
    $ can_pull = False
    $ gems_to_spend = pulls * pull_cost
    if gems_to_spend > gems:
        $ renpy.notify("Not enough gems!")
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
    if pulls > 0:
        show screen showguy (list_of_pulls)
    $ can_pull = True
    if will_capture_click:
        $ renpy.pop_call()
        call lookuptable(story_index)
    return

