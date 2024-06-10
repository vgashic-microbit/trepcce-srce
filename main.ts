input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . # . # .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . # # # .
        `)
})
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . # # . .
        # # # # .
        . # # # #
        # # # # .
        . # # . .
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        # # # # #
        . # . # .
        `)
    basic.showLeds(`
        . . # # .
        . # # # #
        # # # # .
        . # # # #
        . . # # .
        `)
})
