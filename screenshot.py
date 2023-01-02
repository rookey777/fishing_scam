import numpy as np
import pyautogui
import imutils
import cv2
from matplotlib import pyplot as plt

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)

pyautogui.screenshot("straight_to_disk.png")

image = cv2.imread("straight_to_disk.png")
plt.imshow(image, vmin = 0, vmax = 255)

plt.show()