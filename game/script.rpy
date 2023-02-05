# The script of the game goes in this file.
# The game starts here.

label start:

    #Stops main menu music with a fade
    $renpy.music.stop(fadeout = 1.0)

    #Define Names
    $ mi_name = "???"
    $ hl_name = "???"
    $ an_name = "???"

    $ chatty_name = "Chatty Lady"
    $ nosy_name = "Nosy Gaudy Lady"
    $ unremark_name = "Unremarkable Lady"
    $ redhead_name = "Redheaded Lady"

    # Define scores
    $ mi_score = 0
    $ hl_score = 0
    $ an_score = 0

    $ seenAnnabelle = False

    call intro

    return

label intro:
    scene bg room with dissolve
    play music "audio/music/opening_song.mp3" fadein 2.0
    "The morning sun shines in through the blinds in your bedroom window, as it does every morning."
    "It feels a little lonely..."
    "But you've gotten used to that."
    "As you get up and make your bed, you think about your plans for the day."
    "First things first, making yourself a cup of coffee."
    "Then, choosing some clothes that make you happy, and taking a nice warm shower."
    "A warm shower is always a nice start to the day."
    "Breakfast. You have some fiber cereal left, but the sugar-free vanilla yogurt might be a better choice today."
    "Its expiration date is soon."
    "And there's some fresh peaches you left out on the counter to ripen. You could have those too."
    "You start the coffee maker and head back into your bedroom to pick out some clothes."

    if(playerGender == "Male"):
        $ outfit = "green and brown cardigan with a pattern of happy ducks eating bread"
    else:
        $ outfit = "tan cardigan with a pattern of tessellated strawberries"

    "As you open the dresser drawer, you see a [outfit] sitting right on top."
    "You pull out the cardigan and look at it wistfully..."
    "...this was your lifelong partner's favorite."
    "The two of you had lived in this apartment at Sunny Palms Retirement Home for several years, before they passed away from illness a few years ago."
    "You mostly have spent time in your room since then, reluctant to meet new people."
    "After all, your partner meant so much to you. You wouldn't want to rush yourself."
    "But you've decided today's the day."
    "Even if you don't meet anyone new, you're at least going to go out there and be around people more."
    "You don't expect to meet anyone new right away anyway..."
    "...but who knows what will happen?"
    "The coffee maker must have finished warming up. You can smell fresh coffee even from here."
    "You head off for your shower, optimistic about what might happen today."
    "You hope it will be a nice afternoon out."
    "After breakfast, you slip on your orthopedic shoes and head out of your room, to the main area of Sunny Palms."

    call chooseRoute

    return

label chooseRoute:
    menu:
        tut "Where would you like to go?"

        "Crafts Room":
            call craftsRoom
        "Game Room":
            call gameRoom
        "Communal Lounge" if seenAnnabelle == False:
            call communalLounge

    return

label craftsRoom:
    scene bg crafts with dissolve
    play music "audio/music/miriam_theme.mp3" fadein 2.0
    "You decide to head to the crafts room."
    "It's a nice cozy space, with cubbies and bins of various craft supplies."
    "There's plenty of yarn, thread, paint, paper, clay, pencils - whatever aspiring arts-and-crafters might want."
    "A couple ladies are sitting in rocking chairs, gossiping while they crochet garish lap blankets."
    "You sit at the puzzle table for now."
    "It has a green felt top, to keep puzzles from breaking apart."
    show miriam at center
    "A short, blonde lady in a long red cardigan is sitting here, too, very intently doing a puzzle."
    "The box lid is nearby."
    "The puzzle picture is of Botticelli's “The Birth of Venus”, but all the people have been replaced with cats."
    "It's a 1000 piece puzzle..."
    "...you don't think you'd have the patience for that."
    mc "That's a cute puzzle."
    mi "Oh, thank you! One of my grandchildren gave it to me for Christmas."
    mi "She's such a dear..."
    mc "How old is she?"
    mi "Oh, she's eight."
    mi "She just loves finding new pretty pieces of art!"
    mi "So, I take her to the art museum every now and again."
    mc "That's cute."
    $ mi_emotion = 'happy'
    show miriam at center
    mi "Isn't it just?"

    $ mi_emotion = 'neutral'
    show miriam at center
    menu:
        mi "Do you have any grandchildren?"
        "Yes.":
            $ mi_emotion = 'happy'
            show miriam at center
            mi "Oh, how darling!"
            mi "I hope you get to see them as often as their little hearts desire."
            $ mi_score += 1
        "No.":
            mi "Oh, that's a shame."
            mi "I think every elderly person deserves grandchildren to dote on."

    $ mi_emotion = 'happy'
    show miriam at center
    "She smiles brightly at you."
    $ mi_name = "Miriam"
    mi "I'm Miriam. Have I seen you around before?"
    mc "I'm [playerName]. I haven't been very social lately."
    mi "Well, you've come to just the right place, [playerName]!"
    $ mi_emotion = 'neutral'
    show miriam at center

    menu:
        mi "Would you like to help me put this puzzle together?"
        "That sounds nice.":
            $ helping = True
            $ mi_emotion = 'happy'
            show miriam at center
            mi "You're so sweet. Thank you!"
            hide miriam
            "You do your best to help Miriam with the puzzle, matching pieces that look like they might go together."

        "No, thank you, but I'd love to keep you company.":
            $ helping = False
            "Miriam lowers her voice."
            mi "That's lovely of you."
            mi "See, I come here every morning to work on this puzzle, and those two old biddies in the corner are always there gossiping!"
            mi "I don't think their blankets will ever be done!"
            hide miriam
            "You're not sure you'd be much help with the puzzle, so you're okay with watching instead."


    $ mi_emotion = 'neutral'
    show miriam at center
    mi "So, do you have any hobbies?"
    if(helping):
        mi "Besides helping little old ladies do their silly kittycat puzzles, of course."
    else:
        mi "Besides watching little old ladies do their silly kittycat puzzles, of course."

    if(playerGender == "Male"):
        menu:
            "Bird Watching":
                mi "That sounds sweet."
                mi "Do you have a little Audubon's field guide that you take with you?"
                mi "And a little pair of binoculars?"
                mc "I do. They're very well-loved."
                $ mi_score += 1
            "Dirt Polishing":
                mi "Oh, my. I didn't realize that was a hobby."
                mi "Is that hard work?"
                mc "Oh, yes. I started getting worried about muscle strain."
                "Miriam winks at you."
                mi "Better to save those muscles for other things, right?"
                $ mi_score -= 1
            "Soap Carving":
                mi "Is that anything like wood carving?"
                mi "With all the special little knives?"
                mc "No, you don't need anything fancy."
                mc "In fact, it's safer with blunter tools"
                mi "Maybe my little grandson would be interested in trying that."
    else:
        menu:
            "Gardening":
                mi "My sister had the most beautiful garden."
                mi "Did you know there's a community garden here?"
                mc "I did."
                mc "Maybe I should go out there and dig in the dirt again, like I used to."
                $ mi_emotion = 'happy'
                show miriam at center
                mi "Borrow their gardening tools! And make sure to take plenty of breaks."
                mi "Don't overexert yourself."
                "Miriam winks at you."
                $ mi_emotion = 'neutral'
                show miriam at center
                $ mi_score += 1
            "Watercolor Painting":
                mi "Oh, that sounds lovely."
                mi "I bet your watercolors are very pretty."
                mc "Thank you."
            "Taxidermy":
                mi "What an...odd hobby."
                mi "Aren't all those chemicals bad for you?"
                mc "Well, yes."
                mc "I stopped doing it myself years ago, but I still have a collection."
                mi "Well, er..."
                $ mi_score -= 1

    mi "I used to knit like a wild woman in my younger years."
    menu:
        mi "The arthritis in my wrists is too poor for it now."
        "Did you knit that sweater you're wearing?":
            "Miriam perks up at your question."
            $ mi_emotion = 'happy'
            show miriam at center
            mi "Why, yes, I did!"
            mi "It's my favorite color: cherry pie red."
            mi "I just love cherry pie."
            $ mi_emotion = 'neutral'
            $ mi_score += 1
        "That's very unfortunate.":
            mc "I have arthritis in my knee."
            mc " I can't walk long distances anymore, like that one song with the Scottish singers."
            mi "..."
            "Miriam doesn't seem to understand your reference."
            $ mi_score -= 1

    hide miriam
    "The two of you sit quietly for a little while longer."
    if(helping):
        "You're doing well putting together the shell the Venus cat stands on."
        "Although, you wish you had attached it to the rest of the puzzle border and not the other way around."
    else:
        "You wonder if she will end up framing this puzzle on the wall."
        "Her granddaughter has good taste."

    show miriam at center
    mi "Tell me, [playerName]."
    menu:
        mi "Do you like cats?"
        "Yes, I do.":
            $ mi_emotion = 'happy'
            show miriam at center
            mi "Oh, wonderful! I just adore them."
            mi "They are the cutest, silliest little things."
            mi "I have three I brought here with me. They're sleeping in my room."
            $ mi_emotion = 'neutral'
            $ mi_score += 1
        "No, I prefer dogs.":
            mc "Unfortunately, I've never owned cats."
            mc "I have a King Charles Spaniel I brought with me named Daisy."
            "Miriam tuts. It seems like she disapproves."
            mi "I much prefer the independence of kittycats, but to each their own."
            mi "Dogs can be sweet in...in their own way."
            $ mi_score -= 1

    hide miriam
    "Suddenly, a soft chime sounds in the room."
    "It's the bell marking the top of the hour."
    show miriam at center
    mi "Oh, goodness! I really must be going."
    mi "I just stepped out for a little bit while my pie was baking."
    mi "Would you like to come over for a little visit, dear?"
    mi "I'm sure we'd both be glad for the company."
    mc "That sounds nice. I'd love to."
    hide miriam

    scene bg apartment with dissolve
    "You walk back to Miriam's room with her."
    "She walks a lot faster than you, but doesn't seem to mind slowing down to keep up with your bad knee."
    "Miriam's apartment is full of rounded, comfortable furniture."
    "There's a colorful afghan over the back of every living room chair."
    "Three cats swarm around your feet as the two of you enter."
    "One of them rubs itself against your shins while another sniffs you."
    show miriam at center
    mi "Don't mind Rufus, he's just a little nosy."
    mi "And Blanche is such a love, isn't she?"

    #Determine the ending
    if(mi_score > 0):
        call miriam_good
    elif (mi_score < 0):
        call miriam_bad
    #Call a random ending if the score is 0
    else:
        $ chooseEnding = renpy.random.randint(1,2)
        if(chooseEnding == 1):
            call miriam_good
        else:
            call miriam_bad

    return

label miriam_good:
    "She backs away from you for a second, leaving you in the crowd of cats."
    mi "I'll be right back, dear."
    hide miriam
    "She shuffles away towards what must be her bedroom."
    "You pet her cats while she's out of the room. Blanche in particular seems to like you a lot."
    "You suddenly hear the oven timer go off. The pie must be done."
    play sound "audio/sfx/oven_ding.wav"
    "Before you go check on it, you hear a door swing open."
    "Miriam comes out wearing a particularly...odd outfit."
    stop music
    mi "Meow."
    "Is that...a lingerie tabby cat fursuit?"

    scene black with dissolve
    tut "Miriam: Good Ending"
    return

label miriam_bad:
    hide miriam
    "Rufus yowls and hisses at you, putting his paw on your shins."
    "Even the other cat seems very aloof."
    show miriam at center
    mi "Oh, my! He doesn't act like that towards anybody."
    "The last thing you remember is a loud screech and a very painful sharp sensation."
    hide miriam
    stop music
    play sound "audio/sfx/cat_screech.wav"
    scene black with dissolve
    "."
    ".."
    "..."
    "You wake up some time later...in a hospital room?"
    "There's a card on the bedside table."
    "{i}Dear [playerName],{/i}"
    "{i}I'm dreadfully sorry about your little visit. You really are sweet.{/i}"
    "{i}Unfortunately Rufus told me you weren't to be trusted.{/i}"
    "{i}I trust my cats more than anyone.{/i}"
    "{i}I'm sorry.{/i}"
    "{i}- With Love, Miriam.{/i}"
    tut "Miriam: Bad Ending"
    return

label gameRoom:
    scene bg game with dissolve
    play music "audio/music/helen_theme.mp3" fadein 2.0
    "You decide to head to the games room."
    "It's a larger-sized room with some moderate décor, a few square wooden tables, and even a pool table."
    "You head over to a white cabinet with glass doors near the entrance."
    "The cabinet is filled with various board games, packs of playing cards, poker chip sets, and..."
    "...a Sexy Senior Citizen Edition of {i}Monopoly{/i}?"
    "Weird."
    "Pulling your attention from the odd board game, you notice that the only people here right now are a group of three ladies playing what looks like mahjong."
    "One of the ladies at the table, wearing a fuzzy and quite gaudy teal sweater notices you."
    nosy "Hello there. Would you like to join in?"
    "You don't know shit about mahjong."
    mc "That sounds fun, but I don't know how to play."
    unremark "That's okay! Why don't you just sit and watch for a game?"
    $ hl_name = "Helen"
    unremark "If you sit next to Helen, I'm sure you'll pick it up in no time."
    nosy "Oh yes, when it comes to mahjong, there's no one better to learn from than Helen."
    nosy "She's very good."
    $ hl_emotion = 'snarky'
    show helen at center
    hl "Of course I'm good. I play to win."
    hide helen
    "Everyone giggles. It doesn't seem like she was joking."

    $ hl_emotion = 'neutral'
    show helen at center
    menu:
        hl "So what do you say? Will you join us?"
        "Sure, why not?":
            hl "Good good, now that's what I like to hear."
            hl "Come sit."
            hide helen
            "You walk your way to the table and take a seat."
            $ hl_score += 1
        "I don't know...":
            $ hl_emotion = 'smirk'
            show helen
            hl "What are you, a coward?"
            hl "Just come and sit down."
            mc "Y-yes ma'am."
            hide helen
            $ hl_emotion = 'neutral'
            "You shamefully waddle to your seat."
            $ hl_score -= 1

    "You sit and watch the ladies play mahjong for a while."
    "They're all very chatty, except the stone-cold Helen."
    "It seems like the point of the game is to pick up or discard the tiles so you have a certain number of matching sets."
    chatty "So, Helen, will you be sharing your ivory mahjong set with us any time soon?"
    nosy "Yes, yes, I'm sure it's exquisite."
    nosy "Didn't your husband buy it for you in Shanghai?"
    $ hl_emotion = 'snarky'
    show helen at center
    hl "{i}Ex{/i}-husband."
    hide helen
    $ hl_emotion = 'neutral'
    "The ladies titter with laughter. You're not sure what's funny."
    nosy "Oh, yes, yes, that's right."
    unremark "That set must be {i}quite{/i} an antique!"

    menu:
        "Do you collect a lot of antiques?":
            $ interest = "antiques"
            show helen at center
            hl "I do."
            chatty "Helen has quite a number of art pieces at home, don't you know?"
        "Where else have you visited?":
            $ interest = "travel"
            show helen at center
            hl "Oh, I could go on for {i}days{/i} about that."
            chatty "Oh, Helen's been to quite a few countries with that ex-husband of hers!"
            nosy "She's taken a number of trips to the Far East, hasn't she?"

    unremark "But out of anything, we know Helen has the best taste in classical music of all of us, though, don't we?"
    "The game continues for a little while longer."
    "As predicted, Helen wins the game."
    "She scoops up the little pile of coins in the middle of the table with a shit-eating grin."
    "The other ladies don't seem bothered that they lost, and cheerfully wave goodbye as they leave."
    nosy "So long, Helen! See you tomorrow!"
    "Helen begins to pack up the mahjong tiles."
    show helen at center
    hl "So, what's your name?"
    mc "My name is [playerName]-{nw}"
    hl "I didn't actually care."
    menu:
        hl "Do you enjoy classical music as well?"
        "Yes":
            hl "Really?"
            menu:
                hl "Do you prefer compositions from the Baroque or Romantic period?"
                "The Baroque Period":
                    hl "I enjoy the Baroque period very much myself."
                    hl "Though, rarely."
                    mc "They really were the masters of musical suites."
                    hl "Are you sure about that?"
                    $ hl_emotion = 'smirk'
                    show helen at center
                    hl "I can think of several others who were {i}much{/i} better."
                    $ hl_emotion = 'neutral'
                    show helen at center
                "The Romantic Period":
                    hl "That's more of an intellectual movement, isn't it?"
                    hl "I'm not as familiar."
                    mc "It is, but I think the Romantic period is so emotionally evocative, too."
                    mc "Like Camille Saint-Saens' work."
                    "It seems like the discussion has piqued Helen's interest."
                    $ hl_score += 1
            $ hl_score += 1
        "No":
            $ hl_emotion = 'disgust'
            show helen at center
            hl "Eugh, you have no taste."
            hl "That's quite a shame. I think classical music is so mentally enriching."
            mc "I prefer being able to visually admire art."
            $ hl_emotion = 'neutral'
            show helen at center
            if(interest == "antiques"):
                hl "I've traveled quite a bit."
                hl "Each art style from around the world is unique and admirable, wouldn't you say?"
            else:
                hl "I have quite a number of art pieces at home."
                hl "Perhaps you'd be interested to take a look"
            $ hl_score -= 1

    hide helen
    "You walk back to Helen's apartment with her, chatting about artistic expression."

    scene bg apartment with dissolve
    show helen at center
    hl "Minimalism is {i}such{/i} a silly fad."
    hl "All this new-age nonsense about projecting your own experiences onto the art."
    $ hl_emotion = 'snarky'
    show helen at center
    hl "I can hardly see what's so artistic about a stupid solid orange canvas."
    if(playerGender == "Male"):
        $ assumption = "soap carving"
    else:
        $ assumption = "macrame"
    hl "You look like the sort that would enjoy [assumption] or some such dull thing."
    $ hl_emotion = 'neutral'
    hide helen
    "Helen's apartment is full of polished, sophisticated furniture."
    "There's a china cabinet full of small decorative dishes."
    "It doesn't seem like they've been touched at all..."
    "Maybe these are art pieces, too."
    mc "Is that a pitcher plant?"
    show helen at center
    hl "What else does it look like, a {i}Rorschach blot{/i}?"
    "You've never seen a pitcher plant with pitchers that large."
    "Helen must take very good care of it."
    hl "While you're here, would you like a coffee, I guess?"
    mc "No, thank you. I had some this morning."
    hl "Suit yourself. It would certainly put some more pep in your step."
    hl "Or less wrinkles on your face."

    #Determine the ending
    if(hl_score > 0):
        call helen_good
    elif (hl_score < 0):
        call helen_bad
    #Call a random ending if the score is 0
    else:
        $ chooseEnding = renpy.random.randint(1,2)
        if(chooseEnding == 1):
            call helen_good
        else:
            call helen_bad
    return

label helen_good:
    hl "Did you say you liked works by Claude Debussy?"
    mc "I did, yes."
    mc "{i}'Afternoon of a Faun'{/i} is one of my favorites."
    hl "I happen to have a pair of tickets to the symphony orchestra."
    hl "Quite a number of his works are on the program."
    hl "...You'd have to wear something besides that cardigan, though."
    if(playerGender == "male"):
        $ outfitName = "ducks eating bread"
    else:
        $ outfitName = "strawberries"
    hl "What on earth is that pattern, {i}[outfitName]{/i}?"
    hl "Anywho, we could make a dinner reservation now, and..."
    hl "perhaps you'd be interested in a nightcap after the concert?"

    scene black with dissolve
    tut "Helen: Good Ending"
    return

label helen_bad:
    hide helen
    "You decide to sit with her even though you're not having coffee."
    "It's the polite thing to do."
    "As you walk into the kitchen, the hem of your cardigan catches on a small black figurehead bust."
    stop music
    "It falls off the endtable..."
    play sound "audio/sfx/bust_break.mp3"
    "...and onto the floor. And breaks."
    "Loudly."
    $ hl_emotion = 'disgust'
    show helen at center
    "Helen looks at you very judgmentally."
    "Before you can even speak up for yourself, she throws her coffee cup at you."
    play sound "audio/sfx/coffee_throw.mp3"
    "Luckily, she misses. Coffee and ceramic pieces go everywhere."
    hl "Do you know how much that cost?!"
    hl "You'd better be able to replace that!"
    mc "I'm so sorry!"
    mc "I'll do my best, I promise!"
    scene black with dissolve
    "You head home quickly to try and find this piece on the internet."
    "You're not very good at this whole 'internet' thing."
    "Eventually, you find an image of it on an auctioneer's website."
    "It's very rare. And very..."
    "...{i}very{/i} expensive."
    tut "Helen: Bad Ending"
    return

label communalLounge:
    scene bg lounge with dissolve
    play music "audio/music/annabelle_theme.mp3" fadein 2.0

    "You head to the communal lounge, where the magazine collections and the nice couches are. "
    "A group of three ladies in slinky dresses and heels are sitting by the fireplace, reading fashion magazines and laughing and gossiping."
    show annabelle at center
    an "Oh, I don't know what the fashion designers are up to these days."
    an "Give me a good Diane Von Furstenburg gown {i}any{/i} day of the week."
    hide annabelle
    redhead "At least the perfume samples still smell good."
    redhead "They have such depth nowadays."
    mc "Excuse me."
    mc "Um...did you know you're holding that magazine upside down?"
    show annabelle at center
    an "Oh, I knew that!"
    "She turns it right side up."
    "It's an issue of {i}VOGUE{/i} all about the outfits celebrities wore to the latest {i}Golden Globes{/i}."
    mc "Do you watch the awards shows, too?"
    show annabelle at center
    an "Oop! I'm so sorry! It looks like the developers ran out of time!"
    an "Go check out one of the other routes instead!"
    an "Toodles!"
    hide annabelle
    $ seenAnnabelle = True

    call chooseRoute

    #Determine the ending
    if(an_score > 0):
        call annabelle_good
    elif (an_score < 0):
        call annabelle_bad
    #Call a random ending if the score is 0
    else:
        $ chooseEnding = renpy.random.randint(1,2)
        if(chooseEnding == 1):
            call annabelle_good
        else:
            call annabelle_bad
    return

label annabelle_good:
    # tut "Annabelle: Good Ending"
    return

label annabelle_bad:
    # tut "Annabelle: Bad Ending"
    return
