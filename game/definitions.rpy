define gui.charaters_text_outlines = [ (0, "#00000080", 2, 2) ]

define tut = Character(None, what_color='#23975F', what_italic=True)

define mc = DynamicCharacter('playerName', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#A05A06", who_outlines=[ (0, "#000000") ])
define mi = DynamicCharacter('mi_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#903434", who_outlines=[ (0, "#000000") ])
define hl = DynamicCharacter('hl_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#4F4078", who_outlines=[ (0, "#000000") ])
define an = DynamicCharacter('an_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#CC9A96", who_outlines=[ (0, "#000000") ])

define chatty = DynamicCharacter('chatty_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#000000", who_outlines=[ (0, "#000000") ])
define nosy = DynamicCharacter('nosy_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#000000", who_outlines=[ (0, "#000000") ])
define unremark = DynamicCharacter('unremark_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#000000", who_outlines=[ (0, "#000000") ])

define test = DynamicCharacter('placeholder_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#454046", who_outlines=[ (1, "#000000") ])

image miriam:
    LiveComposite(
        (625,1000),
        (0,0), im.MatrixColor("actors/miriam/miriam_%s.png"%(mi_emotion),im.matrix.tint(huer, hueg, hueb)),
        )

image helen:
    LiveComposite(
        (450,1280),
        (0,0), im.MatrixColor("actors/helen/helen_%s.png"%(hl_emotion),im.matrix.tint(huer, hueg, hueb)),
        )

image annabelle:
    LiveComposite(
        (625,1000),
        (0,0), im.MatrixColor("actors/annabelle/annabelle_%s.png"%(an_emotion),im.matrix.tint(huer, hueg, hueb)),
        )

image placeholder:
    LiveComposite(
        (625,1000),
        (0,0), im.MatrixColor("actors/placeholder/placeholder_%s.png"%(p_emotion),im.matrix.tint(huer, hueg, hueb)),
        )

##Backgrounds
image bg room = "backgrounds/bedroom.png"
image bg crafts = "backgrounds/craftsRoom.png"
image bg game = "backgrounds/gameRoom.png"
image bg lounge = "backgrounds/communalLounge.png"
image bg apartment = "backgrounds/apartment.png"

init:
    #Current emotions
    $ p_emotion = 'neutral'
    $ mi_emotion = 'neutral'
    $ hl_emotion = 'neutral'
    $ an_emotion = 'neutral'

    #Hues for images
    $ huer = 1.0
    $ hueg = 1.0
    $ hueb = 1.0

default playerName = ""
default playerGender = "Male"
