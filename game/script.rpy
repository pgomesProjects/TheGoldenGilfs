﻿# The script of the game goes in this file.
# The game starts here.

label start:

    scene empty background

    #Define Names
    $ player = "Player"
    $ placeholder_name = "Your Dream Grandma"

    mc "This is {i}The Golden Gilfs.{/i}"

    menu:
        tut "Do you want to see hot grandmas in your area?"

        "Of Course!":
            call rightAnswer
        "I Do But I'm In Denial So I Must Say No.":
            call wrongAnswer
    return

label rightAnswer:
    show placeholder
    test "Great!"
    test "Once the game is complete, you will get to see hot grandmas!"
    return

label wrongAnswer:
    "Well, we don't need people like you."
    "Get out."
    return