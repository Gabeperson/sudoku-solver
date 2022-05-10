import pytesseract
import cv2
from PIL import ImageGrab
import numpy as np
from math import floor
import os

import drawer
import solver

while True:
    os.system("cls")
    input("Press enter to get clipboard\n")
    initial_img = np.array(ImageGrab.grabclipboard())
    img = cv2.cvtColor(initial_img, cv2.COLOR_RGB2GRAY)


    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

    height, width = img.shape
    height = floor(height / 9)
    width = floor(width / 9)

    arr = []

    for y in range(1,10):
        for x in range(1,10):
            cut = img[(y - 1) * height + 7: floor(y * height) - 7, (x - 1) * width + 7: floor(x * width) - 7]
            arr.append(cut)


    arr2 = []
    count1 = 1
    for i in arr:
        os.system("cls")
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
    os.system("cls")
    print("Close the window before proceeding")
    print("Next question: Is the grid correct?")
    drawer.draw(grid)
    answer = "a string"
    while answer != "yes" and answer != "no" and answer != "manual":
        os.system("cls")
        answer = input("Is the grid correct? (yes/no)\n")
    if answer == "yes":
        break
    if answer == "manual":
        while True:
            os.system("cls")
            manual_x = input("X coordinate of change: ")
            if manual_x == "done":
                break
            if manual_x == "show":
                drawer.draw(grid)
                continue
            manual_y = input("Y coordinate of change: ")
            if manual_y == "done":
                break
            if manual_y == "show":
                drawer.draw(grid)
                continue
            manual_number = input("Value of changed coordinate: ")
            if manual_number == "done":
                break
            if manual_number == "show":
                drawer.draw(grid)
                continue
            grid[int(manual_y)-1][int(manual_x)-1] = int(manual_number)
        break

solver.solve(grid)