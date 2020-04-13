import os
import time
import keyboard
import pyscreenshot as ImageGrab
from datetime import datetime
from PIL import ImageChops

# Record rate (screenshots per second)
rate = 100
# Folder destination
dst = ''

def menu ():
    print("Online Classes - Press Enter to record", end="", flush=True)
    input()
    record()

def record ():

    print('Folder to save the record:',end=' ', flush=True)
    dst = input()

    if not os.path.exists(dst):
        os.mkdir(dst)
        print('Folder ' + dst + ' created.')

    # Just visual stuff
    print("The record starts in...", end=" ", flush=True)
    time.sleep(1)
    print("3", end=" ", flush=True)
    time.sleep(1)
    print("2", end=" ", flush=True)
    time.sleep(1)    
    print("1")
    time.sleep(1)
    print("Hold Ctrl+Shift+q to stop the recording")


    prev = ImageGrab.grab()
    prev.save(dst + '/'+ str(datetime.now()) + '.png')

    while 1:

        # sudo required
        if keyboard.is_pressed('ctrl+shift+q'): 
            break

        time.sleep(1/rate)
        im = ImageGrab.grab()

        diff = ImageChops.difference(prev,im)

        if diff.getbbox():
            im.save(dst + '/'+ str(datetime.now()) + '.png')

        prev = im


if __name__ == '__main__':
    menu()


