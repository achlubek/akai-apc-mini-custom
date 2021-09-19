import device

COLOR_OFF = 0
COLOR_RED = 3
COLOR_RED_FLASHING = 4
COLOR_GREEN = 1
COLOR_GREEN_FLASHING = 2
COLOR_YELLOW = 5
COLOR_YELLOW_FLASHING = 6

def setDevice(d):
    device = d

def clearAll():
    for index in range(0, 90):
        device.midiOutMsg(0x90 + (index << 8) + (0x00 << 16))

def getNoteForXYPad(x: int, y: int) -> int:
    return (7 - y) * 8 + x

def setXYPadColor(x: int, y: int, color: int) -> None:
    device.midiOutMsg(0x90 + (getNoteForXYPad(x,y) << 8) + (color << 16))

def setXControlColor(index: int, color: int) -> None:
    device.midiOutMsg(0x90 + ((index + 64) << 8) + (color << 16))

def setYControlColor(index: int, color: int) -> None:
    device.midiOutMsg(0x90 + ((index + 82) << 8) + (color << 16))
