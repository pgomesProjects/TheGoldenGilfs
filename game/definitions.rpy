define gui.charaters_text_outlines = [ (0, "#00000080", 2, 2) ]

define tut = Character(None, what_color='#59B84F', what_italic=True)

define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#DB7093", who_outlines=[ (1, "#000000") ])
define test = DynamicCharacter('placeholder_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#454046", who_outlines=[ (1, "#000000") ])

image placeholder:
    LiveComposite(
        (625,1000),
        (0,0), im.MatrixColor("actors/placeholder/placeholder_%s.png"%(p_emotion),im.matrix.tint(huer, hueg, hueb)),
        )

init:
    #Current emotions
    $ p_emotion = 'neutral'

    #Hues for images
    $ huer = 1.0
    $ hueg = 1.0
    $ hueb = 1.0
