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
