import numpy as np
import cv2


def draw(grid):

    sudoku_img = np.full((900, 900), 255, np.uint8)

    width = 2
    small_width = 1

    big_color = (0,)

    small_color = (50,)

    cv2.line(sudoku_img, (1, -1000), (1, 1000), big_color, width)  # left side
    cv2.line(sudoku_img, (899, -100), (899, 1000), big_color, width)  # right side
    cv2.line(sudoku_img, (-1000, 1), (1000, 1), big_color, width)  # upper part
    cv2.line(sudoku_img, (-1000, 899), (1000, 899), big_color, width)  # lower part

    for i in range(1, 9):
        x_coord = i * 100
        if i % 3 == 0:
            cv2.line(sudoku_img, (x_coord, -1000), (x_coord, 1000), big_color, width)
        else:
            cv2.line(sudoku_img, (x_coord, -1000), (x_coord, 1000), small_color, small_width)

    for i in range(1, 9):
        y_coord = i * 100
        if i % 3 == 0:
            cv2.line(sudoku_img, (-1000, y_coord), (1000, y_coord), big_color, width)
        else:
            cv2.line(sudoku_img, (-1000, y_coord), (1000, y_coord), small_color, small_width)

    for i in grid:
        for ii in i:
            if ii == 0:
                continue

            center_x = i.index(ii) * 100 + 50
            center_y = grid.index(i) * 100 + 50
            center = (center_x, center_y)

            text_font = cv2.FONT_ITALIC
            text_scale = 2
            text_weight = 2
            text = str(ii)

            text_size, _ = cv2.getTextSize(text, text_font, text_scale, text_weight)
            text_origin = (center[0] - text_size[0] // 2, center[1] + text_size[1] // 2)

            cv2.putText(sudoku_img, text, text_origin, text_font, text_scale, (5,), text_weight, cv2.LINE_AA)

    sudoku_img = cv2.resize(sudoku_img, (0,0), fx=0.5, fy=0.5)
    cv2.imshow("Sudoku Img (Close before proceeding)", sudoku_img)
    cv2.waitKey(0)
