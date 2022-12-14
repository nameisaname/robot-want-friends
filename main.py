def on_button_pressed_a():
    serial.write_line("do you be friend of microbit?")
    if input.pin_is_pressed(TouchPin.P0):
        serial.write_line("yes")
    else:
        serial.write_line("no")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)
    serial.write_line("why all is shaking?!")
    basic.pause(1000)
    serial.write_line("oh its you")
    basic.pause(100)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(1000)
    serial.write_line("you want to be friends?")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

serial.write_string("to be friends press P0")
basic.show_icon(IconNames.ASLEEP)
serial.write_line("hi")