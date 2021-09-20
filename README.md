# Custom FL Studio 20 script for AKA APC Mini

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