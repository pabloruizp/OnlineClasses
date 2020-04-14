import os
import time
import keyboard
import pyscreenshot as ImageGrab

from PIL import ImageChops
from datetime import datetime

# Record rate (screenshots per second)
rate = 1000
# Folder destination
dst = ''
# Tolerance %
tolerance = 50

def menu ():
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
            area = diff.size[0] * diff.size[1]
            
            coorDiff = diff.getbbox()
            areaDiff = (coorDiff[2] - coorDiff[0]) * (coorDiff[3] - coorDiff[1])

            if (areaDiff / area) * 100 > tolerance:  
                im.save(dst + '/'+ str(datetime.now()) + '.png')
                prev = im


if __name__ == '__main__':
    menu()


