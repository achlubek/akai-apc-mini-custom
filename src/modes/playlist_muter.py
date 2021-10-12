from .. import leds
import mixer
import playlist


class PlaylistMuter:

    xOffset = 0

    trackVolumesMemory = [0.0] * 64

    def __init__(self):
        print("Initializing PlaylistMuter mode")

    def onEnable(self) -> None:
        print("Enabling PlaylistMuter mode")
        leds.clearAll()
        leds.setXControlColor(self.xOffset, leds.COLOR_RED_FLASHING)

    def onUpdateMeters(self, pwm) -> None:
        self.updateMuteLeds()
        for y in range(8 * 0, 8 * 1):
            self.updateTrackActivity(pwm, y, 1, y - 8 * 0)
        for y in range(8 * 1, 8 * 2):
            self.updateTrackActivity(pwm, y, 3, y - 8 * 1)
        for y in range(8 * 2, 8 * 3):
            self.updateTrackActivity(pwm, y, 5, y - 8 * 2)
        for y in range(8 * 3, 8 * 4):
            self.updateTrackActivity(pwm, y, 7, y - 8 * 3)

    def updateTrackActivity(self, pwm, trackIndex, xPadIndex, yPadIndex):
        peak = playlist.getTrackActivityLevel(trackIndex + 1)
        peakVis = playlist.getTrackActivityLevelVis(trackIndex + 1)
        peakVis -= 0.5
        peakVis = max(peakVis, 0.0)
        peakVis *= 2.0
        self.trackVolumesMemory[trackIndex] += peakVis * 3.0
        self.trackVolumesMemory[trackIndex] *= 0.95
        self.trackVolumesMemory[trackIndex] = min(
            self.trackVolumesMemory[trackIndex], 1.0)
        if(self.trackVolumesMemory[trackIndex] < 0.1):
            self.trackVolumesMemory[trackIndex] = 0.0
        self.gradientLed(pwm,
                         xPadIndex, yPadIndex, self.trackVolumesMemory[trackIndex] * 0.5 + min(0.5, peak), leds.COLOR_YELLOW)

    def gradientLed(self, pwm, x, y, value, color):
        if(value <= 0.0):
            leds.setXYPadColor(x, y, leds.COLOR_OFF)
        else:
            comparer = int((1.0 - value) * 10.0) + 1
            leds.setXYPadColor(x, y, color if pwm %
                               comparer == 0 else leds.COLOR_OFF)

    def onDisable(self) -> None:
        print("Disabling PlaylistMuter mode")

    def onRequestRefresh(self, flags) -> None:
        pass

    def updateMuteLeds(self):
        for x in range(0, 4):
            for y in range(8 * x, 8 * (x + 1)):
                if playlist.isTrackMuted(y + 1):
                    leds.setXYPadColor(x * 2, y - (8 * x), leds.COLOR_RED)
                else:
                    leds.setXYPadColor(x * 2, y - (8 * x), leds.COLOR_GREEN)

    def onPadKeyDown(self, x: int, y: int, originalEvent) -> bool:
        if x % 2 == 0:
            track = 1 + y + int(x / 2) * 8
            playlist.muteTrack(track)
            self.updateMuteLeds()
        return True

    def onPadKeyUp(self, x: int, y: int, originalEvent) -> bool:
        return True

    def onControlXKeyDown(self, index: int, originalEvent) -> bool:
        leds.setXControlColor(self.xOffset, leds.COLOR_OFF)
        self.xOffset = index
        leds.setXControlColor(self.xOffset, leds.COLOR_RED)
        return True

    def onControlXKeyUp(self, index: int, originalEvent) -> bool:
        return True

    def onSlidersValueChange(self, index: int, value) -> None:
        mixer.setTrackVolume(index + 1 + 8 * self.xOffset, value)
