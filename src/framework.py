def handleSliderValueChange(index: int, value: float) -> None:
    print(f"Slider {str(index)} value {str(value)}")

def isXYPad(note: int) -> bool:
    if note >= 0 and note < 64:
        return True
    return False

def isXControl(note: int) -> bool:
    if note >= 64 and note < 72:
        return True
    return False

def isYControl(note: int) -> bool:
    if note >= 82 and note < 90:
        return True
    return False

def isShift(note: int) -> bool:
    if note == 98:
        return True
    return False

def getIndexForXControl(note: int) -> int:
    return note - 64

def getIndexForYControl(note: int) -> int:
    return note - 82

def getXYTopLeft00ForPad(note: int) -> list:
    x = note % 8
    y = (note - x) / 8
    y = int(8 - y) - 1
    return [x, y]
