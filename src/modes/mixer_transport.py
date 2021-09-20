from .. import leds
import mixer


class MixerTransport:

    xOffset = 0

    def __init__(self):
        print("Initializing MixerTransport mode")

    def onEnable(self) -> None:
        print("Enabling MixerTransport mode")
        leds.clearAll()

    def onUpdateMeters(self, pwm) -> None:
        for x in range(0, 8):
            for y in range(0, 8):
                peak = mixer.getTrackPeaks(x + 1 + 8 * self.xOffset, 2)
                intval = 8 - int(peak * 8.0)
                enableColor = leds.COLOR_GREEN
                if y < 4:
                    enableColor = leds.COLOR_YELLOW
                if y < 1:
                    enableColor = leds.COLOR_RED
                c = enableColor if y >= intval else leds.COLOR_OFF
                leds.setXYPadColor(x, y, c)

    def onDisable(self) -> None:
        print("Disabling MixerTransport mode")

    def onRequestRefresh(self, flags) -> None:
        pass

    def onPadKeyDown(self, x: int, y: int, originalEvent) -> bool:
        return True

    def onPadKeyUp(self, x: int, y: int, originalEvent) -> bool:
        return True

    def onControlXKeyDown(self, index: int, originalEvent) -> bool:
        self.xOffset = index
        return True

    def onControlXKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onSlidersValueChange(self, index: int, value) -> None:
        mixer.setTrackVolume(index + 1 + 8 * self.xOffset, value)
