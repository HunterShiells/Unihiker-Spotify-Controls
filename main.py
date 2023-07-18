from pinpong.extension.unihiker import *
from pinpong.board import Board, Pin
from unihiker import GUI
import spotify_functions as sf
from PIL import Image
import requests
import io
import time

# Event callback functions
def button_click1():
    buzzer.pitch(131, 1)
    sf.prev_song()
    update_image()

def button_click2():
    buzzer.pitch(147, 1)
    sf.play_pause()
    update_image()

def button_click3():
    buzzer.pitch(165, 1)
    sf.next_song()
    update_image()

def update_image():
    # Fetch the updated image from the URL
    response = requests.get(sf.get_image())
    image_data = response.content

    # Open the updated image using Pillow
    image = Image.open(io.BytesIO(image_data))

    # Update the image on the GUI
    do.config(image=image)
    u_gui.update()

# Initialize the GUI and board
u_gui = GUI()
Board().begin()

# Fetch the initial image from the URL
response = requests.get(sf.get_image())
image_data = response.content

# Open the initial image using Pillow
image = Image.open(io.BytesIO(image_data))

# Draw the image on the GUI
do = u_gui.draw_image(image=image, x=20, y=3)
do.config(h=200)

# Draw the previous button on the GUI
my = u_gui.draw_image(image="PREV.png", x=0, y=215)
my.config(h=75)
my.config(onclick=button_click1)

# Draw the play/pause button on the GUI
re = u_gui.draw_image(image="PLAY.png", x=82.5, y=215)
re.config(h=75)
re.config(onclick=button_click2)

# Draw the next button on the GUI
mi = u_gui.draw_image(image="NEXT.png", x=165, y=215)
mi.config(h=75)
mi.config(onclick=button_click3)

while True:
    time.sleep(0.01)
