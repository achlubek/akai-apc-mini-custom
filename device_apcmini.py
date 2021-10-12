# name=AKAI APC Mini (AFL CUSTOM)

from src.modes.sequencer import Sequencer
from src.modes.notes_pad import NotesPad
from src.modes.mixer_transport import MixerTransport
from src.modes.playlist_muter import PlaylistMuter
import mixer
import midi
import device
import ui

import transport

from src import framework
from src import leds

modes = [Sequencer(), NotesPad(), MixerTransport(), PlaylistMuter()]

currentModeIndex = 2

currentMode = modes[currentModeIndex]

# default note is 72

mixerWindowIndex = 0
channelRackWindowIndex = 1
playlistWindowIndex = 2
pianoRollWindowIndex = 3


def OnNoteOn(event):
    global currentModeIndex
    global currentMode
    print('Midi note on:', event.data1, " ", event.data2)
    n = event.data1
    if(framework.isXYPad(n)):
        coords = framework.getXYTopLeft00ForPad(n)
        print(f"XYPad DOWN Control X: {str(coords[0])}, Y: {str(coords[1])}")
        event.handled = currentMode.onPadKeyDown(coords[0], coords[1], event)

    if(framework.isXControl(n)):
        index = framework.getIndexForXControl(n)
        print(f"X DOWN Control {str(index)}")
        event.handled = currentMode.onControlXKeyDown(index, event)

    if(framework.isYControl(n)):
        index = framework.getIndexForYControl(n)
        print(f"Y DOWN Control {str(index)}")
        if index == 0:
            transport.start()
        if index == 1:
            transport.stop()
        if index == 2:
            transport.record()
        if index == 3:
            transport.setLoopMode()

        if index == 4:
            ui.showWindow(mixerWindowIndex)
        if index == 5:
            ui.showWindow(channelRackWindowIndex)
        if index == 6:
            ui.showWindow(playlistWindowIndex)
        if index == 7:
            ui.showWindow(pianoRollWindowIndex)

        event.handled = True

    if(framework.isShift(n)):
        print(f"Shift DOWN {str(n)}")
        currentModeIndex += 1
        if currentModeIndex >= len(modes):
            currentModeIndex = 0
        currentMode.onDisable()
        currentMode = modes[currentModeIndex]
        currentMode.onEnable()
        event.handled = True


def OnNoteOff(event):
    n = event.data1
    if(framework.isXYPad(n)):
        coords = framework.getXYTopLeft00ForPad(n)
        print(f"XYPad UP Control X: {str(coords[0])}, Y: {str(coords[1])}")
        event.handled = currentMode.onPadKeyUp(coords[0], coords[1], event)

    if(framework.isXControl(n)):
        index = framework.getIndexForXControl(n)
        print(f"X UP Control {str(index)}")
        event.handled = currentMode.onControlXKeyUp(index, event)

    if(framework.isYControl(n)):
        index = framework.getIndexForYControl(n)
        print(f"Y UP Control {str(index)}")
        event.handled = True

    if(framework.isShift(n)):
        print(f"Shift UP {str(n)}")
        event.handled = True


disableMeters = False


def OnControlChange(event):
    global disableMeters
    disableMeters = True
    if (event.pmeFlags & midi.PME_System != 0):
        index = event.data1 - 48
        data = event.data2/127
        if index == 8:
            mixer.setTrackVolume(0, data)
        else:
            currentMode.onSlidersValueChange(index, data)


def OnInit():
    device.setHasMeters()
    leds.clearAll()
    leds.setYControlColor(0, leds.COLOR_GREEN)
    leds.setYControlColor(1, leds.COLOR_GREEN)
    leds.setYControlColor(2, leds.COLOR_GREEN)
    leds.setYControlColor(3, leds.COLOR_OFF)

    leds.setYControlColor(4, leds.COLOR_GREEN)
    leds.setYControlColor(5, leds.COLOR_GREEN)
    leds.setYControlColor(6, leds.COLOR_GREEN)
    leds.setYControlColor(7, leds.COLOR_GREEN)
    currentMode.onEnable()


def OnDeInit():
    currentMode.onDisable()
    leds.clearAll()


def OnRefresh(flags):
    currentMode.onRequestRefresh(flags)


def OnIdle():
    pass


pwm = 0


def OnUpdateMeters():
    global pwm
    global disableMeters
    if not disableMeters:
        pwm += 1
        currentMode.onUpdateMeters(pwm)
        if transport.getLoopMode() == 1:
            leds.setYControlColor(3, leds.COLOR_GREEN)
        else:
            leds.setYControlColor(3, leds.COLOR_OFF)

        if transport.isRecording():
            if pwm % 30 < 15:
                leds.setYControlColor(2, leds.COLOR_GREEN)
            else:
                leds.setYControlColor(2, leds.COLOR_OFF)
        else:
            leds.setYControlColor(2, leds.COLOR_GREEN)

        if transport.isPlaying():
            if pwm % 30 < 15:
                leds.setYControlColor(0, leds.COLOR_GREEN)
                leds.setYControlColor(1, leds.COLOR_OFF)
            else:
                leds.setYControlColor(0, leds.COLOR_OFF)
                leds.setYControlColor(1, leds.COLOR_GREEN)
        else:
            leds.setYControlColor(0, leds.COLOR_GREEN)
            leds.setYControlColor(1, leds.COLOR_OFF)

        if ui.getFocused(mixerWindowIndex):
            leds.setYControlColor(4, leds.COLOR_GREEN)
        else:
            leds.setYControlColor(4, leds.COLOR_OFF)

        if ui.getFocused(channelRackWindowIndex):
            leds.setYControlColor(5, leds.COLOR_GREEN)
        else:
            leds.setYControlColor(5, leds.COLOR_OFF)

        if ui.getFocused(playlistWindowIndex):
            leds.setYControlColor(6, leds.COLOR_GREEN)
        else:
            leds.setYControlColor(6, leds.COLOR_OFF)

        if ui.getFocused(pianoRollWindowIndex):
            leds.setYControlColor(7, leds.COLOR_GREEN)
        else:
            leds.setYControlColor(7, leds.COLOR_OFF)

        if pwm > 1000000:
            pwm = 0
    disableMeters = False
