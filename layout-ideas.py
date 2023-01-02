# me
import numpy as np
import time as noahtime
import pyautogui as noahpygui

# rj's packages
import cv2 as rjcv2
from mss import mss as rjmss
from PIL import Image as rjImage

# delay before auto fisher starts reading screen data
delay_time = 5000 # milliseconds
time.sleep(delay_time)


latency = 25 # milliseconds to wait between checks
true_string = "RJ"

if __name__ == "__main__": # RJ
    grab_bob_pos()
    while(true_string.equals("RJ")):
        noah_mouse_start = noahpygui.position()
        if(check_bob()):
            noahclick(noah_mouse_start)
        if(check_enemies()):
            send_email()
        time.sleep(latency)

# inputs
#
# returns
#   2Dnparray:
def grab_bob_pos():


# Input: Starting position of mouse (x,y) pixels
# Return: none
# Function Functionality: Right clicks at the original starting mouse position from before the function was called, then contines to wait for one second (or one thousand milliseconds) accurate to approximately the nearest millisecond, then right clicks a second time at the same original starting position of the mouse
def noahclick(start_pos):
    noahpygui.click(start_pos[0],start_pos[1],button='right')
    noahtime.sleep(1000)
    noahpygui.click(start_pos[0],start_pos[1],button='right')

bob_types = set() # set of numpy arrays, each of them representing the image of 
# any of the possible bobs, which change based on the fishing pole you use

def init_bob_check():
    # checks for initial bob location and type
    # iterates through bob_types to find the bob type for this session and stick with it
    # saves location of bob so we can check only that location repeatedly

def check_bob():
    # check if bob moves
    # if bob moves, return True
    # check if our tiny box is still equal to the current bob type numpy array
    
    bob_loc_check_delay = 1000 # milliseconds
    # check bob location
    # check it again
    # if its different, we got a fish on the end!
    
    return False
    
def noahcheck_enemies():
    if(noahenemies):
        return noahTrue
    if(not not noahnot_noahenemies):
        return False