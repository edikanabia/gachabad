# The script of the game goes in this file.

# The game starts here.

label start:

    #scene cg ceiling
    scene bg black

    show screen repeatthat
    #show screen testphone
    $ story_index = -1
    "It's a lazy Saturday,{w=0.2} and everyone in the Spelltower is cooped up indoors..."
    "Especially Cassiopeia.{w=0.2} Cassiopeia has been enamored with a new game he downloaded onto his new phone just last week!"
    "It's called...{w=0.2} um...{w=0.2} Well,{w=0.2} he can't remember what it's called.{w=0.2} But he's absolutely hooked!"
    $ story_index = 0
    $ preferences.afm_enable = True #we can use renpy code to enable auto-forward in the script.
    "The day he downloaded it,{w=0.2} he showed it to Gabriel in a euphoric frenzy."
    "But Gabriel,{w=0.2} in typical Gabriel fashion,{w=0.2} took one look at it and called him a moron."
    "So now he has to play it under the covers,{w=0.2} where no one can see his shame."

    #show screen phone

    "The guy Cassiopeia wants is in the time-limited banner today.{w=0.2} It's the last opportunity to get him before the next season starts---tomorrow!"
    "It would be a good time to try for the guy during some downtime." #set interact to false on this line until the gacha roll occurs.
    #the first roll will always fail
    $ is_first_roll = False

    #hide screen phone

    #play sound door_open
    "???" "Cassiopeia?{w=0.2} Are you in here?"
    "He knows that voice.{w=0.2} It's Niecy!"
    "...she cannot see him playing this game!"
    menu:
        "Say no":
            "Cassiopeia thinks he hears someone chuckle."
            n "Oooookay...{w=0.2} I guess he's not in here!"
            pass
        "Shake your head":
            n "Did something move under the- {nw=0.5}"
            pass

    #scene cg covers

    n "What are you doing?"
    menu:
        "Show her the phone":
            pass
        "Do not":
            "Cassiopeia holds the phone close to his chest and shakes his head."
            "Niecy assumes he must be looking at something lascivious,{w=0.2} like exposed ankles or toe tanlines."
            "She throws the cover back over him and leaves the room."
            "The end!"
            #it's not a dusty game without an early false ending!
            return
    
    "Cassiopeia turns the screen so Niecy can see."
    c "This."
    #show screen phone, pause, then hide the phone and continue.
    n "Oh.{w=0.2} Anyway,{w=0.2} wanna go out and do something?"
    c "Like what?"
    n "I don't know,{w=0.2} but it's Saturday.{w=0.2} There's probably something fun we could do."
    n "We could always just go to a park and hang."
    c "..."
    n "Cas?"
    c "Hm?"
    n "Does that sound good?"
    c "Yeah,{w=0.2} hang on."
    show screen testphone
    n "Okay...{nw=1.0}"(interact=False)
    n "Um,{w=0.2} how long is that gonna take?"
    $ story_index = 1
    menu:
        "Answer":
            $ story_index = 0
            c "Until I get the guy I want."
            n "Um..."
            n "Surely this can wait."
            c "No,{w=0.2} the season ends today."
            n "What does that mean?"
            c "It means today is the last day I can get him.{w=0.2} I HAVE to get him now."

    label .phonereturn1:
        $ story_index = 0
    n "...Cas,{w=0.2} I don't think this game is very good for you..."

    #end of intro.
    return

label partone:
    
    "{i}From now on, dialogue will automatically proceed based on your preferences.{/i}"
    "{i}You can change the duration of the auto-advance in the Preferences menu.{/i}"
    return

label phoneinterrupttest:
    g "Cassiopeia!{w=0.2} Surely,{w=0.2} this game can't be more important than your girlfriend."
    
    return