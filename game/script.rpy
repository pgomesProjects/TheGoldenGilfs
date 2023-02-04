# The script of the game goes in this file.
# The game starts here.

label start:

    #Stops main menu music with a fade
    $renpy.music.stop(fadeout = 1.0)

    #Define Names
    $ mi_name = "???"
    $ hl_name = "???"
    $ an_name = "???"

    # Define scores
    $ mi_score = 0
    $ hl_score = 0
    $ an_score = 0

    call intro

    return

label intro:
    scene black
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

    menu:
        tut "Where would you like to go?"

        "Crafts Room":
            call craftsRoom
        "Game Room":
            call gameRoom
        "Communal Lounge":
            call communalLounge

    return

label craftsRoom:
    "You decide to head to the crafts room."
    "It's a nice cozy space, with cubbies and bins of various craft supplies."
    "There's plenty of yarn, thread, paint, paper, clay, pencils - whatever aspiring arts-and-crafters might want."
    "A couple ladies are sitting in rocking chairs, gossiping while they crochet garish lap blankets."
    "You sit at the puzzle table for now."
    "It has a green felt top, to keep puzzles from breaking apart."
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
    mi "Isn't it just?"

    menu:
        mi "Do you have any grandchildren?"
        "Yes.":
            mi "Oh, how darling!"
            mi "I hope you get to see them as often as their little hearts desire."
            $ mi_score += 1
        "No.":
            mi "Oh, that's a shame."
            mi "I think every elderly person deserves grandchildren to dote on."

    "She smiles brightly at you."
    $ mi_name = "Miriam"
    mi "I'm Miriam. Have I seen you around before?"
    mc "I'm [playerName]. I haven't been very social lately."
    mi "Well, you've come to just the right place, [playerName]!"

    menu:
        mi "Would you like to help me put this puzzle together?"
        "That sounds nice.":
            $ helping = True
            mi "You're so sweet. Thank you!"
            "You do your best to help Miriam with the puzzle, matching pieces that look like they might go together."

        "No, thank you, but I'd love to keep you company.":
            $ helping = False
            "Miriam lowers her voice."
            mi "That’s lovely of you."
            mi "See, I come here every morning to work on this puzzle, and those two old biddies in the corner are always there gossiping!"
            mi "I don't think their blankets will ever be done!"
            "You're not sure you'd be much help with the puzzle, so you're okay with watching instead."

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
                mi "Did you know there’s a community garden here?"
                mc "I did."
                mc "Maybe I should go out there and dig in the dirt again, like I used to."
                mi "Borrow their gardening tools! And make sure to take plenty of breaks."
                mi "Don’t overexert yourself."
                "Miriam winks at you."
                $ mi_score += 1
            "Watercolor Painting":
                mi "Oh, that sounds lovely."
                mi "I bet your watercolors are very pretty."
                mc "Thank you."
            "Taxidermy":
                mi "What an...odd hobby."
                mi "Aren’t all those chemicals bad for you?"
                mc "Well, yes."
                mc "I stopped doing it myself years ago, but I still have a collection."
                mi "Well, er..."
                $ mi_score -= 1

    mi "I used to knit like a wild woman in my younger years."
    menu:
        mi "The arthritis in my wrists is too poor for it now."
        "Did you knit that sweater you're wearing?":
            "Miriam perks up at your question."
            mi "Why, yes, I did!"
            mi "It’s my favorite color: cherry pie red."
            mi "I just love cherry pie."
            $ mi_score += 1
        "That's very unfortunate.":
            mc "I have arthritis in my knee."
            mc " I can't walk long distances anymore, like that one song with the Scottish singers."
            mi "..."
            "Miriam doesn’t seem to understand your reference."
            $ mi_score -= 1

    "The two of you sit quietly for a little while longer."
    if(helping):
        "You're doing well putting together the shell the Venus cat stands on."
        "Although, you wish you had attached it to the rest of the puzzle border and not the other way around."
    else:
        "You wonder if she will end up framing this puzzle on the wall."
        "Her granddaughter has good taste."

    mi "Tell me, [playerName]."
    menu:
        mi "Do you like cats?"
        "Yes, I do.":
            mi "Oh, wonderful! I just adore them."
            mi "They are the cutest, silliest little things."
            mi "I have three I brought here with me. They're sleeping in my room."
            $ mi_score += 1
        "No, I prefer dogs.":
            mc "Unfortunately, I've never owned cats."
            mc "I have a King Charles Spaniel I brought with me named Daisy."
            "Miriam tuts. It seems like she disapproves."
            mi "I much prefer the independence of kittycats, but to each their own."
            mi "Dogs can be sweet in...in their own way."
            $ mi_score -= 1

    "Suddenly, a soft chime sounds in the room."
    "It's the bell marking the top of the hour."
    mi "Oh, goodness! I really must be going."
    mi "I just stepped out for a little bit while my pie was baking."

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
    tut "Miriam: Good Ending"
    return

label miriam_bad:
    tut "Miriam: Bad Ending"
    return

label gameRoom:
    

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
    tut "Helen: Good Ending"
    return

label helen_bad:
    tut "Helen: Bad Ending"
    return

label communalLounge:


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
    tut "Annabelle: Good Ending"
    return

label annabelle_bad:
    tut "Annabelle: Bad Ending"
    return
