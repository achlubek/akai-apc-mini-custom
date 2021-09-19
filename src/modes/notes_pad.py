from .. import leds
import device
import channels


class NotesPad:

    velocity = 0.5
    currentChannel = 0

    def __init__(self):
        print("Initializing NotesPad mode")

    def onEnable(self) -> None:
        print("Enabling NotesPad mode")
        leds.clearAll()
        self.currentChannel = channels.selectedChannel()

    def onDisable(self) -> None:
        print("Disabling NotesPad mode")

    def onRequestRefresh(self, flags) -> None:
        pass

    def onPadKeyDown(self, x: int, y: int, originalEvent) -> bool:
        originalEvent.note += 24
        originalEvent.velocity = int(255 * self.velocity)
        return False

    def onPadKeyUp(self, x: int, y: int, originalEvent) -> bool:
        return True

    def onControlXKeyDown(self, index: int, originalEvent) -> bool:
        if index == 2:
            self.currentChannel -= 1
            if self.currentChannel < 0:
                self.currentChannel = channels.channelCount() - 1
            if channels.channelCount() > 0:
                channels.deselectAll()
                channels.selectChannel(self.currentChannel)
                print("Selecting " + str(self.currentChannel))

        if index == 3:
            self.currentChannel += 1
            if self.currentChannel >= channels.channelCount():
                self.currentChannel = 0
            if channels.channelCount() > 0:
                channels.deselectAll()
                channels.selectChannel(self.currentChannel)
                print("Selecting " + str(self.currentChannel))

        return True

    def onControlXKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onControlYKeyDown(self, index: int, originalEvent) -> bool:
        return True

    def onControlYKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onSlidersValueChange(self, index: int, value) -> None:
        if index == 4:
            self.velocity = value
