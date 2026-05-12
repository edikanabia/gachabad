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
    "The day he downloaded it,{w=0.2} he showed it to Gabriel in a euphoric frenzy."
    "But Gabriel,{w=0.2} in typical Gabriel fashion,{w=0.2} took one look at it and called him a moron."
    "So now he has to play it under the covers,{w=0.2} where no one can see his shame."

    #show screen phone

    "The guy Cassiopeia wants is in the time-limited banner today.{w=0.2} It's the last opportunity to get him before the next season starts---tomorrow!"
    "It would be a good time to try for the guy during some downtime."

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

    



    return

label phoneinterrupttest:
    g "Cassiopeia!{w=0.2} Surely,{w=0.2} this game can't be more important than your girlfriend."
    
    return