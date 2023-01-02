# me
import numpy as np
import time as time
import pyautogui as noahpygui

# rj's packages
import cv2

# delay before auto fisher starts reading screen data
# delay_time = 5000 # seconds
# time.sleep(delay_time)


latency = 0.025 # seconds to wait between checks
true_string = "RJ"




class FishingLine:
    def __init__(self, x, y, screen):
        self.start = np.array([x, y])
        self._line = np.array([])
        self.find_string(self.start, screen)

# inputs
#   Fishing line object
#   Pixel coordinates [x,y] in the fishing line to start the recursive algorithm from
#   Image of the screen when the line is cast
# returns
#   Adds pixel coordinates of pixels in fishing line to line array in fishing line object 
    def find_string(self, start, screen):
        threshold = 50 # Threshold for difference in rgb. Bigger than threshold means not in string
        np.append(self._line,start)
        for i in range(-1,1): # Check each pixel surrounding the current pixel
            for j in range(-1,1):
                if i!=0 or j!=0:
                    print(np.linalg.norm(img[start[0]+i][start[1]+j]-img[start[0]][start[1]]))
                    if np.linalg.norm(img[start[0]+i][start[1]+j]-img[start[0]][start[1]]) < threshold: # If the current pixel is below threshold, it is part of fishing line
                        return self.find_string(np.array([[start[0]+i],[start[1]+j]]),screen)
                    else:
                        return




# Input: Starting position of mouse (x,y) pixels
# Return: none
# Function Functionality: Right clicks at the original starting mouse position from before the function was called, then contines to wait for one second (or one thousand milliseconds) accurate to approximately the nearest millisecond, then right clicks a second time at the same original starting position of the mouse
def noahclick(start_pos):
    noahpygui.click(start_pos[0],start_pos[1],button='right')
    time.sleep(1000)
    noahpygui.click(start_pos[0],start_pos[1],button='right')

bob_types = set() # set of numpy arrays, each of them representing the image of 
# any of the possible bobs, which change based on the fishing pole you use

def init_bob_check():
    # checks for initial bob location and type
    # iterates through bob_types to find the bob type for this session and stick with it
    # saves location of bob so we can check only that location repeatedly
    return False # placeholder for no erro

def check_bob():
    # check if bob moves
    # if bob moves, return True
    # check if our tiny box is still equal to the current bob type numpy array
    
    bob_loc_check_delay = 1000 # milliseconds
    # check bob location
    # check it again
    # if its different, we got a fish on the end!
    
    return False

if __name__ == "__main__": # RJ
    img = cv2.imread("./terr-fish.jpeg")
    test_FL = FishingLine(200, 300, img)
    print(test_FL.line)
    # grab_bob_pos()
    # while(true_string.equals("RJ")):
    #     noah_mouse_start = noahpygui.position()
    #     if(check_bob()):
    #         noahclick(noah_mouse_start)
    #     if(check_enemies()):
    #         send_email()
    #     time.sleep(latency)