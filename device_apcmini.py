# name=AKAI APC Mini (AFL CUSTOM)

from src.modes.sequencer import Sequencer
from src.modes.notes_pad import NotesPad
from src.modes.mixer_transport import MixerTransport
from src.modes.playlist_muter import PlaylistMuter
import mixer
import midi
import device
import ui

from src import framework
from src import leds

modes = [Sequencer(), NotesPad(), MixerTransport(), PlaylistMuter()]

currentModeIndex = 3

currentMode = modes[currentModeIndex]

# default note is 72


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
        event.handled = currentMode.onControlXKeyDown(index, event)

    if(framework.isShift(n)):
        print(f"Shift DOWN {str(n)}")
        currentModeIndex += 1
        if currentModeIndex >= len(modes):
            currentModeIndex = 0
        currentMode.onDisable()
        currentMode = modes[currentModeIndex]
        currentMode.onEnable()
        event.handled = True

    # if event.data1 > 63 and event.data1 < 81 or event.data1 > 81 and event.data1 < 88:	#Check to see if the note is in the range used by the patch selector
    #     event.handled = True #Start by telling FL we are dealing with this note to stop it from playing a tone
    #     setPatchBank(event.data1) #If it is, pass it through to the function that selects patches
    #     ui.setHintMsg("Bank " + str(selectedBank) + " selected (" + str(((selectedBank-1)*9)) + "-" + str(((selectedBank-1)*9)+8) + ")")
    # elif event.data1 == 98:
    #     ui.setHintMsg("LEDs Turned off")
    #     clearAllLEDs()
    #     event.handled = True
    # else:
    #     event.handled = False #Allows you to continue to use the pads inside of the FPC if you want to


def OnNoteOff(event):  # Tell FL what to do with note off data
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
        event.handled = currentMode.onControlXKeyUp(index, event)

    if(framework.isShift(n)):
        print(f"Shift UP {str(n)}")
        event.handled = True


def OnControlChange(event):  # Let's define what FL will do when a slider moves
    # Not entirely sure what this does, (pretty certian it rate limits) but it seems to improve performance, so I'll leave it in.
    if (event.pmeFlags & midi.PME_System != 0):
        # mixer.setTrackVolume(bankSliderToChan(selectedBank, event.data1), event.data2/127) #Set the mixer track volume according to the input
        currentMode.onSlidersValueChange(event.data1 - 48, event.data2/127)


def OnInit():
    device.setHasMeters()
    currentMode.onEnable()


def OnDeInit():
    currentMode.onDisable()


def OnRefresh(flags):
    currentMode.onRequestRefresh(flags)


def OnIdle():
    pass


def OnUpdateMeters():
    currentMode.onUpdateMeters()
