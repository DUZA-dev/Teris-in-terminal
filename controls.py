import keyboard


def unhook_hotkeys():
    try:
        keyboard.unhook_all_hotkeys()
    except AttributeError:
        pass


def update(figure):
    unhook_hotkeys()

    keyboard.add_hotkey("up", figure.coup)
    keyboard.add_hotkey("down", figure.declineCheckConditions)
    keyboard.add_hotkey("left", figure.moving, args=('left',))
    keyboard.add_hotkey("right", figure.moving, args=('right',))

    keyboard.add_hotkey("w", figure.coup)
    keyboard.add_hotkey("s", figure.declineCheckConditions)
    keyboard.add_hotkey("a", figure.moving, args=('left',))
    keyboard.add_hotkey("d", figure.moving, args=('right',))

    keyboard.add_hotkey("k", figure.coup)
    keyboard.add_hotkey("j", figure.declineCheckConditions)
    keyboard.add_hotkey("h", figure.moving, args=('left',))
    keyboard.add_hotkey("l", figure.moving, args=('right',))

    keyboard.add_hotkey("num 8", figure.coup)
    keyboard.add_hotkey("num 2", figure.declineCheckConditions)
    keyboard.add_hotkey("num 4", figure.moving, args=('left',))
    keyboard.add_hotkey("num 6", figure.moving, args=('right',))
