

# background = cv2.imread('face.jpg')
# overlay = cv2.imread('dog-face.png',cv2.IMREAD_UNCHANGED)
# overlay = cv2.resize(overlay,(450,321))
##background = cv2.resize(background,(640,480))

import cv2
import numpy as np

def overlay_transparent(background, overlay, x, y):


    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]
    print(overlay.shape[2])
    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0
    cv2.imshow('overlay_image',overlay_image)
    # cv2.imshow('mask', mask)
    # cv2.waitKey(10)
    # print(mask)
    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background
