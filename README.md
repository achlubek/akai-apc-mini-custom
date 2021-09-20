# Custom FL Studio 20 script for AKA APC Mini

# For modes description, scroll down, below installation instruction

## Installation
### Manually
- Downloads the latest release zip file from here: https://github.com/achlubek/akai-apc-mini-custom/releases
- Find your scripts directory, for Windows, by default, it's C:\Users\YOUR USER HERE\Documents\Image-Line\FL Studio\Settings\Hardware
- Create directory there named `APC Mini` and paste zip file contents there, so that both `src` directory and `device_apcmini.py` file are in this `APC Mini` directory
- Ensure your have your AKAI APC Mini plugged it
- Boot up FL Studio
- Go to OPTIONS -> MIDI settings
- In output, enable AKAI APC Mini and set it's port to 0 (this might not be neccessary)
- In input, also enable AKAI APC Mini and set it's port to 0
- Below Input list, ensure Enable is checked
- Right to Enable checkbox, there is a dropdown with Controller type, select AKAI APC Mini (AFL CUSTOM) (user), this will probably be at the right side of the dropdown
- How it should look like: 

![Example](https://i.imgur.com/E6imXIP.png)

Then enjoy! Write any issues, problems and suggestions in Issues tab on github, also contributions are welcome!

# HOW TO USE
## Common controls for ALL the modes:
- `SHIFT` key iterates between modes
- Slider below `SHIFT` key controls Master Volume
- First circle button on the right is `PLAY`
- Second circle button on the right is `STOP`
- Third circle button on the right is `RECORD ARM`
- Fourth circle button on the right is `Song/Pattern` switch
- Below are 4 circle buttons to switch between windows, in order: Mixer, ChannelRack, Playlist, PianoRoll

Main 8x8 button matrix, circle buttons below matrix and sliders except the last one are controlled by Modes, look below for descriptions

# By default the script boots into MixerTransport mode

# MixerTransport mode description:
- Sliders control volume of tracks
- Circle buttons below matrix control track offset, for example, pressing first circle button from the left will make the mode use tracks 1-8, pressing next one will switch to 9-16 and so on
- Buttons matrix show track volume peaks level dynamically when something is playing

# NotesPad mode description:
- Buttons matrix works like a normal keyboard playing notes
- Buttons below matrix labelled as `<` and `>` iterate between instruments in channel rack
- Slider labelled `VOLUME` controls notes velocity

# Sequencer mode description:
- Buttons matrix work like sequencer steps in channel rack
- Buttons below matrix work as horizontal offset for sequencer, pressing first one sets the offset to 0, pressing second one sets the offset to 8 and so on
- What is displayed on the APC is also shown in FL Studio by a red square that is displayed when offset changes

# PlaylistMuter mode description:
- Buttons matrix will display 4 columns of 2 column data, so first 32 tracks from playlist are shown
- Green/Red buttons on matrix indicate the track is muted or not muted
- The off or yellow blinking button next to mute/unmute button shows track activity, it will blink and light up when track plays something
- Pressing Green/Red button will mute/unmute the track