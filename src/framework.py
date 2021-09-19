
COLOR_RED = 'Green'
COLOR_GREEN = 'Red'
COLOR_YELLOW = 'Yellow'

def color(c: str, flashing: bool) -> str:
    return c + "Flashing" if flashing else c

print(color(COLOR_RED, True));
print(color(COLOR_GREEN, False));

def handleSliderValueChange(index: int, value: float) -> None:
    print(f"Slider {str(index)} value {str(value)}")
