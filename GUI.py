from Tkinter import *
import tkFont
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
##hardware
red = LED(24)
blue = LED(18)
green = LED(23)

##  GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkFont.Font(family='Helvetica',size = 12, weight="bold")

### EVENT FUNCTIONS ###
def redToggle():
	if red.is_lit:
		red.off()
		redButton["text"] = "Turn Red Led On"
	else:
		red.on()
		redButton["text"] = "Turn Red Led Off"
def blueToggle():
	if blue.is_lit:
		blue.off()
		blueButton["text"] = "Turn Blue Led On"
	else:
		blue.on()
		blueButton["text"] = "Turn Blue Led Off"
def greenToggle():
        if green.is_lit:
                green.off()
                greenButton["text"] = "Turn Green Led On"
        else:
                green.on()
                greenButton["text"] = "Turn Green Led Off"

def close():
	RPi.GPIO.cleanup()
	win.destroy()

### WIDGETS ###
redButton = Button(win, text = 'Turn Red Led On', font = myFont, command = redToggle, bg = 'bisque2',height =1, width = 24)
redButton.grid(row=0,column=1)

blueButton = Button(win, text = 'Turn Blue Led On', font = myFont, command = blueToggle,bg = 'bisque2',height =1, width = 24)
blueButton.grid(row=1,column=1)

greenButton = Button(win, text = 'Turn Green Led On', font = myFont, command = greenToggle,bg = 'bisque2',height =1, width = 24)
greenButton.grid(row=2,column=1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close,bg ='red',height =1, width = 6)
exitButton.grid(row=3,column=1)

win.protocol("WM DELETE WINDOW",close) #exit cleanly
win.mainloop() #loop forever
