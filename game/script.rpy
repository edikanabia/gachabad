# The script of the game goes in this file.

# The game starts here.

label start:
    #scene cg ceiling
    scene bg black
    show screen testphone2
    jump scammer

    if persistent.got_the_guy:
        jump postguy
    else:
        pass

    show screen repeatthat
    #show screen testphone
    $ story_index = -1
    "It's a lazy Saturday at the Spelltower,{w=0.25} and everyone is cooped up indoors..." 
    "Especially Cassiopeia.{w=0.25} Cassiopeia has been enamored with a new game he downloaded onto his new phone just last week!"
    "It's called...{w=0.25} um...{w=0.25} Well,{w=0.25} he can't remember what it's called.{w=0.25} But he's absolutely hooked!"
    $ story_index = 0
    $ preferences.afm_enable = True #we can use renpy code to enable auto-forward in the script.
    "The day he downloaded it,{w=0.25} he showed it to Gabriel in a euphoric frenzy."
    "But Gabriel,{w=0.25} in typical Gabriel fashion,{w=0.25} took one look at it and called him a moron."
    "So now he has to play it under the covers,{w=0.25} where no one can see his shame."

    #show screen phone

    "The guy Cassiopeia wants is in the time-limited banner today.{w=0.25} It's the last opportunity to get him before the next season starts---tomorrow!"
    "It would be a good time to try for the guy during some downtime." #set interact to false on this line until the gacha roll occurs.
    #the first roll will always fail
    $ is_first_roll = False

    #hide screen phone

    #play sound door_open
    "???" "Cassiopeia?{w=0.25} Are you in here?"
    "He knows that voice.{w=0.25} It's Niecy!"
    "...she cannot see him playing this game!"
    menu:
        "Say no":
            "Cassiopeia thinks he hears someone chuckle."
            n "Oooookay...{w=0.25} I guess he's not in here!"
            pass
        "Shake your head":
            n "Did something move under the- {nw=0.5}"
            pass

    #scene cg covers
    #play sound fwoom

    n "What are you doing?"
    menu:
        "Show her the phone":
            pass
        "Do not":
            "Cassiopeia holds the phone close to his chest and shakes his head."
            "Niecy assumes he must be looking at something lascivious,{w=0.25} like exposed ankles or toe tanlines."
            "She throws the cover back over him and leaves the room."
            "The end!"
            #it's not a dusty game without an early false ending!
            return
        "Say it's porn to chase her off" if persistent.girlfriend_flag:
            jump jorkinit
    
    "Cassiopeia turns the screen so Niecy can see."
    c "This."
    #show screen phone, pause, then hide the phone and continue.
    n "Oh.{w=0.25} Anyway,{w=0.25} wanna go out and do something?"
    c "Like what?"
    n "I don't know,{w=0.25} but it's Saturday.{w=0.25} There's probably something fun we could do."
    n "We could always just go to a park and hang."
    c "..."
    n "Cas?"
    c "Hm?"
    n "Does that sound good?"
    c "Yeah,{w=0.25} hang on."
    show screen testphone
    n "Okay...{nw=1.0}"(interact=False)
    n "Um,{w=0.25} how long is that gonna take?"
    $ story_index = 1
    menu:
        "Answer":
            $ story_index = 0
            c "Until I get the guy I want."
            n "Um..."
            n "Surely this can wait."
            c "No,{w=0.25} the season ends today."
            n "What does that mean?"
            c "It means today is the last day I can get him.{w=0.25} I HAVE to get him now."

    label .phonereturn1:
        $ story_index = 0
    n "...Cas,{w=0.25} I don't think this game is very good for you..."

    #end of intro.
    return

#story path
label gabriel1:
    n "Oh!{w=0.25} Hey,{w=0.25} Gabriel!{w=0.25} How was your nap?"
    g "It's not done...{w=0.25} I'm about to go back to sleep,{w=0.25} but..."
    g "Piapia...{w=0.25} did you make a purchase recently?"
    $ story_index = 2
    menu:
        "Yes":
            $ story_index = 0
            g "That's okay...{w=0.25} Just don't forget to let me know ahead of time."
            return
        "No":
            $ story_index = 0
            g "Umm...{w=0.25} yeah you did,{w=0.25} but that's okay..."
            g "Just let me know next time,{w=0.25} and don't make a habit of lying..."
            return
    label .ignore1:
        $ story_index = 3
        g "Did you buy something!?"
        menu:
            "Yes":
                pass
            "No":
                pass
    label .ignore2:
        g "You're not even listening..."
        n "It's okay.{w=0.25} I can handle this."
        g "Are you sure?"
        
    return

#story path
label gabriel2:
    g "Piapia,{w=0.25} I gave you that card because I wanted you to be able to practice some autonomy."
    g "You've been so responsible iwith it up until now.{w=0.25} What happened!?"
    return

#story path
label jorkinit:
    c "Jorkin' it."
    n "With no hands,{w=0.25} buddy?"
    menu:
        "She's not buying it."
        "Double down":
            c "Uh-huh."
            "She gives him a once-over."
            n "Looks like it's slow-going."
            menu:
                "Commit to the bit":
                    c "These things take time,{w=0.25} you know?"
                    n "Oh,{w=0.25} I'm sure."
                    c "Well,{w=0.25} I'm gonna need some privacy.{w=0.25} Because I'm jorkin' it."
                    n "No you're not."
                    c "Yes I am."
                    n "{cps=*0.5}Nooooo{/cps} you're not!"
                    c "{i}Yes,{w=0.25}{/i} I am!"
                    "Niecy gives Cassiopeia one more chance to tell the truth before..."
                    "Hold on,{w=0.25} before what?{w=0.25} What's she gonna do!?{w=0.25} Her lips curl into a mischievous smile..."
                    menu:
                        "I'm totally jorkin' it, dog":
                            n "Then you don't have a problem with me joining you,{w=0.25} do you?{w=0.25} {i}If{/i} that's what you're doing."
                            menu:
                                "I don't":
                                    n "Wow!{w=0.25} {size=*0.75}Oh wow...{/size}"
                                    n "Well!{w=0.25} Here I go!"
                                    #fade to white
                                    show cg white with Dissolve(2.0)
                                    "For the rest of the afternoon,{w=0.25} Cassiopeia forgot all about the guy that he wanted..."
                                    #the end!
                                    return
                                    
                                "I do":
                                    n "Exactly.{w=0.25} Why are you trying to get rid of me so bad?"
                                    c "Because...{w=0.25} I'm playing my stupid game on my stupid phone.{w=0.25} Okay!?"
                                    n "Well yeah,{w=0.25} but other than that."
                                    c "That's it."
                                    n "...Seriously?"
                                    c "Yeah."
                                    "Niecy sighs."
                                    n "Cas...{w=0.25} {size=*0.85}Cassie.{/size}{w=0.25} You have an important decision to make:{w=0.25}{p=0.25}Which is more important to you?{w=0.25} Your girlfriend,{w=0.25} or your fucking telephone?"
                                    menu:
                                        "Touch of a woman":
                                            n "Good answer,{w=0.25} sweet pea."
                                            pass
                                        "My goddamn telephone":
                                            n "Well,{w=0.25} it can't be helped."
                                            #jump to the rest of the game...
                                            pass


                                    pass
                            pass
                        "Okay fine I'm on my stupid phone":
                            pass
                    pass
                "Drop the façade":
                    pass
            pass
        "Bail":
            pass
    return

#ending
label weed:
    show cg green with Dissolve(2.0)
    "Cassiopeia greened out!"
    return


#ending
label realed:
    c ""
    e "I'm a trickster,{w=0.25} not a terrorist."
    return

#ending
label scammer:


    
    c "Ah!{w=0.25} Uh-oh..."
    i "Cassiopeia?"
    #screenshake
    g "{size=*2}Cassiopeia!{/size}"  #probably a lot more angry
    i "What's going on?"
    g "Good,{w=0.25} you caught him.{w=0.25} Tell him stop spending my money on gacha games."
    i "Why?{w=0.25} He's not a child.{w=0.25} He can handle himself."
    c "Yeah,{w=0.25} I-I can handle myself!"
    g "No,{w=0.25} you've developed a gambling addiction over a mediocre RPG."
    i "Well...{w=0.25} It's not gambling if there's no monetary value involved."


    g "I've been trying to talk sense into him all day!{w=0.25} He needs to hear it from someone like you."
    i 'What do you mean "someone like me?"'
    g "You know,{w=0.25} someone who can embarrass him into straightening out!{w=0.25} You always do that."
    i "I don't know,{w=0.25} Gabriel.{w=0.25} It sounds like you bear the responsibility for this."
    i "If you don't want him spending your money,{w=0.25} don't give him your credit card."
    g "Oh,{w=0.25} come on.{w=0.25} I'm not a tyrant."
    i "Yes you are."(multiple=2)
    c "Yes you are..." (multiple=2)
    g "No,{w=0.25} I'm not-{w=0.25} I don't want to be-{w=0.25} Ngh!{w=0.25} You two are being impossible today!"
    #gabriel leaves

    c "Ed...{w=0.25} Thanks for standing up for me back there."
    i "Of course,{w=0.25} Cassiopeia.{w=0.25} I wouldn't think twice before helping you."
    c "Wow,{w=0.25} you've really changed a lot!{w=0.25} You must have had a serious change of heart."
    i "Er,{w=0.25} yes.{w=0.25} I have."
    c "You know I'm really happy to hear that.{w=0.25} I thought it'd never happen..."
    c "I guess...{w=0.25} I'll see you around,{w=0.25} then!"
    i "See you later,{w=0.25} man."
    #show cg edphone
    #show screen balance
    i "Heh.{w=0.25} Sucker..."
    #play sound ringtone
    #$ renpy.pause(1.0)
    #show cg impostor
    i "Hello?"
    i "Yes,{w=0.25} we've pinpointed the psychological profile of the ideal player for our new type of game."
    i "Should I proceed to the second phase of Operation Ruin All Video Games Forever?"
    i "Yes,{w=0.25} sir.{w=0.25} Right away,{w=0.25} sir."
    #play sound hangup


    return


#placeholder
label partone:
    
    "{i}When you see this icon,{w=0.25} dialogue will automatically proceed based on your preferences.{/i}"
    "{i}You can change the duration of Auto-Advance in the Preferences menu.{/i}"
    return

label phoneinterrupttest:
    g "Cassiopeia!{w=0.25} Surely,{w=0.25} this game can't be more important than your girlfriend."
    
    return