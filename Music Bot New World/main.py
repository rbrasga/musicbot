from ast import If
import cv2
import pyautogui
import time
import random
import mss
import numpy as np
from PIL import Image
import gc
pyautogui.FAILSAFE = False

def click():
        pyautogui.click(button='left')
        pyautogui.click(button='right')

def main():

    # Adding randomness to the wait times for the animations
    animationSleepTime = .1 + (.1 * random.random())

    # Finds all Windows with the title "New World"
    newWorldWindows = pyautogui.getWindowsWithTitle("New World")

    # Find the Window titled exactly "New World" (typically the actual game)
    for window in newWorldWindows:
        if window.title == "New World":
            newWorldWindow = window
            break

    cv2.namedWindow("visuals", cv2.WINDOW_NORMAL)
    
    # Select that Window
    newWorldWindow.activate()

    # Selecting the Start Area
    mssRegion = {"mon": 1, "top": (600), "left": (1065), "width": (250), "height": (50)}

     # Selecting the Note Area
    mssRegionNote = {"mon": 1, "top": (760), "left": (550), "width": (115), "height": (200)}
    
    # Selecting the Skip button
    mssRegionSkip = {"mon": 1, "top": (440), "left": (820), "width": (50), "height": (50)}

    # Starting screenshotting object
    sct = mss.mss()


    while True:
        # Screenshot
        sctImg = sct.grab(mssRegion)
        sctImg = np.array(sctImg)

        sctImgNote = sct.grab(mssRegionNote)
        sctImgNote = np.array(sctImgNote)

        sctImgSkip = sct.grab(mssRegionSkip)
        sctImgSkip = np.array(sctImgSkip)


        # Looking for the Start
        if pyautogui.locate("imgs/Start.png", sctImg, grayscale=True, confidence=.6):
        
            # Starting Song
            pyautogui.keyDown('E')
            pyautogui.keyUp('E')            
            print("Starting Song...")
            time.sleep(1.5)


        # Looking for the E
        if pyautogui.locate("imgs/E.png", sctImgSkip, grayscale=True, confidence=.75):
        
            # Skipping timer
            pyautogui.keyDown('E')
            time.sleep(3)
            pyautogui.keyUp('E')            
            print("Skipping timer...")



        # Looking for the A
        if pyautogui.locate("imgs/A-cut.png", sctImgNote, grayscale=True, confidence=.65):

            # Pressing Note A
            pyautogui.keyDown('A')
            pyautogui.keyUp('A')
            print("A")



        # Looking for the S
        if pyautogui.locate("imgs/S-cut.png", sctImgNote, grayscale=True, confidence=.65):

            # Pressing Note S
            pyautogui.keyDown('S')
            pyautogui.keyUp('S')
            print("S")



        # Looking for the D
        if pyautogui.locate("imgs/D-cut.png", sctImgNote, grayscale=True, confidence=.65):

            # Pressing Note D
            pyautogui.keyDown('D')
            pyautogui.keyUp('D')
            print("D")



        # Looking for the W
        if pyautogui.locate("imgs/W-cut.png", sctImgNote, grayscale=True, confidence=.65):

            # Pressing Note W
            pyautogui.keyDown('W')
            pyautogui.keyUp('W')
            print("W")



        # Looking for the MouseClicks
        if pyautogui.locate("imgs/Mouse-slim.png", sctImgNote, grayscale=True, confidence=.5):

            # Pressing Note MouseClicks
            click()
            print("MouseClicks")



        # Looking for the Space
        if pyautogui.locate("imgs/Space-Blank.png", sctImgNote, grayscale=True, confidence=.65):

            #Pressing Space
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            print("Space")



        # Stuff to check and make visuals work + garbage cleaner
        #cv2.imshow("visuals", sctImgNote)
        #if cv2.waitKey(1) and 0xFF == ord('q'):
    
            gc.collect()

gc.collect()

# Runs the main function
if __name__ == '__main__':
    main()
