from .. import leds
import channels
import ui


class Sequencer:

    xOffset = 0

    def __init__(self):
        print("Initializing Sequencer mode")

    def onEnable(self) -> None:
        print("Enabling Sequencer mode")
        self.refreshLeds()

    def onUpdateMeters(self, pwm) -> None:
        pass

    def refreshLeds(self):
        count = channels.channelCount()
        if count > 8:
            count = 8
        for index in range(0, count):
            for step in range(0, 8):
                status = channels.getGridBit(index, step + self.xOffset * 8)
                if status > 0:
                    leds.setXYPadColor(step, index, leds.COLOR_GREEN)
                else:
                    leds.setXYPadColor(step, index, leds.COLOR_OFF)
        for index in range(count, 8):
            for step in range(0, 8):
                leds.setXYPadColor(step, index, leds.COLOR_OFF)
        ui.crDisplayRect(self.xOffset * 8, 0, 8, 8, 1000)
        for xcontrolLed in range(0, 8):
            color = leds.COLOR_RED if xcontrolLed == self.xOffset else leds.COLOR_OFF
            leds.setXControlColor(xcontrolLed, color)

    def onDisable(self) -> None:
        print("Disabling Sequencer mode")

    def onRequestRefresh(self, flags) -> None:
        self.refreshLeds()

    def onPadKeyDown(self, x: int, y: int, originalEvent) -> bool:
        count = channels.channelCount()
        if(y < count):
            status = channels.getGridBit(y, x + self.xOffset * 8)
            channels.setGridBit(y, x + self.xOffset * 8, 1 - status)
            self.refreshLeds()
        return True

    def onPadKeyUp(self, x: int, y: int, originalEvent) -> bool:
        return True

    def onControlXKeyDown(self, index: int, originalEvent) -> bool:
        self.xOffset = index
        self.refreshLeds()
        return True

    def onControlXKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onSlidersValueChange(self, index: int, value) -> None:
        pass
