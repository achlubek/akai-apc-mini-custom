import device

COLOR_OFF = 0
COLOR_RED = 3
COLOR_RED_FLASHING = 4
COLOR_GREEN = 1
COLOR_GREEN_FLASHING = 2
COLOR_YELLOW = 5
COLOR_YELLOW_FLASHING = 6

ledsStateMap = [-1] * 90


def setLed(index: int, color: int) -> None:
    global ledsStateMap
    state = ledsStateMap[index]
    if state != color:
        device.midiOutMsg(0x90 + (index << 8) + (color << 16))
        ledsStateMap[index] = color


def clearAll():
    for index in range(0, 90):
        setLed(index, COLOR_OFF)


def getNoteForXYPad(x: int, y: int) -> int:
    return (7 - y) * 8 + x


def setXYPadColor(x: int, y: int, color: int) -> None:
    setLed(getNoteForXYPad(x, y), color)


def setXControlColor(index: int, color: int) -> None:
    setLed(index + 64, color)


def setYControlColor(index: int, color: int) -> None:
    setLed(index + 82, color)
