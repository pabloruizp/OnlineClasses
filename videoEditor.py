import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from PIL import ImageChops
from numpy  import asfarray
from moviepy.editor import *
from progress.bar import ShadyBar

compiledFolder = 'CUT'

def menu():
    print('Folder with the videos to cut:',end=' ', flush=True)

    dst = input()

    if not os.path.exists(dst + '/' + compiledFolder):
        os.mkdir(dst + '/' + compiledFolder)
        print('Folder ' + dst + ' created.')

    dirList = os.listdir(dst)
    dirList.remove(compiledFolder)

    for video in dirList:
        cutVideo(dst,video) 


def cutVideo(folderName,fileName):

    video = VideoFileClip(folderName + '/' + fileName)
    audio = AudioFileClip(folderName + '/' + fileName)


    clips = []
    values = []

    totalFrames = int(audio.duration*audio.fps)

    nFrame = 0

    bar = ShadyBar('Getting values  ', max=100, suffix = '%(percent).1f%% - %(eta)ds')

    for frame in audio.iter_frames():
        values.append(abs(frame[0]))
        nFrame = nFrame + 1
        if nFrame % int(totalFrames / 100)  == 0:
            bar.next()

    bar.finish()

    average = sum(values)/len(values)

    margin = audio.fps / 20 # 0.05 secs of margin

    nFrame = 0
    beg = 0
    end = 0
    silence = False

    marginloop = margin

    bar = ShadyBar('Removing silence', max=100, suffix = '%(percent).1f%% - %(eta)ds')

    for frame in audio.iter_frames():

        if abs(frame[0]) < (average / 5):
            if not silence:
                marginloop = marginloop - 1

                if marginloop <= 0:
                    silence = True
        else:
            if silence:
                clips.append(video.subclip(beg/audio.fps,end/audio.fps))
                beg = nFrame

            marginloop = margin
            end = nFrame
            silence = False

        nFrame = nFrame + 1
        if nFrame % int(totalFrames / 100)  == 0:
            bar.next()

    bar.finish()

    clips.append(video.subclip(beg/audio.fps,end/audio.fps))

    final = concatenate_videoclips(clips)
    final.write_videofile(folderName + '/' + compiledFolder + '/CUT-' + fileName)

if __name__ == '__main__':
    menu()
