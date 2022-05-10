import pytesseract
import cv2
from PIL import ImageGrab
import numpy as np
from math import floor


initial_img = np.array(ImageGrab.grabclipboard())
img = cv2.cvtColor(initial_img, cv2.COLOR_RGB2GRAY)


pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

height, width = img.shape
height = floor(height / 9)
width = floor(width / 9)

arr = []

for y in range(1,10):
    for x in range(1,10):
        cut = img[(y - 1) * height + 10: floor(y * height) - 10, (x - 1) * width + 10: floor(x * width) - 10]
        arr.append(cut)


arr2 = []
count1 = 1
for i in arr:
    print(f"On {count1}/81 iterations")
    string_result = pytesseract.image_to_string(i, config='--psm 6')
    try:
        int_result = [int(s) for s in string_result.split() if s.isdigit()][0]
    except IndexError:
        int_result = 0
    arr2.append(int_result)
    count1 += 1



count = 0
grid = []

for i in range(9):
    grid.append([])
    for ii in range(9):
        grid[i].append(arr2[count])
        count += 1

print(np.array(grid))







