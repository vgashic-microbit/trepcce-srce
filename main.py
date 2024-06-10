def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . # . # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        . # # . .
        # # # # .
        . # # # #
        # # # # .
        . # # . .
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        # # # # #
        . # . # .
        """)
    basic.show_leds("""
        . . # # .
        . # # # #
        # # # # .
        . # # # #
        . . # # .
        """)
basic.forever(on_forever)
