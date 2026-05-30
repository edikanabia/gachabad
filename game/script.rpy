# The script of the game goes in this file.

# The game starts here.

label start:
    #scene cg ceiling
    scene bg black
    #show screen testphone2
    #jump scammer
    #show screen gachadebug
    #jump theendlessloop
    jump givemeyourphone
    if persistent.got_the_guy:
        jump postguy
    else:
        pass
    #$ greenout.lines_until = renpy.random.randint(0,3)
    #$ spontaneous_handler.add_spontaneous(greenout)
    
    #show screen repeatthat
    #show screen testphone2
    $ story_index = -1
    #call quieres #testing the weed mechanic
    #call screen tutorialize
    "It's a lazy Saturday at the Spelltower,{w=0.25} and everyone is cooped up indoors..." 
    "Especially Cassiopeia.{w=0.25} Cassiopeia has been enamored with a new game he downloaded onto his new phone just last week!"
    "It's called...{w=0.25} um...{w=0.25} Well,{w=0.25} he can't remember what it's called.{w=0.25} But he's absolutely hooked!"
    $ story_index = 0
    #$ preferences.afm_enable = True #we can use renpy code to enable auto-forward in the script.
    "The day he downloaded it,{w=0.25} he showed it to Gabriel in a euphoric frenzy."
    "But Gabriel,{w=0.25} in typical Gabriel fashion,{w=0.25} took one look at it and called him a moron."
    "So now he has to play it under the covers,{w=0.25} where no one can see his shame."

    "The guy Cassiopeia wants is in the time-limited banner today.{w=0.25} It's the last opportunity to get him before the next season starts—tomorrow!"
    "It would be a good time to try for the guy during some downtime."
    #call screen banner
    #the first roll will always fail

    #hide screen banner

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
        "Get out of bed and greet your beautiful girlfriend":
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
            $ persistent.true_reset_visible = True #move this to the other endings when building
            return
        "Say it's porn to chase her off" if persistent.girlfriend_flag:
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
    show screen testphone 
    n "Okay...{nw=1.0}"
    n "Um,{w=0.25} how long is that gonna take?"
    $ story_index = 1
    menu:
        "Uhhh...":
            $ story_index = 0
            c "Until I get the guy I want?"
            n "Well...{w=0.25} I don't want to be dismissive,{w=0.25} but...{w=0.25} can it wait?"
            c "No,{w=0.25} the season ends today."
            n "Okay,{w=0.25} then,{w=0.25} I'll wait for you,{w=0.25} but while you do that..."

    label .phonereturn1:
        $ story_index = 0
    n "...we definitely need to talk."

    #end of intro.
    return

#storypath
label niecyroute:
    show bg room cassiopeia with dissolve
    show niecy with dissolve
    
    n "So,{w=0.25} like,{w=0.25} you've been spending a lot of time playing this game,{w=0.25} right?"

    return


#storypath
label gabrielroute:
    g "So!{w=0.25} Tell me,{w=0.25} what is this game?{w=0.25} What's it about?"
    # idea: nested menu options that if they time out gabriel will say something different. mechanic change: we're just gonna make a choice menu timer time out thing
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
    
    menu:
        "About":
            pass
    
    
    label .ignore1:
        g "If you can't tell me,{w=0.25} there's no reason for you to keep playing it."
    
    #join in here at gabriel2
    g "Piapia,{w=0.25} I gave you that card because I wanted you to be able to practice some autonomy." #if you spent money these show
    g "You've been so responsible with it up until now.{w=0.25} What happened?"
    menu:
        "Nothing":
            pass
    c 'Nothing "happened," Gabriel.{w=0.25} I\'m fine.'
    g "But you're not fine,{w=0.25} Piapia. {w=0.25}You're ignoring Niecy."
    g "You came into my room and you told me, {w=0.25}\"I love this woman,{w=0.25} Gabriel.\"{w=0.25} Is that not what you did?"
    g "You told me she was the love of your life."


    g "Just how much money did you spend on this thing,{w=0.25} anyway...?"
    if money_spent > 300:
        g "JESUS CHRIST-"
        g "[money_spent] DOLLARS!?"
        jump givemeyourphone

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
    e "{size=*0.85}(He's right,{w=0.25} but...){/size}"
    e "Listen,{w=0.25} you didn't find any of that suspicious?"
    c "Well,{w=0.25} you definitely didn't look as hot as you do now,{w=0.25} but...{nw=0.5}"
    e "{size=*0.85}I didn't look what now?{/size}{nw=0.5}"
    c "I don't know,{w=0.25} I wanted to talk to you."
    c "...I thought you changed."
    e "Change takes a lot longer than a week when you're as old as I am."
    c "You keep saying that. {w=0.25}You don't look a day older than 30."
    e "So I've been told." #smug
    e "But I'm sure last week I was the same as ever.{w=0.25} Because I don't remember a lick of this."
    c "What!?{w=0.25} But that's..."
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
                                    "She shuffles into bed with him."
                                    n "This is nice, {w=0.25}isn't it?"
                                    #show screen banner with Dissolve(5.0)
                                    "Niecy presses her head into the crook of his neck."
                                    "..."
                                    "..."
                                    n "...you're warm."
                                    "..."
                                    "..."
                                    "..."
                                    #hide screen phone with None

                                    n "Wow!{w=0.25} {size=*0.75}Oh wow...{/size}"
                                    n "Well!{w=0.25} Here I go!"
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
                                            n "Good answer,{w=0.25} sweet pea.{w=0.25} Now,{w=0.25} c'mere!"
                                            "For the rest of the afternoon,{w=0.25} Cassiopeia forgot all about the guy that he wanted..."
                                            return
                                        "My goddamn telephone":

                                            show cg covers 0 with Dissolve(0.2)
                                            n "Huh."
                                            n "Can we talk about it?"
                                            "Cassiopeia shrinks into his bed."
                                            n "No?"
                                            c "We can!{w=0.25} I just...{w=0.25} I don't...{w=0.25} I don't know what I was thinking.{w=0.25} I don't know why I said that."
                                            n "I don't either.{w=0.25} I was really hoping you would pick me. {w=0.25}Your girlfriend."
                                            c "I'm sorry...{w=0.25} I'm sorry.{w=0.25} Can I make this right?"
                                            n "You can...{w=0.25} As a matter of fact,{w=0.25} you should..."
                                            c "Um.{w=0.25} You're more important.{w=0.25} I love you."
                                            return

                            pass
                        "Okay fine I'm on my stupid phone":
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
    n "Cassiopeia, {w=0.25}are you serious right now? {w=0.25}You can't get off your phone long enough to just cuddle with me?"
    c "No! {w=0.25}I can't!{w=0.25} I can't even stop thinking about it!"
    c "I...{w=0.25} I don't even think I like playing it all that much,{w=0.25} but when I don't play it and get the rewards,{w=0.25} I get all itchy!{w=0.25} I don't know why..."
    
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
    $ spontaneous_handler.add_spontaneous(greenout)
    "Nothing happened..."
    return

#event ed
label quieres:
    #show ed
    e "Yo."
    n "What's up?"
    e "Anyone else see a demon prowling around?{w=0.25} I thought I saw one go into the break room."
    n "Maybe it's because you took the Edible That Makes You See Demons and Forget You Took the Edible That Makes You See Demons?"
    e "Oh yeah...{w=0.25} That's probably one of my best inventions."
    n "It's not even close to your top 75."
    e "Everyone's a critic." #ed annoyed
    e "Yo C-man,{w=0.25} you want one?"
    $ story_index = 4
    menu:
        "Sure":
            pass
        "What did you call me":
            pass
    $ has_gummy = True
    show cutin gummy1 with dissolve:
        align (0.2, 0.4)
    pause 1.0
    show maskedcutin as cutin2 with dissolve

    label .ignore:
        e "See ya."
    hide cutin with dissolve
    hide cutin2 with dissolve

    if has_gummy:
        c "So...{w=0.25} what happens if I take this?"
        n "Don't eat that."
        show screen deliciousgummy
    return

#event gabriel
label gabriel1:
    n "Hello? {nw=0.5}"
    n "Hey,{w=0.25} Gabriel!{w=0.25} How was your nap?"
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
        if niecy_irritation > 3:
            g "No,{w=0.25} you look genuinely irritated already. {w=0.25}You aren't typically like that with him."
            n "I know, {w=0.25}but I have to try..."
            g "Sweetheart. {w=0.25}Let me talk to him. {w=0.25}I'll straighten him out."
            n "Oh... {w=0.25}okay..."
            jump gabrielroute
        else:
            g "Are you sure,{w=0.25} sweetheart?"
            n "Positive."
            g "All right,{w=0.25} I'll leave you to it...{w=0.25} but Cassiopeia?"
            #stop spending my money on gacha games. cg and sound.       

    return

label gabriel2:
    show gabriel annoyed
    g "Cassiopeia!{w=0.25} I can see you spending decent money on this thing instead of an afternoon out!"
    $ story_index = 5
    g "Surely,{w=0.25} this game can't be more important than your girlfriend."
    $ found_gf_flag = True
    menu:
        "It isn't":
            pass
    c "I'm not ignoring her!"
    g "Then why are you tap tap tapping when she's standing right in front of you!?"
    g "Don't make me come in here again!"
    return

#event gabriel
label gabriel3:
    #play sound door slamming open
    show gabriel rage
    jump givemeyourphone
    return

#event ending
label instakill:
    #if music is playing stop music
    #show cg instakill
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
    
    jump scammer
    return

#ending
label gavephone:
    #show the give phone cgs
    g "Good."
    g "You can have this back in a week."
    "Gabriel sighs."
    g "I hate to patronize like this,{w=0.25} but..."
    g "Piapia.{w=0.25} You know I love you. {w=0.25}But you understand,{w=0.25} this is wrong,{w=0.25} right?"
    c "...I don't think it's wrong to play a game."
    "Gabriel groans,{w=0.25} realizing he has no way to make Cassiopeia understand his perspective."
    g "Well,{w=0.25} give it a week and you'll forget all about it. {w=0.25}OK?"
    c "..." #pouting
    g "{i}OK?{/i}"
    c "OK..."
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
        show screen phone
        show screen testphone2
        "Click the gacha button and mark the result."
        if guy_end:
            jump theguy
    return