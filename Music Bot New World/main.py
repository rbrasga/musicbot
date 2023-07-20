#####################for the bot to work perfectly, you must put the exact directory of "imgs", for example, "C:/desktop/bot/imgs/Start.png"


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
        pyautogui.PAUSE=0.01 #Im using this to make loop faster
        pyautogui.mouseDown(button='left');pyautogui.mouseDown(button='right')
        time.sleep(0.05) 
        pyautogui.mouseUp(button='left');pyautogui.mouseUp(button='right')

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
    mssRegion = {"mon": 1, "top": (820), "left": (1430), "width": (250), "height": (50)}

     # Selecting the Note Area
    mssRegionNote = {"mon": 1, "top": (1050), "left": (770), "width": (90), "height": (200)}
    
    # Selecting the Skip button
    mssRegionSkip = {"mon": 1, "top": (820), "left": (1430), "width": (75), "height": (75)}

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

        '''

        # Looking for the Start
        elif pyautogui.locate("imgs/Start.png", sctImg, grayscale=True, confidence=.6):
        
            # Starting Song
            pyautogui.keyDown('E')
            pyautogui.keyUp('E')            
            print("Starting Song...")
            time.sleep(0.05)

        '''


        # Looking for the A
        if pyautogui.locate("imgs/A-cut.png", sctImgNote, grayscale=True, confidence=.7):

            # Pressing Note A
            pyautogui.keyDown('A')
            pyautogui.keyUp('A')
            print("A")



        # Looking for the S
        elif pyautogui.locate("imgs/S-cut.png", sctImgNote, grayscale=True, confidence=.7):

            # Pressing Note S
            pyautogui.keyDown('S')
            pyautogui.keyUp('S')
            print("S")



        # Looking for the D
        elif pyautogui.locate("imgs/D-cut.png", sctImgNote, grayscale=True, confidence=.7):

            # Pressing Note D
            pyautogui.keyDown('D')
            pyautogui.keyUp('D')
            print("D")



        # Looking for the W
        elif pyautogui.locate("imgs/W-cut.png", sctImgNote, grayscale=True, confidence=.7):

            # Pressing Note W
            pyautogui.keyDown('W')
            pyautogui.keyUp('W')
            print("W")



        # Looking for the MouseClicks
        elif pyautogui.locate("imgs/Mouse-slim.png", sctImgNote, grayscale=True, confidence=.7):

            # Pressing Note MouseClicks
            click()
            print("MouseClicks")



        # Looking for the Space
        elif pyautogui.locate("imgs/Space-Blank.png", sctImgNote, grayscale=True, confidence=.7):

            #Pressing Space
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            print("Space")

        # Looking for the E
        elif pyautogui.locate("imgs/E.png", sctImgSkip, grayscale=True, confidence=.75):
        
            # Skipping timer
            pyautogui.keyDown('E')
            time.sleep(0.05)
            pyautogui.keyUp('E')            
            print("Skipping timer...")

        # Stuff to check and make visuals work + garbage cleaner
        #cv2.imshow("visuals", sctImgNote)
        #if cv2.waitKey(1) and 0xFF == ord('q'):
    
            gc.collect()
        time.sleep(0.05)
gc.collect()

# Runs the main function
if __name__ == '__main__':
    main()
