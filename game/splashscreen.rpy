##Splashscreen
##
##This is the animation that occurs before the title screen when the game is opened

init python:
    splash_message_default = "This Game Is Intended For Mature Audiences.\nPlease Play At Your Own Risk."

image white_screen = "#FFFFFF"
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5, text_align = 0.5, size = 50)

label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass

    $ renpy.music.play(config.main_menu_music)

    $ renpy.pause(1.0, hard='True')

    $ config.allow_skipping = False

    show white_screen with dissolve
    $ splash_message = splash_message_default
    show splash_warning "[splash_message]" with Dissolve(2.0, alpha=True)
    $ renpy.pause(2.0, hard='True')

    hide white_screen with dissolve

    $ config.allow_skipping = True

return
