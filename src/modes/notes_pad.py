from .. import leds
import device

class NotesPad:
    def __init__(self):
        print("Initializing NotesPad mode")

    def onEnable(self, x: int, y: int) -> None:
        print("Enabling NotesPad mode")
        leds.clearAll()

    def onDisable(self, x: int, y: int) -> None:
        print("Disabling NotesPad mode")

    def onPadKeyDown(self, x: int, y: int, originalEvent) -> bool:
        originalEvent.note += 24
        return False

    def onPadKeyUp(self, x: int, y: int, originalEvent) -> bool:
        return True

    def onControlXKeyDown(self, index: int, originalEvent) -> bool:
        return True

    def onControlXKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onControlYKeyDown(self, index: int, originalEvent) -> bool:
        return True

    def onControlYKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onSlidersValueChange(self, index: int, value) -> None:
        pass