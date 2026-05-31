# The script of the game goes in this file.

# The game starts here.

label start:
    #scene cg ceiling
    scene bg black
    #show screen testphone2
    #jump scammer
    #show screen gachadebug
    #jump theendlessloop
    #jump givemeyourphone
    if persistent.got_the_guy:
        jump postguy
    else:
        pass
    #show screen repeatthat
    #show screen testphone2
    $ story_index = -1
    #call quieres #testing the weed mechanic
    #call screen tutorialize
    
    #jump gabriel2
    if persistent.niecy_complete:
        if persistent.gabriel_complete:
            if persistent.ed_complete:
                $ persistent.true_end

    "It's a lazy Saturday at the Spelltower,{w=0.25} and everyone is cooped up indoors..."
    "Especially Cassiopeia.{w=0.25} Cassiopeia has been enamored with a new game he downloaded onto his new phone just last week!"
    "It's called...{w=0.25} um...{w=0.25} Well,{w=0.25} he can't remember what it's called.{w=0.25} But he's absolutely hooked!"
    $ story_index = 0
    #$ preferences.afm_enable = True #we can use renpy code to enable auto-forward in the script.
    "The day he downloaded it,{w=0.25} he showed it to Gabriel in a euphoric frenzy."
    "But Gabriel,{w=0.25} in typical Gabriel fashion,{w=0.25} took one look at it and called him a moron."
    "So now he has to play it under the covers,{w=0.25} where no one can see his shame."

    "The guy Cassiopeia wants is in the time-limited banner today.{w=0.25} It's the last opportunity to get him before the next season starts—tomorrow!"
    #show the guy for a bit
    "It would be a good time to try for the guy during some downtime."
    call screen banner (phonexpos, phoneypos)
    #the first roll will always fail

    #hide screen banner

    #play sound door_open
    "???" "Cassiopeia?{w=0.25} Are you in here?"
    "He knows that voice.{w=0.25} It's Niecy!"
    "...she cannot see him playing this game!"
    #show screen timed_menu (5, "timeout")
    menu:
        "Say no":
            "Cassiopeia thinks he hears someone chuckle."
            n "Oooookay...{w=0.25} I guess he's not in here!"
            pass
        "Shake your head":
            #play sound covers
            n "Did something move under the... {nw=0.5}"
            #play sound footsteps
        "Don't move or say anything" if persistent.ed_not_niecy:
            "Cassiopeia lay on his bed in silence until he hears the footsteps recede."
            "Now he's in the dark and quiet."
            "Underneath his blanket fort (com-fort-er?) is the perfect nowhere to do nothing."
            "Disconnected from space,{w=0.25} disconnected from time,{w=0.25} in the recesses and crevices,{w=0.25} in the lulls in speech,{w=0.25} in thought."
            "Nowheres are everywhere,{w=0.25} created and collapsed in an instant.{w=0.25} Thousands of millions of people have wandered into a nowhere at least once."
            "These nowheres are collectively known as the Void."
            "Cassiopeia settles into his nowhere,{w=0.25} his eyelids hanging half-open under his phone's bluish glow, {w=0.25}veiled to the people mulling about the Spelltower..."
            jump realed
        "Get out of bed and greet your beautiful girlfriend" if persistent.true_end:
            jump trueend

    #play sound fwoom
    show bg white with Dissolve(1.0) #wipe up
    show cg covers 0 with Dissolve(0.2)

    n "What are you doing?"
    menu:
        "Show her the phone":
            pass
        "Do not":
            show cg covers 1
            "Cassiopeia holds the phone close to his chest and shakes his head."
            "Niecy assumes he must be looking at something lascivious,{w=0.25} like exposed ankles or toe tanlines."
            "She throws the cover back over him and leaves the room."
            "The end!"
            #it's not a dusty game without an early false ending!
            #$ persistent.true_reset_visible = True #move this to the other endings when building
            return
        "Say it's porn to chase her off": #if persistent.girlfriend_flag
            jump jorkinit
    
    "Cassiopeia turns the screen so Niecy can see."
    c "This."
    label .showphone:
        #show screen phone, pause, then hide the phone and continue.
        pass
    n "Oh.{w=0.25} Anyway,{w=0.25} wanna go out and do something?"
    c "Like what?"
    n "I don't know,{w=0.25} but it's Saturday.{w=0.25} There's probably something fun we could do."
    n "We could always just go to a park and hang."
    c "..."
    n "Cas?"
    c "Hm?"
    n "Does that sound good?"
    c "Yeah,{w=0.25} hang on."
    show screen banner (phonexpos, phoneypos) 
    label .aftertestphone:
        n "Okay...{nw=1.0}"
    n "Um,{w=0.25} how long is that gonna take?"
    $ story_index = 1
    $ will_capture_click = True

    menu:
        "Uhhh...":
            $ will_capture_click = False
            $ story_index = 0
            c "Until I get the guy I want?"
            n "Well...{w=0.25} I don't want to be dismissive,{w=0.25} but...{w=0.25} can it wait?"
            c "No,{w=0.25} the season ends today."
            n "Okay,{w=0.25} then,{w=0.25} I'll wait for you,{w=0.25} but while you do that..."

    label .phonereturn1:
        $ story_index = 0
    n "...we definitely need to talk."
    c "Huh...?"
    c "Y-yeah, {w=0.25}we can talk."
    #call screen tutorialbox1
    jump niecynomoney
    #end of intro.
    return

#storypath
label niecynomoney:
    scene bg room cassiopeia
    show niecy neutral with dissolve
    show screen autoplayactive with Dissolve(0.2)
    nauto "So,{w=0.25} like,{w=0.25} you've been spending a lot of time playing this game,{w=0.25} but you haven't spent any money on it,{w=0.25} right?{nw=[delay]}"
    nauto "I'm assuming not, {w=0.25}but I'm sure you can see the tradeoff.{nw=[delay]}"
    nauto "You are kind of selling your time instead of separating with your money...{nw=[delay]}"
    nauto "And,{w=0.25} like, {w=0.25}I think time is very precious!{w=0.25} We only have so much of it.{nw=[delay]}"
    nauto "That makes sense,{w=0.25} right?{nw=[delay]}"

    show screen timed_menu( q_delay,"niecynomoney.ignore1")
    menu:
        "Makes sense to me":
            pass
        "I don't get it":
            hide screen timed_menu
            nauto "Well,{w=0.25} it's like...{nw=[delay]}"
            nauto "Other players spend money on the game to get increased rewards.{nw=[delay]}"
            nauto "If you {i}don't{/i} spend that money,{w=0.25} you have a significantly decreased chance of getting those same rewards.{nw=[delay]}"
            nauto "Of course,{w=0.25} games that used to have very clear and obvious pay-to-win schemes didn't have a very high reputation...{nw=[delay]}"
            nauto "So developers started emphasizing how far you could get by playing for free.{w=0.25} You'd still have access to the same rewards as any other player.{nw=[delay]}"
            nauto "The thing is,{w=0.25} if you can buy your way out of having to grind for items,{w=0.25} that game is implicitly putting a price on the time its players spend grinding.{nw=[delay]}"
            if persistent.impostor_seen:
                call quieres
                nauto "Anyway...{nw=[delay]}"
            show screen timed_menu(q_delay, "helloooo")
            menu:
                n "You with me so far?"
                "Ye":
                    hide screen timed_menu
                    pass
                "Nah":
                    hide screen timed_menu
                    nauto "Uh, {w=0.25}basically what you need to know is what you save on money you pay in time.{nw=[delay]}"
                    cauto "Philosophical.{nw=[delay]}"
                    nauto "No, {w=0.25}it's very literal...{nw=[delay]}"
                    nauto "Anyways!{nw=[delay]}"
                    jump niecynomoney.sadness

            show screen timed_menu(q_delay, "niecynomoney.ignore1_1")        
            menu helloooo:
                n "Cassiopeia?"
                "I'm with you":
                    pass

                "My head's spinning":
                    hide screen timed_menu
                    nauto "Uh, {w=0.25}basically what you need to know is what you save on money you pay in time.{nw=[delay]}"
                    cauto "Philosophical.{nw=[delay]}"
                    nauto "No, {w=0.25}it's very literal...{nw=[delay]}"
                    nauto "Anyways!{nw=[delay]}"
                    jump niecynomoney.sadness

            pass
    hide screen timed_menu
    nauto "Great.{w=0.25} How much does it cost to purchase this season's Guy?{nw=[delay]}"
    cauto "Thousand bucks.{nw=[delay]}"
    nauto "Oh hell no.{w=0.25} How much did it cost to buy last season's Guy?{nw=[delay]}"
    cauto "Like, {w=0.25}forty, {w=0.25}from what I saw online...{nw=[delay]}"
    nauto "See? {size=*0.8}That proves my point a {i}lot{/i} better...{/size}{nw=[delay]}"
    nauto "This company thinks your... {w=0.25}how long have you been grinding? Since you woke up?{nw=[delay]}"
    nauto "Which is usually around 9 am or so...{nw=[delay]}"
    nauto "This company thinks five hours of your time is worth forty dollars.{nw=[delay]}"
    cauto "Woah...{nw=[delay]}"
    nauto "Right!{w=0.25} So...{nw=[delay]}"
    nauto "A-and I'm not trying to alarm you or anything,{w=0.25} but...{nw=[delay]}"
    label .sadness:
        nauto "I got a bit sad when I saw how easily you can give your time to this game.{nw=[delay]}"
    menu:
        "Why?":
            cauto "It's not like it's a person.{nw=[delay]}"
            nauto "It's exactly the fact that it's not a person that's making me upset,{w=0.25} Cas.{nw=[delay]}"
            nauto "It took a lot for us to get to where we're at now, {w=0.25}y'know?{nw=[delay]}"
            nauto "We barely get days like this that are just...{w=0.25} calm.{nw=[delay]}"
            jump niecynomoney.sadtimeout
        "I get you":
            nauto "So then why do you..."
            show screen timed_menu(short_delay[1], "niecynomoney.ignore1_1")
            menu:
                "Why do I what":
                    hide screen timed_menu
                    nauto "...no,{w=0.25} I can't stop you from playing a game.{nw=[delay]}"
                    nauto "I'm not an authoritarian.{nw=[delay]}"
                    jump niecynomoney.afterignore1
                "I'll stop playing the game":
                    hide screen timed_menu
                    hide screen autoplayactive
                    $ will_capture_click = True
                    n "..."
                    n "Really?"
                    n "Like,{w=0.25} we can go out today?"
                    menu:
                        "We can go out today":
                            $ renpy.hide_screen("phone")
                            hide screen timed_menu
                            $ will_capture_click
                            jump niecyendhappy
        
        
    
    label .ignore1:
        $ niecy_irritation += 1
        nauto concern "...or you could just ignore me.{w=0.25} That's cool, {w=0.25}too...{nw=[delay]}"
        jump niecynomoney.afterignore1

    label .ignore1_1:
        nauto "Never mind...{nw=[delay]}"
        jump niecynomoney.afterignore1

    label .sadtimeout:
        cauto "Mm-hm.{nw=[delay]}"
        nauto "Days like these are rare.{w=0.25} And I don't wanna feel like I'm squandering it,{w=0.25} you feel?{nw=[delay]}"
        $ story_index = 7
        $ will_capture_click = True
        cauto "Mm-hm...{nw=[delay]}"
        nauto "Even if I'm just laying still for a bit next to you,{w=0.25} just enjoying your presence.{nw=[delay]}"
        nauto "I wanna do {i}something.{/i} I wanna really stretch the moment...{nw=[delay]}"
        "...{nw=[delay]}"
        $ will_capture_click = False
        $ story_index = 0
        nauto "Cassiopeia?{nw=[delay]}"
        menu:
            "Yes?":
                pass
            "Be quiet":
                nauto unimpressed "!?{nw=[delay]}"
                nauto smile open "Ah...{w=0.25} yeah...{nw=[delay]}"
                pass
        nauto smile close "Actually,{w=0.25} this is fine...{nw=[delay]}"
        jump niecyendnormal


    label .iwish:
        $ niecy_irritation += 1
        nauto confuse "...{nw=[delay]}"
        nauto "{size=0.75}I really wish you wouldn't use your phone while I'm trying to talk to you...{/size}"

    label .afterignore1:
        nauto "Let's see... {size=*0.8}What else...{/size}{nw=[delay]}"

    nauto "How many hours have you put into the game so far?"
    
    show screen timed_menu (q_delay,"niecynomoney.team")
    menu hours:
        "Eh, not a lot":
            nauto "...Cassiopeia,{w=0.25} I think that might be more than the amount of hours we've spent on a date together.{nw=[delay]}"
            cauto "Really?{w=0.25} I don't think it's that much.{nw=[delay]}"
            nauto "But that's exactly my point. It might not be much time to you but it is time better served somewhere else.{nw=[delay]}"
        "Nunya":
            nauto "It most definitely is my business,{w=0.25} Cassiopito.{nw=[delay]}"
            "Cassiopeia firmly shakes his head.{nw=[delay]}" (advance=False)
            nauto "It's my business if it cuts into my time.{nw=[delay]}"
            cauto "It's not your business and it's not your time{nw=[delay]}"
            nauto "Yes it is.{nw=0.25}"
            cauto "No it's not.{nw=0.25}"
            nauto "Yes it is!{nw=0.25}"
            cauto "No,{w=0.25} it's not!{nw=0.25}"
            pass
    label .team:        
        nauto "Cassiopeia, {w=0.25}we're supposed to be a team.{nw=[delay]}"
    nauto "What does it mean if I have to go looking for you in the middle of the day because you're hiding from me?{nw=[delay]}"
    nauto "And it goes back to what I was saying earlier:{w=0.25} time is literally money.{nw=[delay]}"
    nauto "Like,{w=0.25} I really think this game is bad for you.{nw=[delay]}"
    
    menu:
        "I disagree":
            pass
    
    label .justhink:
        hide screen autoplayactive
        n angry "OK,{w=0.25} well,{w=0.25} just think about it,{w=0.25} OK!?"
        jump niecyendsad


    label .stopclick:
        hide screen autoplayactive
        n "Oh.{w=0.25} So you were just... {w=0.25}lying?"
        jump niecyendsad

    return

#storypath
label niecymoney:
    $ money_route = True
    nauto "Okay... so.{nw=[delay]}"
    nauto "Spending money on the game is definitely a step in the wrong direction, but we can work it out. {nw=[delay]}"
    nauto "What did you end up buying?{nw=[delay]}"
    menu:
        "Gems":
            pass
        "Clocks (to get more gems)":
            pass
    cauto "I really wish I could just buy the guy outright,{w=0.25} though.{nw=[delay]}"
    nauto "Do not do that under any circumstances.{nw=[delay]}"
    if persistent.bought_the_guy:
        cauto "You don't need to tell me twice.{nw=[delay]}"
    else:
        cauto "Understood...{nw=[delay]}"
    return

#storypath
label gabrielroute:
    gauto "So!{w=0.25} Tell me,{w=0.25} what is this game?{w=0.25} What's it about?{nw=[delay]}"
    
    show screen timed_menu( q_delay,"gabrielroute.ignore1")
    menu:
        "It's an RPG...":
            $ game_genre = "RPG"
            pass
        "It's an idle game...":
            $ game_genre = "idle game"
            pass
        "It's an action-adventure game...":
            $ game_genre = "action-adventure game"
            pass
    hide screen timed_menu

    show screen timed_menu( q_delay,"gabrielroute.ignore2")
    menu:
        "About a princess...":            
            pass
        "About an entourage...":
            pass
        "About a frog...":
            pass
    hide screen timed_menu

    show screen timed_menu( q_delay,"gabrielroute.ignore2")
    menu:
        "Who explores a vast continent.":
            pass
        "Who must uncover the mystery of their past.":
            pass
        "Who must battle hordes of monsters.":
            pass
    
    gauto "Okay,{w=0.25} I see...{nw=[delay]}"
    gauto "{size=*0.75}It doesn't seem terribly original...{/size}{nw=[delay]}"

    gauto "What do you like about it?{nw=[delay]}"
    menu:
        "The Guys":
            pass
        "I don't like it":
            hide screen autoplayactive
            g "Huh!? {w=0.25}So what's all the hubbub for?!"
            g "You've been stressing out your dear girlfriend over a game you {i}don't{/i} like?"
            g "It's just you and a couple of dumb bitches telling each other \"exactly!\""
            g "Give me that!"
            "Before he even has a chance to react,{w=0.25} Gabriel snatches the phone from Cassiopeia's hand..."
            jump gavephone
            pass
    gauto "Right... the Guys."
    
    label .ignore1:
        gauto "If you can't even tell me,{w=0.25} there's no reason for you to keep playing it.{nw=[delay]}"
        jump gabrielroute.afterignore

    
    label .ignore2:
        gauto "Can't even finish the thought?{nw=[delay]}"
        jump gabrielroute.afterignore
    
    label .afterignore:
        gauto "Anyway...{nw=[delay]}"
    

    g "Just how much money did you spend on this thing,{w=0.25} anyway...?"
    if money_spent > 300:
        gauto "JESUS CHRIST-{nw=0.5}"
        gauto "[money_spent] DOLLARS!?"
        jump givemeyourphone
    elif money_spent <= 300 and money_spent >= 100:
        gauto "[money_spent] dollars?{w=0.25} You're killing me,{w=0.25} man."
    elif money_spent < 100:
        gauto "Less than a hundred bucks,{w=0.25} huh?"
        gauto "It's still not great for such a short period of playing, {w=0.25}but I guess I..."
        gauto "No. I still don't condone this, Piapia. Go be with your wife."

    return

#storypath
label realed:
    show cg covers 3 with Dissolve(0.2)
    e "Yo.{w=0.25} Get up."
    "He's so assertive Cassiopeia has no choice but to oblige."
    show bg room cassiopeia
    #show ed neutral
    hide cg with dissolve
    c "So we're not even saying hello anymore?"
    e "I've never said hello to you before in my life.{w=0.25} I'm here to tell you to get off that phone and go be with your wife."
    c "Dude,{w=0.25} I'm gonna... {w=0.25}just as soon as I can get some items and characters that will-{nw=0.5}"
    e "Ahem:{w=0.25} I'm here to tell you to get off that phone {w=0.1}{i}now.{/i}"
    c "Don't...{w=0.25} You can't talk to me like that."
    e "What?"
    c "You can't talk to me like that!{w=0.25} You can't just go back to pretending like you hate me!"
    e "Au contraire,{w=0.25} my friend. {w=0.25}T'is an act of love."
    e "I'm telling you this because if you break Niecy's heart,{w=0.25} I beat the shit outta you. {w=0.25}Simple as."
    c "No,{w=0.25} no,{w=0.25} no! {w=0.25}You weren't like this last week!{w=0.25} You were different!"
    e "What?"
    c "You were different!{w=0.25} You had a different demeanor,{w=0.25} a different tone... {w=0.25}different!{w=0.25} You were different!"
    e "..."
    e "Elaborate on that."
    c "Last week,{w=0.25} you approached me."
    c "I got all tense,{w=0.25} like usual, {w=0.25}but instead of teasing me, {w=0.25}you said hello."
    c "We even spoke for a while. {w=0.25}We told each other jokes and stuff. {w=0.25}Then you told me about the game. {w=0.25}You said you were playing it!"
    c "That's why I started...{w=0.25} I thought it was something I could connect with...{w=0.25} um..."
    c "Well,{w=0.25} yeah. {w=0.25}Yeah. {w=0.25}I talked to you last week and you were cool."
    c "Not like now."
    e "Well?"
    e "That's impossible because last week I was in Dubai."
    c "Dubai? {w=0.25}That's not very woke of you."
    e "..."
    e impressed "{size=*0.85}(He's right,{w=0.25} but...){/size}"
    e "Listen,{w=0.25} you didn't find any of that suspicious?"
    c "Well,{w=0.25} you definitely didn't look as hot as you do now,{w=0.25} but...{nw=0.5}"
    e "{size=*0.85}I didn't look what now?{/size}{nw=0.5}"
    c "I don't know,{w=0.25} I wanted to talk to you."
    c "...I thought you changed."
    e "Change takes a lot longer than a week when you're as old as I am."
    c "You keep saying that. {w=0.25}You don't look a day older than 30."
    e smug "So I've been told." #smug
    e "But I'm sure last week I was the same as ever.{w=0.25} Because I don't remember a lick of this."
    e "If I didn't know any better,{w=0.25} I'd be offended you would ever accuse me of playing a video game."
    c "You're not lying to me,{w=0.25} are you?"
    e "I already told you I was in Dubai.{w=0.25} I lie to make myself look better, {w=0.25}not worse."
    c "So what now?{w=0.25} What happens now?"
    #ed smug
    e "What happens is you go be with your wife and forget you ever saw anything."
    e "I have some business to take care of."

    #edpath complete (optional for completion)

    return


#story path
label jorkinit:
    c "Jorkin' it."
    show cg covers 2 with Dissolve(0.2)
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
                    "Hold on,{w=0.25} before what?{w=0.25} What's she gonna do!?"
                    menu:
                        "I'm totally jorkin' it, dog":
                            n "Then you don't have a problem with me joining you,{w=0.25} do you?{w=0.25} {i}If{/i} that's what you're doing."
                            menu:
                                "I don't":
                                    #there's also the idea for the game loop here where you pull out your phone and she gets mad at you
                                    #if you click on it.
                                    c "I'm not in the mood for anything really intense,{w=0.25} though."
                                    n "That's OK.{w=0.25} Let's just cuddle."
                                    show bg black
                                    hide cg covers with dissolve

                                    "She shuffles into bed with him."
                                    show screen banner (phonexpos, phoneypos) with Dissolve(5.0)
                                    $ story_index = 6
                                    $ will_capture_click = True
                                    "...{nw=1.0}"
                                    n "This is nice, {w=0.25}isn't it?{nw=1.0}"
                                    "...{nw=1.0}"
                                    "Niecy presses her head into the crook of his neck.{nw=1.0}"
                                    "...{nw=1.0}"
                                    "...{nw=1.0}"
                                    n "...you're warm.{nw=1.0}"
                                    "...{nw=1.0}"
                                    "...{nw=1.0}"
                                    "...{nw=1.0}"
                                    "Cassiopeia feels something light and tingly underneath his chin.{nw=1.0}"
                                    $ will_capture_click = False
                                    $ block_spontaneous
                                    hide screen phone
                                    c "Niecy?"
                                    n "Mm-hm?"
                                    c "I'm ready for something more intense now."
                                    n "Oh! {w=0.25}Already?"
                                    c "Uh-huh."
                                    n "Wow!{w=0.25} {size=*0.75}Oh wow...{/size}"
                                    n "Well...!{w=0.25} Here I go!"
                                    #fade to white
                                    show cg white with Dissolve(2.0)
                                    "For the rest of the afternoon,{w=0.25} Cassiopeia forgot all about the guy that he wanted..."
                                    #the end!
                                    return
                                    
                                "I do":
                                    show cg covers 1 with Dissolve(0.2)
                                    n "Exactly.{w=0.25} Why are you trying to get rid of me so bad?"
                                    c "Because...{w=0.25} I'm playing my stupid game on my stupid phone.{w=0.25} OK!?"
                                    n "Well yeah,{w=0.25} but other than that."
                                    c "That's it."
                                    show cg covers 0 with Dissolve(0.2)
                                    pause 1.0
                                    n "...Seriously?"
                                    c "Yeah."
                                    "Niecy sighs."
                                    show cg covers 2 with Dissolve(0.2)
                                    c "I was worried you would think it was silly."
                                    n "I mean,{w=0.25} it's a video game.{w=0.25} All video games are a bit silly."
                                    c "I know,{w=0.25} but I can't really put it down.{w=0.25} The game. {w=0.25}That's the silly part..."
                                    n "That's...{w=0.25} concerning,{w=0.25} but it really just comes to this:{w=0.25}{p=0.25}Which is more important to you?{w=0.25} Your girlfriend,{w=0.25} or your {cps=*0.5}fffffff{/cps}ucking telephone?"
                                    menu:
                                        "Touch of a woman":
                                            show cg covers 2 with Dissolve(0.2)
                                            n "Good answer,{w=0.25} sweet pea."
                                            "For the rest of the afternoon,{w=0.25} Cassiopeia forgot all about the guy that he wanted..."
                                            return
                                        "My goddamn telephone":
                                            n "Tch!"
                                            n "To think you've experienced love...{w=0.25} On your {cps=*0.5}fffffff{/cps}ucking telephone!{w=0.25} Get real!"
                                            #david lynch ending

                                            return

                            pass
                        "Okay fine I'm on my stupid phone":
                            n "You don't have to call it stupid."
                            c "It is stupid. {w=0.25}Gabriel said I was stupid for playing it,{w=0.25} right?"
                            n "I understand his concern but I don't think he was right to say that to you."
                            pass

                "Drop the façade":
                    c "Yeah..."
                    n "Not in the mood,{w=0.25} huh?"
                    c "Not really...{w=0.25} I mean,{w=0.25} I'm not {i}opposed{/i} to getting in the mood."
                    c "I'm just...{w=0.25} doing something else."
                    n "So,{w=0.25} what is it?"
            
        "Bail":
            "Cassiopeia sighs."
            c "No..."
            c "I'm doing this."
            
    jump start.showphone
    return

label evenwhile:
    $ will_capture_click = False
    if renpy.get_screen("phone") != None:
        $ renpy.hide_screen("phone")
    hide screen countdown
    n "Cassiopeia, {w=0.25}are you serious right now? {w=0.25}You can't get off your phone long enough to just cuddle with me?"
    c "No! {w=0.25}I can't!{w=0.25} I can't even stop thinking about it!"
    c "I...{w=0.25} I don't even think I like playing it all that much,{w=0.25} but when I don't play it,{w=0.25} I get all itchy!{w=0.25} I don't know why!"
    c "I'm sorry, {w=0.25}Niecy! {w=0.25}I want to spend time with you!{w=0.25} I really do!{w=0.25} I don't know what's wrong with me!"
    n "Woah,{w=0.25} woah, {w=0.25}woah! {w=0.25}Cas, {w=0.25}it's okay!"
    c "I'm sorry... {w=0.25}I didn't mean to yell like that."
    n "It's all right... {w=0.25}I'm not mad as much as I am worried about you, {w=0.25}y'know?"
    n "I don't think there's anything {i}wrong{/i} with you, {w=0.25}Cas."
    n "You've never experienced a game like this before, {w=0.25}so it's no wonder it's got you in a chokehold."
    n "It's just the nature of that kind of game. {w=0.25}It's designed to suck people in."
    n "How'd you even get into this game, {w=0.25}anyway?"
    c "Ed told me about it."
    n "Really?{w=0.25} When?"
    c "Last week or so... {w=0.25}But it's weird..."
    c "These days when I ask him about it, {w=0.25}he says he doesn't know what I'm talking about."
    n "Huh. {w=0.25}That is weird."
    "A beat between the two.{w=0.25} Then Cassiopeia breaks the silence."
    c "I'm sorry... {w=0.25}I completely ruined the mood."
    n "Heh...{w=0.25} Says who?"
    c "Says...{w=0.25} um..."
    "He catches on."
    c "Ah."
    
    return

label niecyendhappy:
    n "O...OK!"
    n "Where should we go!?"
    c "I thought you had somewhere in mind."
    n "I..."
    n "I forgot."
    $ persistent.niecy_complete = True

label niecyendnormal
    n "Welp!"
    n "That's all I wanted say!"
    n "Hope you'll consider it."
    if found_ed_flag:
        jump edunlock
    n "If you get the Guy today,{w=0.25} let me know so I can make plans before it gets too late to go out."
    n "Later,{w=0.25} Cas!"
    $ persistent.niecy_complete = True

label niecyendsad:

    n "I don't really have anything else to add..."
    if found_ed_flag:
        jump edunlock

    n "I hope that was valuable... {w=0.25}If you ever get that Guy,{w=0.25} just let me know..."
    c "Mm-hm."
    n "See you around, {w=0.25}Cassiopeia..."
    $ persistent.niecy_complete = True
    return


#event ending niecy
label edunlock:
    #play sound crash
    n "What on earth was that!?"
    #footsteps, go into the hallway
    e "Goddammit,{w=0.25} I knew I wasn't high...{w=0.25} After him!"
    e "He's going to ruin video games forever!"
    i "You're too late,{w=0.25} servants of the well-dressed nonbinary drag queen with an incoherent political ideology!"
    i "I've already launched the animated series for your precious Cassiopeia's favorite game.{w=0.25} It will live in the public consciousness for the rest of the century!"
    i "People the world over will willingly degrade their relationships and jeopardize their finances because they can't stop playing our game..."
    i "More and more studios will make games just like it in the hopes that they can replicate our success..."
    i "In mere months,{w=0.25} the gaming landscape will be awash with psychological manipulation and unscrupulous busineess practices!"
    i "No developer is safe!{w=0.25} Ohoho,{w=0.25} it's delightful!"
    e "Bastard!{w=0.25} Who sent you!?"
    i "Well,{w=0.25} well,{w=0.25} well,{w=0.25} if it isn't the immortal warlock himself!"
    i "Did you think we would forget your little stint in the Trickster God Wars?"
    i "But no worries,{w=0.25} my friend! {w=0.25}We know just how much you {i}love{/i} your earthly delights."
    i "So we've decided you can have a front row seat to the enshittification of everything you love!"
    i "Ahahahahahahahahahahaha-{nw}"
    #show cg neck snap
    g "I've had enough of that guy."
    c "Ed,{w=0.25} did they say you were immortal?"
    g 'No,{w=0.25} Piapia,{w=0.25} they said he was "infertile."{w=0.25} Immortals aren\'t real.'
    c "Oh.{w=0.25} Right."
    #play sound horse
    c "Of horse."
    e "Well.{w=0.25} You got them.{w=0.25} So,{w=0.25} thanks,{w=0.25} Gabriel."
    n "But they said we're too late,{w=0.25} and I think they're right..."
    n "Games like Cassiopeia's are everywhere already.{w=0.25} And they're seriously popular."
    #show cg pan out
    n "There's nothing we can do..."

    $ persistent.ed_complete = True

    return

#event ed
label cantfeelshit:
    "..."
    $ spontaneous_handler.add_spontaneous(Spontaneous("weed", 0, "weed", jump=True, lines_until=5))
    "Nothing happened..."
    return

#event ed
label quieres:
    $ found_ed_flag = True
    $ block_repeat = True
    show ed neutral:
        xalign 0.75
    e "Yo.{nw=[delay]}"
    n "What's up?{nw=[delay]}"
    e "Anyone else see a demon prowling around?{w=0.25} I thought I saw one go into the break room.{nw=[delay]}"
    n "Maybe it's because you took the Edible That Makes You See Demons and Forget You Took the Edible That Makes You See Demons?{nw=[delay]}"
    e "Oh yeah...{w=0.25} That's probably one of my best inventions.{nw=[delay]}"
    n "It's not even close to your top 75.{nw=[delay]}"
    e "Everyone's a critic.{nw=[delay]}" #ed annoyed
    e "Yo C-man,{w=0.25} you want one?{nw=[delay]}"
    $ will_capture_click = True
    $ story_index = 4
    show screen timed_menu (q_delay,"quieres.ignore")
    menu:
        "Sure":
            pass
        "What did you call me":
            pass
    hide screen timed_menu
    $ will_capture_click = False
    $ has_gummy = True
    show cutin gummy1 with dissolve:
        align (0.2, 0.4)
    pause 1.0
    show maskedcutin as cutin2 with dissolve


    hide cutin with dissolve
    hide cutin2 with dissolve

    eauto "See ya.{nw=[delay]}"
    if has_gummy:
        cauto "So...{w=0.25} what happens if I take this?{nw=[delay]}"
        nauto "Don't eat that.{nw=[delay]}"
        show screen deliciousgummy
        $ block_repeat = False
        return

    label .ignore:
        show ed finger
        eauto "How many fingers am I holding up?{nw=[delay]}"
        nauto "Leave the man alone, {w=0.25}Ed.{nw=[delay]}"
        eauto "Tuh.{nw=[delay]}"
    $ block_repeat = False
    return

#event gabriel
label gabriel1:
    show gabriel groggy:
        xalign 0.75
    nauto "Hey,{w=0.25} Gabriel.{w=0.25} How was your nap?{nw=[delay]}"
    gauto "It's not done...{w=0.25} I'm about to go back to sleep,{w=0.25} but...{nw=[delay]}"
    gauto "Piapia...{w=0.25} did you make a purchase recently?{nw=[delay]}"
    $ story_index = 2
    show screen timed_menu(q_delay,"gabriel1.ignore0")
    menu:
        "Yes":
            hide screen timed_menu
            $ story_index = 0
            gauto "That's okay...{w=0.25} Just don't forget to let me know ahead of time.{nw=[delay]}"
            hide gabriel with dissolve
            return
        "No":
            hide screen timed_menu
            $ story_index = 0
            gauto annoyed "Umm...{w=0.25} yeah you did,{w=0.25} but that's okay...{nw=[delay]}"
            gauto "I can see the purchases on my phone,{w=0.25} you know.{w=0.25} The buzzing woke me up.{nw=[delay]}"
            gauto neutral "It's OK this time,{w=0.25} but don't make a habit of lying...{nw=[delay]}"
            hide gabriel with dissolve
            return
    label .ignore0:
        gauto "Cassiopeia!{nw=[delay]}"

    label .ignore1:
        $ story_index = 3
        gauto "Did you buy something!?{nw=[delay]}"
        show screen timed_menu(q_delay,"gabriel1.phoneignore")
        $ will_capture_click = True
        menu:
            "Yes":
                $ will_capture_click = False
                gauto "I thought so.{nw=[delay]}"
            "No":
                gauto "Yeah, {w=0.25}well, {w=0.25}I see a purchase right here, {w=0.25}so.{nw=[delay]}"
        jump gabriel1.answer2

    label .phoneignore:
        $ will_capture_click = False
        gauto "You're not even listening...{nw=[delay]}"
        nauto "It's okay.{w=0.25} I can handle this.{nw=[delay]}"

    
    label .ignore2:
        if niecy_irritation > 2:
            gauto "No,{w=0.25} you look genuinely irritated already. {w=0.25}You aren't typically like that with him.{nw=[delay]}"
            nauto "I know, {w=0.25}but I have to try...{nw=[delay]}"
            gauto "Sweetheart. {w=0.25}Let me talk to him. {w=0.25}I'll straighten him out.{nw=[delay]}"
            nauto "Oh... {w=0.25}okay...{nw=[delay]}"
            hide niecy with dissolve
            jump gabrielroute
        else:
            gauto "Are you sure,{w=0.25} sweetheart?{nw=[delay]}"
            nauto "Positive.{nw=[delay]}"
            gauto "All right,{w=0.25} I'll leave you to it...{w=0.25} but Cassiopeia?{nw=[delay]}"
            gauto "Stop spending my money on gacha games.{nw=[delay]}"
            hide gabriel
            #stop spending my money on gacha games. cg and sound. fade to white. hide cg. 
            return     
    label .answer2:
        gauto "Listen,{w=0.25} whatever it is you bought,{w=0.25} keep it under 50 bucks.{nw=[delay]}"
        gauto "I'm going back to bed.{nw=[delay]}"
        nauto "See ya.{nw=[delay]}"
        gauto "Mm-hm.{nw=[delay]}"

    return

label gabriel4:
    gauto "Come on.{w=0.25} Again?{nw=[delay]}"
    gauto "Piapia,{w=0.25} I gave you that card because I wanted you to be able to practice some autonomy.{nw=[delay]}"
    gauto "You've been so responsible with it up until now.{w=0.25} What happened?{nw=[delay]}"
    cauto 'Nothing "happened,"{w=0.25} Gabriel.{w=0.25} I\'m fine.{nw=[delay]}'
    gauto "But you're not fine,{w=0.25} Piapia. {w=0.25}You're holed up in your room and playing on your phone,{w=0.25} spending money you've never spent before.{nw=[delay]}"
    gauto "This?{w=0.25} Can't continue. {w=0.25}Something's got to give.{nw=[delay]}"

    return


label gabriel2:
    show gabriel annoyed:
        xalign 0.75
    gauto "Cassiopeia!{w=0.25} I can see you spending decent money on this thing instead of an afternoon out!{nw=[delay]}"
    $ story_index = 5
    gauto "Surely,{w=0.25} this game can't be more important than your girlfriend.{nw=[delay]}"
    $ found_gf_flag = True
    $ will_capture_click = True
    menu:
        "It isn't":
            pass
    $ will_capture_click = False
    cauto "I'm not ignoring her!{nw=[delay]}"
    gauto "Then why are you tap tap tapping when she's standing right in front of you!?{nw=[delay]}"
    label .thereturn:
        gauto "Don't make me come in here again!{nw=[delay]}"
    hide gabriel
    return

#event gabriel
label gabriel3:
    #play sound door slamming open
    show gabriel rage:
        xalign 0.75
    pause 1.0

    jump givemeyourphone
    return

#event ending
label instakill:
    show bg black
    pause 1.0
    #if music is playing stop music
    #show cg instakill
    $ persistent.bought_the_guy = True
    return

label givemeyourphone:
    g "THAT'S IT."
    g "CASSIOPEIA."
    g "GIVE ME YOUR PHONE."
    call screen givephone
    return

#ending
label escapeseq:
    #show the escape sequence
    "As Cassiopeia makes a mad dash for the halls,{w=0.25} he runs into an unfamiliar familiar face..."
    
    jump scammer
    return

#ending
label gavephone:
    #show the give phone cgs
    g "Good."
    g "You can have this back in a week."
    "Gabriel sighs."
    g "Piapia.{w=0.25} You know I love you. {w=0.25}But you understand what you did was wrong,{w=0.25} right?"
    c "No,{w=0.25} actually. {w=0.25}I don't think it's wrong to play a game."
    "Gabriel groans,{w=0.25} realizing he has no way to make Cassiopeia understand his perspective."
    g "Well,{w=0.25} give it a week and you'll forget all about it. {w=0.25}OK?"
    c "..." #pouting
    g "{i}OK?{/i}"
    c "OK..."
    $ persistent.gabriel_complete = True
    #set flag end of gabriel route
    return


#ending
label weed:
    #stop auto forward
    #if music is playing stop the music
    c "Uh,{w=0.25} hold on."
    c "I feel a little,{w=0.25} uh, {w=0.25}I feel a little..."
    c "Uh...{nw=0.25}"

    show cg green with Dissolve(2.0)
    "Cassiopeia greened out!"
    return

#ending
label scammer:

    c "Ah!{w=0.25} Uh-oh..."
    i "Cassiopeia?"
    #screenshake
    g "{size=*2}Cassiopeia!{/size}"  #probably a lot more angry
    #show gabriel
    g "Oh,{w=0.25} good,{w=0.25} you caught him."
    i "Gabriel. {w=0.25}What's going on?"
    g "This little shit thinks he can pull a fast one on me!"
    i "Can he?"
    g "Not the point."
    g "Tell him to learn how to behave when he talks to me."
    i "Why?{w=0.25} He's not a child.{w=0.25} He can handle himself."
    c "Yeah,{w=0.25} I-I can handle myself!"
    g "No,{w=0.25} clearly,{w=0.25} you can't,{w=0.25} since you ran away like a child afraid to face a consequence."
    i "Why are you reprimanding him like a child?"
    g "Some things need reprimanding,{w=0.25} {i}sweetness.{/i} {w=0.25}He's been spending my money on gacha games."
    i "What's the harm in that?{w=0.25} It's just a video game."
    g "Absolutely not.{w=0.25} Piapia almost got a gambling habit before I nipped in the bud."
    i "It's not legally gambling if the prize has no real-world monetary value.{w=0.25}"
    i "And no one's forcing him to pay for it,{w=0.25} either. {w=0.25}People play for free all the time."
    i "I'm sure he's just spending a little extra because he likes the game."
    g "No,{w=0.25} that thing is preying on his poor impulse control!{w=0.25} It's got its hooks in his brain already."
    g "I've been trying to talk sense into him all day!{w=0.25} Tell him!{w=0.25} He needs to hear it from someone like you."
    i 'What do you mean "someone like me?"'
    g "You know,{w=0.25} someone who can embarrass him into straightening out!{w=0.25} You always do that."
    i "I don't know,{w=0.25} Gabriel.{w=0.25} It sounds like you bear the responsibility for this."
    i "If you didn't want him spending your money,{w=0.25} you shouldn't have him your credit card."
    g "Oh,{w=0.25} come on,{w=0.25} you know he doesn't have-{w=0.25} I'm not a tyrant!"
    i "Yes you are."(multiple=2)
    c "Yes you are..." (multiple=2)
    g "No,{w=0.25} I'm not-{w=0.25} I don't want to be-{w=0.25} Ngh!{w=0.25} You two are being impossible today!"
    #gabriel leaves

    c "Ed...{w=0.25} Thanks for standing up for me back there."
    i "Of course,{w=0.25} Cassiopeia.{w=0.25} I wouldn't think twice before helping you."
    c "Wow,{w=0.25} you've really changed a lot!{w=0.25} You must have had a serious change of heart."
    i "Er,{w=0.25} yes.{w=0.25} I have."
    c "You know,{w=0.25} I'm really happy to hear that.{w=0.25} I thought it'd never happen..."
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

    $ persistent.gabriel_complete = True
    $ persistent.impostor_seen = True
    return


#ending
label trueend:
    n "There you are!"
    n "What have you been doing?{w=0.25} It's such a beautiful Saturday."
    c "Oh...{w=0.25} I've been trying for this guy on this game I've been playing,{w=0.25} but no luck so far..."
    c "I think I'm gonna put it down. {w=0.25}I'll pick it up later,{w=0.25} maybe."
    n "You bored?{w=0.25} Cuz I'm bored,{w=0.25} and you sound {i}hella{/i} bored."
    c "Yeah...{w=0.25} I'm pretty bored."
    n "Can I chill with you for a bit?"
    c "Sure!"
    #cg niecy chilling on the floor
    n "I wanna talk to the other people in the Tower but I'm pretty sure Gabriel's asleep and I don't know where Ed is."
    n "I mean,{w=0.25} I know you and Ed don't really get along,{w=0.25} but-"
    c "I try.{w=0.25} I really try,{w=0.25} Niecy..."
    n "You know,{w=0.25} I think he's trying,{w=0.25} too. {w=0.25}He may not show it,{w=0.25} but-"
    #ed bursts in with a TV and gabriel with a gamecube
    g "Guess who's back from the liiiiiibraryyyyy!"
    n "...you went out in your pajamas?"
    g "Quiet,{w=0.25} you."
    g "Someone told me you were hiding in your bed playing a game,{w=0.25} Piapia."
    g "And I thought,{w=0.25} \'Why don't we all play together?\""
    g "So I went out and brought home some party games."
    g "And I brought your sister from downstairs."
    "Orion doesn't say anything."
    n "Hey,{w=0.25} I didn't know you could check out video games from the library!"
    n "This is a game-changer!{w=0.25} Oh-{w=0.25} pardon the pun..."
    e "Nah,{w=0.25} I'm in a good mood."
    #cg controller
    e "Yo,{w=0.25} Cassiopeia."
    e "Get on the game." #he's smiling.
    
    return


#ending
label theguy:
    #if the phone is on screen hide the phone
    c "I got the guy."
    n "You got the guy?" #Speaker depends on who's on screen right now. 
    c "I got the guy! {w=0.25}Oh my god,{w=0.25} I got the guy!"
    #persistent variable is commented out for testing other routes.
    #$ persistent.got_the_guy = True
    return

#alternate intro
label postguy:
    "It's a lazy Saturday at the Spelltower,{w=0.25} and Cassiopeia is nowhere to be found."
    "Last week on Sunday,{w=0.25} when he tried to log in,{w=0.25} he got an error message saying the game needed to be updated."
    "He was sure his game was up-to-date,{w=0.25} but since he didn't know how to fix the error,{w=0.25} he had no choice but to set the game aside."
    "It made him realize how pointless it all was."
    "After all,{w=0.25} he wasn't even having fun."
    "Well,{w=0.25} he hasn't thought about that game for a while."
    "He's on a date with Niecy right now and he couldn't be happier."
    return

#test
label partone:
    
    "{i}When you see this icon,{w=0.25} dialogue will automatically proceed based on your preferences.{/i}"
    "{i}You can change the duration of Auto-Advance in the Preferences menu.{/i}"
    return


#test loop
label timerland:
    show screen timer
    show screen countdown
    show screen storefront
    while True:
        "This is a test of the storebuttons."
    return

#test loop
label theendlessloop:
    while True:
        #show screen phone
        show screen testphone2
        "Click the gacha button and mark the result."
        if guy_end:
            jump theguy
    return