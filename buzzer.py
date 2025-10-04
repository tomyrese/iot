from gpiozero import Buzzer
from signal import pause

bz = Buzzer(12)
bz.beep(0.1, 1)

pause()
