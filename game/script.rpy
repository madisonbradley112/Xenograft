# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define puter_before = Character("???", window_background=Frame("images/textbox/green.png", 25, 25),  who_xpos=225, who_ypos=28, color="#FFF", what_color="#B14DE3") 
define puter = Character("Puter", window_background=Frame("images/textbox/green.png", 25, 25),  who_xpos=225, who_ypos=28, color="#FFF", what_color="#B14DE3")
define tunep_before = Character("???", window_background=Frame("images/textbox/orange.png", 25, 25),  who_xpos=200, who_ypos=28, color="#FFF")
define tunep = Character("Tunep", window_background=Frame("images/textbox/orange.png", 25, 25),  who_xpos=225, who_ypos=28, color="#FFF")
define jupiter = Character("Jupiter", color="#96FF3E", window_background=Frame("images/textbox/world.png"))
define neptune = Character("Neptune", color="#DC7D01", window_background=Frame("images/textbox/world.png"))
define jupiter_before = Character("???", color="#96FF3E", window_background=Frame("images/textbox/world.png"))
define neptune_before = Character("???", color="#DC7D01", window_background=Frame("images/textbox/world.png"))
define god = Character("God?")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 2.0
    scene black

    "You are exhausted.{p} It's been a looong day of work and uni, and you were laying in your bed, mentally preparing to do some schoolwork." 
    
    "You had a major assignment due tomorrow, and you've been putting it off for as long as you could manage."

    "Your strategy was to get it all done in one day, but you were just so tired... Maybe you could leave it all for the morning?"

    "It was due at 11:59pm tomorrow anyway, so you had some breathing room. At least, enough breathing room for a nap."

    "As you opened your phone to scroll TikTok, you felt your eyes get heavy, and you slipped away to sleep."

    "snnzzzz...{w=0.5} snzzzzzzzzzz,,, {w=1} szzznnnn... {w=0.5} snnnnz..."

    "You dreamt of a red and pink and blue world, nothing like you had ever seen before. The plants were unfamiliar to you - spiky and angular."

    "You looked around in your dream, and the sun was bright and blinding and... blue?"
    "As you looked up to the sky, the entire world washed out, with consuming indigo light."

    "And then you woke."

    define wake_up = Fade(0.0, 0.0, 4)
    play music "alien-techno.mp3" fadein 2.0 volume 0.5
    scene bg with wake_up
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "You looked around you at the mustard yellow ground and the pink sky. Your head hurt with the contrast, and everything was terribly vibrant."

    "Every plant here was strange and wide and blocky, with the trees having thick, triangular trunks, and the grass turned into squishy-looking fungal growths."

    "Or... at least you thought those were trees and grass. You looked up to the sky, and saw the blue sun from your dream - blaring and radiant."

    "And next to it, there were two moons. The longer you looked at them, the more you realized they were slowly moving around each other."

    "You immediately moved your hands to pinch yourself to see if you were still dreaming, only to notice - you had no thumbs."

    "in fact, you had no fingers at all - and as you looked down at your hands, you screamed - they were replaced with green stubby limbs."

    show puter scared
    with dissolve

    puter_before "AAAAUGHHHHHHHHHHHHHHHH!!!!"

    puter_before "(What the fuck??!! What am I?? Where am I? Am I still dreaming?)"
    puter_before "(What happened to me?? My body - this isn't me!)"

    show tunep annoyed
    with dissolve

    tunep_before "Glarp... no need to sizzle a flox so loudly, pan..."

    puter_before "What am I?! Who are you?! Where are we???"

    tunep_before "Aye... get your gneebles gneebled, pan..."
    tunep_before "Get your plorps collected in a box - you're waking the swipples."

    puter_before "Again... Who are you?!"
    tunep_before "No jokes, pan... I'm your plinko, remember? Your plinko Tunep?"

    show puter stressed
    puter_before "...Tunep? My pwinko?"

    show tunep peeved
    tunep "We stopped being pwinkos one sunspin ago when we became plinkos!! Do you think you're being funny? A real flarp-slapper?"

    show puter embarrassed
    puter_before "Aye - I misspoke, okay... My plinko Tunep... of course."
    show tunep baffled
    show puter stressed
    puter_before "Just - just to make sure I haven't lost it, can you tell me my name?" 

    tunep "Lost what?"

    puter_before "Ah - nothing - just, what's my name please?"

    tunep "You're my plinko Puter... as you have been since getting that name at our enplinkening. Is everything coco?"

    puter "Ahh.. yes thank you... everything's 'coco', I guess."

    puter "Just..."

    puter "Just... how did I get here?"

    tunep "We walked?"

    puter "I... guess so. Tell me..."

    label ordering:
    menu:
        tunep "Hm?"

        "Have... you ever heard of Earth?":
            jump earth

        "Do you know about humans?":
            jump humans

    label earth:
        show tunep base
        tunep "Ea-urth...?"

        tunep "What is ea-urth?"

        show tunep bored
        tunep "Sounds like a new type of gneeble... is it one?"

        menu:
            "Eh... sure - it's a new gneeble.":
                show tunep peeved
                tunep "Ehhh... strange. You'd really think they'd have stopped making those. Didn't I say you should stop paying attention to those?"
                show puter stupid
                puter "Eh....?"

            "Ahhh.. nah.. it's a new plorbus.":
                show tunep freaky
                tunep "Ah - Puter - shh!! We're in public! What if someone heard that??"
                show puter embarrassed 
                puter "OOPS!! I'm sorry - I didn't mean to..."
                show tunep wistful
                tunep "It's coco... just wait until we're home then we can talk about it!" 
                show puter stupid 
                puter "Eh....?"

        jump us

    label humans:
        show tunep base
        tunep "Hewmans?"

        tunep "What's a hew? What's a man?"

        tunep "Do they have those at Glamby's?"

        menu:
            "Ah... yeah! They've got a few at Glamby's.":
                show tunep peeved
                tunep "Hm... I don't quite know what I expected. They seem to have just anything at Glamby's these days..."

            "Ahhh.. nah... they're a type of creature.":
                show tunep peeved
                tunep "Hey!! You know I'm scared of chrechers!! What are you trying to do?" 
                show puter crying 
                puter "Hey - oh shoot - I'm sorry - I forgot... I didn't mean to remind you!"
        jump us

    label us:
        show puter angel

        puter "Anyway... enough about that, it's not important. "

        show tunep base
        puter "I'm feeling like I want to reminisce... can you remind me about us?"

        show tunep wistful
        tunep "Us...?"

        tunep "Well, when I met you back in Tweeble eight sunspins ago, I worked at Blamper's. You were up there at the drinksdesk."

        tunep "I saw you and I found you incredibly blarpy..."

        tunep "I suppose you felt the same, as you bought me a Pink Glorble. You didn't know this... but those were my favourite."

        tunep "And... since then, it's been history. Eight sunspins of us. We went from pwinkos to plinkos last sunspin, after our enplinkening."

        tunep "That's when we got our new names - yours Puter, mine Tunep."

        puter "Ah... Thank you for reminding me. Let's cheer to eight sunspins... of us. And many more. "

        show puter stressed
        puter "(Dang... I think Tunep might be the alien spouse of the owner of this body - Puter.)" 
        puter "(This gives me a bit of pressure... Tunep doesn't know their spouse has been replaced with a person.)" 
        puter "(I don't want to hurt Tunep's feelings or make Puter seem weird or rude... so I guess I have to try my hardest to fit in.)"
        puter "(Of course - this only matters so long as I end up getting my real body back in the end.)"
        show puter handsome
        puter "(Here's to alien-hood - let's hope I don't screw it up. I'll keep looking into what's up with this body-swap in the meantime.)"
        stop music fadeout 2.0 

        "Meanwhile, on a different world, across the universe... two people are talking in a park. Or, at least one of them *looks* like a person."
        play music "normal-techno.mp3" fadein 2.0 volume 0.3
        show bg_2 
        show neptune base
        show jupiter base
        show hand wave
        with fade

        neptune_before "So... tell me more about your new earrings and hair clips - they're cute. Where did you get them?"

        jupiter_before "Ehhh - thank gneep! They were a gift from Tunep! Although... I've never worn them before today."

        show neptune hyrax
        neptune_before "...What was that?"

        show jupiter weary
        jupiter_before "...a gift from Tunep?"

        neptune_before "No... did you just say 'thank gneep'?"

        show jupiter embarrassed
        jupiter_before "AH! Sorry, sorry, I meant 'thank you'! Force of habit of course. "

        show neptune tired
        
        neptune_before "*sigh*{p}You're cute sometimes, you know that?"
        
        show jupiter cute

        jupiter_before "Ah.... thank you!? "

        show hand point
        show jupiter weary

        jupiter_before "I'll have you know though, I'm kindly taken by my lovely partner since eight sunspins ago! Puter and Tunep, our recent anniversary!"

        show neptune base

        neptune_before "Ahahahahaha - enough with the jokes babe."

        show hand wave
        show jupiter scared

        jupiter_before "Wha?!?!"

        neptune_before "Besides, what's with the pig latin? I thought 'Jupiter' becomes Upiterjay and 'Neptune' becomes 'Eptunenay'? Not 'Puter' and 'Tunep'."
        neptune "Ahah, anyways - I know our eight year anniversary was only a week ago - seems like it's only been a year, hasn't it?"

        show jupiter weary
        jupiter "(Oh gleebus... First I get transported into some weird alien body, no Tunep to be found...)"
        jupiter "(Then, a complete alien version of Tunep appears in front of my eyes??!)"
        jupiter "(I guess I gotta plork the pleebus...)"

        menu:
            "Ah! Yeah, it feels like it's only been one tenth of a sunspin!":
                show neptune annoyed
                neptune "Ah... well I don't know if I'd go that far."
                show neptune base
                neptune "Let's just say it feels just right."
                neptune "No more, no less - it's perfect where it's at."

            "Oh - no, it's felt like at least 20 sunspins!":
                show neptune uncomfortable
                neptune "Hey!! What is that supposed to mean??" 
                show jupiter embarrassed 
                jupiter "Hey - wuh?"
                neptune "Do you realize how that sounds?"
                jupiter "Whatdya mean?"
                show neptune tired
                neptune "*sigh* - it's all good. Let's just say that it feels like just the right amount of time, including the rest of the future."

        neptune "Anyways - what got into you, calling years 'sunspins' now?"
        neptune "Is this some sort of TikTok prank where you replace one word with something random and see how your partner reacts?"

        menu:
            "Oh - no, it's my new ...synonym... I learnt it from the... broadcasts?":
                show neptune base
                neptune "The... broadcasts...?{w} You're ridiculous sometimes, I love it. You're lucky you're so cute."
                show jupiter handsome
                neptune "Ahaha... ahah... thank you Tunep-like!"
                show neptune tired
                neptune "Still, with the janky pig latin?"

            "Ah! It's just how the word should be used... It just makes sense!":
                show neptune base
                neptune "Sure - sure. Eight sunspins of us, I suppose. You're funny." 
                show jupiter weary 
                jupiter "Ah... thanks?"
                show neptune tired
                neptune "*sigh* You'll have to let me know where you heard that from, when we get home from our walk."

        stop music fadeout 2.0 
        "Suddenly, a bright light appears from the heavens."
        show white with dissolve
        "It was as if your soul was being ripped out of your body (or, at least the body you inhabited.)"
        "You heard an incredible voice booming from above, echoing through your entire being."
        "Or, at least, you thought of it as above? It reverberated throughout the wisps of your soul."
        "Was this God? Did you die?"
        play music "choir.mp3" fadein 2.0 volume 0.3

        god "{bt=5}Aw fuck.{/bt}"
        god "{bt=5}I got a couple of 'em mixed up again.{/bt}"
        god "{bt=5}This shit's a bit hard.{/bt}"
        god "{bt=5}Keeping track of everyone's souls, all at once, all across the universe...{/bt}"
        god "{bt=5}You'd think they'd have found a better way to do it.{/bt}"
        god "{bt=5}Instead, I'm just focusin' real hard {p} every goddamn moment {w} so that everything stays put.{/bt}"
        god "{bt=5}Puttin' a lot of trust in the old guy's concentration here... {p} Got one of the lackeys to take care of it for me once.{/bt}"
        god "{bt=5}Pretty sure everyone on the universe knew how that one turned out. {p} The old universe died {w} and a new one came in with a big *bang*!{/bt}"
        god "{bt=5}Stopped me from trustin' anyone anymore. {p} So now it's just 'lil ol' me {w} trying to keep my memory intact.{/bt}"
        god "{bt=5}Anyways. You'll have to forgive me, Puter and Jupiter. {p} Real easy to get both of ya mixed up when you two are so similar.{/bt}"
        god "{bt=5}Who knew there'd be two little weird freaks out there {p} with nearly the same names, personalities, and partners? {/bt}"

        puter "Hey!! What the gleep is that supposed to mean?"
        jupiter "Weird little freaks?!!"

        god "{bt=5}Bahahah... knew that'd rile you two up. {w} You'll keep a secret for me, will ya?{/bt}"
        god "{bt=5}The whole 'we're not alone in this universe' sort of freakout {p} was supposed to happen a couple millenia in the future.{/bt}"
        god "{bt=5}You're lucky I didn't smite ya on the spot - {p} you know the amount of trust that takes, {p} to let you two run amok with that info?!{/bt}"
        god "{bt=5}But I guess it's my bad, {w} so it'd not be *too* fair {p} to let you two get evaporated just to hold up my reputation.{/bt}"
        god "{bt=5}You're free to go. {w} Just don't say anything {p} or you'll be turned into powder {p} so fine that the Devil couldn't snort it.{/bt}"
        god "{bt=5}Seeya!{/bt}"

        hide white
        hide jupiter
        hide neptune
        hide hand
        hide bg_2
        show bg 
        show puter shocked
        show tunep base
        with dissolve

        puter "WHAT THE GLEEP???"
        show tunep baffled
        tunep "???!"
        show puter appalled
        puter "The gnarp is going on today?!"
        show tunep peeved
        tunep "Ah? What the plarp's up with you??"
        show puter stressed
        puter "...Nothing gleebable, I guess."

        "Meanwhile..."

        show bg_2
        show jupiter nonalien1
        show hand wave
        show neptune base
        with dissolve

        jupiter "WHAT THE FUCK???"
        show neptune uncomfortable 
        neptune "Everything okay??"
        show jupiter nonalien2
        jupiter "The fuck is going on today?!"
        neptune "What's up with you??"
        jupiter "Nothing important, I guess."
        centered "{size=+75}{cps=8}And that's that.{/cps}{/size}{p=5.0}{nw}"
        stop music fadeout 2.0 
        centered "{size=+75}{cps=8}The End.{/cps}{/size}{p=5.0}{nw}"
    return
