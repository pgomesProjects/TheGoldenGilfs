# The script of the game goes in this file.
# The game starts here.

label start:

    #Stops main menu music with a fade
    $renpy.music.stop(fadeout = 1.0)

    #Define Names
    $ mi_name = "???"
    $ hl_name = "???"
    $ an_name = "???"

    call intro

    return

label intro:
    scene black
    "The morning sun shines in through the blinds in your bedroom window, as it does every morning."
    "It feels a little lonely..."
    "But you’ve gotten used to that."
    "As you get up and make your bed, you think about your plans for the day."
    "First things first, making yourself a cup of coffee."
    "Then, choosing some clothes that make you happy, and taking a nice warm shower."
    "A warm shower is always a nice start to the day."
    "Breakfast. You have some fiber cereal left, but the sugar-free vanilla yogurt might be a better choice today."
    "Its expiration date is soon."
    "And there’s some fresh peaches you left out on the counter to ripen. You could have those too."
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
    "After all, your partner meant so much to you. You wouldn’t want to rush yourself."
    "But you’ve decided today’s the day."
    "Even if you don’t meet anyone new, you’re at least going to go out there and be around people more."
    "You don’t expect to meet anyone new right away anyway..."
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
    return

label gameRoom:
    return

label communalLounge:
    return
