from .. import leds
import device
import channels
import ui
import mixer
import transport


class MixerTransport:

    xOffset = 0

    def __init__(self):
        print("Initializing MixerTransport mode")

    def onEnable(self) -> None:
        print("Enabling MixerTransport mode")
        leds.clearAll()
        leds.setXYPadColor(0, 0, leds.COLOR_RED_FLASHING)  # record
        leds.setXYPadColor(1, 0, leds.COLOR_YELLOW)  # stop
        leds.setXYPadColor(2, 0, leds.COLOR_GREEN)  # start

        leds.setXYPadColor(0, 1, leds.COLOR_GREEN)  # ff
        leds.setXYPadColor(2, 1, leds.COLOR_GREEN)  # rw

    def onUpdateMeters(self) -> None:
        leftPeak = mixer.getLastPeakVol(0)
        rightPeak = mixer.getLastPeakVol(1)
        leftInt = 8 - int(leftPeak * 8.0)
        rightInt = 8 - int(rightPeak * 8.0)

        for y in range(0, 8):
            c = leds.COLOR_GREEN if y >= leftInt else leds.COLOR_OFF
            leds.setXYPadColor(6, y, c)
            c = leds.COLOR_GREEN if y >= rightInt else leds.COLOR_OFF
            leds.setXYPadColor(7, y, c)

    def onDisable(self) -> None:
        print("Disabling MixerTransport mode")

    def onRequestRefresh(self, flags) -> None:
        print("REFRESH")

    def onPadKeyDown(self, x: int, y: int, originalEvent) -> bool:
        if x == 0 and y == 0:
            transport.record()
        if x == 1 and y == 0:
            transport.stop()
        if x == 2 and y == 0:
            transport.start()

        if x == 0 and y == 1:
            transport.rewind(2)
        if x == 2 and y == 1:
            transport.fastForward(2)
        return True

    def onPadKeyUp(self, x: int, y: int, originalEvent) -> bool:
        if x == 0 and y == 1:
            transport.rewind(0)
        if x == 2 and y == 1:
            transport.fastForward(0)
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
