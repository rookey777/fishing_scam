# me
import numpy as np
import time as time
import pyautogui as noahpygui
from matplotlib import pyplot as plt
# rj's packages
import cv2

# delay before auto fisher starts reading screen data
# delay_time = 5000 # seconds
# time.sleep(delay_time)


latency = 0.025 # seconds to wait between checks
true_string = "RJ"

class FishingRod: # Garrett
    def __init__(self):
        self.rod_types = ("wood", "boreal", "crimsonite")
        self.rod_type = self.rod_types[0]
        if self.rod_type == "wood":
            self.string_start_loc = (513, 909)
        elif self.rod_type == "boreal":
            self.string_start_loc = (100, 999) # fake
        elif self.rod_type == "crimsonite":
            self.string_start_loc = (41,432) # not fake

def rgb_dif(pixel1, pixel2):
    max1 = max(pixel1[0],pixel2[0])
    max2 = max(pixel1[1],pixel2[1])
    max3 = max(pixel1[2],pixel2[2])
    min1 = min(pixel1[0],pixel2[0])
    min2 = min(pixel1[1],pixel2[1])
    min3 = min(pixel1[2],pixel2[2])
    return (np.sqrt((max1-min1)**2+(max2-min2)**2+(max3-min3)**2))

class FishingLine(FishingRod):
    def __init__(self, screen):
        FishingRod.__init__(self)
        x, y = self.string_start_loc[0], self.string_start_loc[1]
        self.start = [x, y]
        self._line = [[5000,5000]]
        self.find_string(self.start, screen)

# inputs
#   Fishing line object
#   Pixel coordinates [x,y] in the fishing line to start the recursive algorithm from
#   Image of the screen when the line is cast
# returns
#   Adds pixel coordinates of pixels in fishing line to line array in fishing line object 
    def find_string(self, start, screen):
        threshold = 110 # Threshold for difference in rgb. Bigger than threshold means not in string
        # arr = np.array([[start[0], start[1]],[start[0],start[1]]]) 
        # self._line = np.append(arr, [[start[0],start[1]],[start[0],start[1]]],axis = 0)
        # self._line = np.concatenate(([self._line],[[start[0],start[1]]]), axis = 0)
        # if len(self._line) == 0:
        self._line = np.concatenate((self._line, [start]), axis=0)
        #print(self._line)
        # print("Appended array along with axis = 0:\n",app_arr)
        for i in (-1, 0, 1): # Check each pixel surrounding the current pixel
            #print(i)
            for j in (-1, 0, 1):
                #print(j)
                if (i!=0 or j!=0) and not np.any(np.isin(self._line, [start[0]+i, start[1]+j])):
                    #print(rgb_dif(screen[start[0]+i][start[1]+j],screen[start[0]][start[1]]))
                    if rgb_dif(screen[start[0]+i][start[1]+j], screen[start[0]][start[1]]) < threshold: # If the current pixel is below threshold, it is part of fishing line
                        #print(len(screen[start[0]+i]))
                        #print(start)
                        break
                return self.find_string(np.array([start[0]+i,start[1]+j]),screen)

    def __repr__(self):
        return self._line



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
    img = cv2.imread("./test_img_1.jpg")
    test_FL = FishingLine(img)
    print(test_FL._line)
    
    for x in test_FL._line:
        if not x[0] == 5000:
            img[x[0],x[1]] = (255,0,0)
    #np.delete(img, 0)
    # img2 = cv2.imwrite(img)
    plt.imshow(img, vmin = 0, vmax = 255)
    plt.show()
    # grab_bob_pos()
    # while(true_string.equals("RJ")):
    #     noah_mouse_start = noahpygui.position()
    #     if(check_bob()):
    #         noahclick(noah_mouse_start)
    #     if(check_enemies()):
    #         send_email()
    #     time.sleep(latency)