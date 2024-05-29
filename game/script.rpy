# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define b = Character("Bertram", color="ffc8c8")

# Images
image bg room = "assets/bg01-hallway.jpg"

# The game starts here.

label start:
    scene bg room
    pause

    show screen EileenScreen with dissolve

    e "Hello there! How are you today?"

    show screen BertramScreen with dissolve

    b "I'm good, thank you! And you?"
    e "I'm doing well, thanks for asking."
    b "Alright, let's get back to the main menu."

    hide EileenScreen with dissolve
    hide BertramScreen with dissolve
    pause

    return
