# The script of the game goes in this file.

# The game starts here.

label start:

    scene cg ceiling
    scene bg black
    #script subject to change. idk what the pov is or if there's a narrator.
    show screen repeatthat
    $ narrator = Character(what_style="bold")
    "It's a lazy Saturday,{w=0.5} and everyone in the Spelltower is cooped up indoors..."
    "Especially Cassiopeia.{w=0.5} Cassiopeia has been enamored with a new game he downloaded onto his new phone just last week!"
    "It's called...{w=0.5} um...{w=0.5} Well,{w=0.5} he can't remember what it's called.{w=0.5} But he's absolutely hooked!"
    "The day he downloaded it,{w=0.5} he showed it to Gabriel in a euphoric frenzy."
    "But Gabriel,{w=0.5} in typical Gabriel fashion,{w=0.5} took one look at it and called him a moron."
    "So now he has to play it under the covers,{w=0.5} where no one can see his shame."

    #show screen phone

    "The guy Cassiopeia wants is in the time-limited banner today.{w=0.5} It's the last opportunity to get him before the next season starts---tomorrow!"
    "It would be a good time to try for the guy during some downtime."

    #the first roll will always fail
    $ is_first_roll = False

    #hide screen phone

    #play sound door_open
    "???" "Cassiopeia?{w=0.5} Are you in here?"
    "He knows that voice.{w=0.5} It's Niecy!"
    "...she cannot see him playing this game!"
    menu:
        "No":
            pass
        "Shake your head":
            pass

    n "Are you...{w=0.5} under the..."
    #scene cg covers

    n "What are you doing?"
    menu:
        "Show her the phone":
            pass
        "Do not":
            pass

    



    return
