import cv2
import numpy as np
import pyautogui

"""min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found needle.')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv2.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

    cv2.imwrite("result1.jpg", haystack_img)

else:
    print('Needle not found.')"""

haystack_img = cv2.imread('albion_farm.jpg', cv2.IMREAD_REDUCED_COLOR_2)
needle_img = cv2.imread('albion_cabbage.jpg', cv2.IMREAD_REDUCED_COLOR_2)

result = cv2.matchTemplate(haystack_img, needle_img, cv2.TM_CCOEFF_NORMED)

