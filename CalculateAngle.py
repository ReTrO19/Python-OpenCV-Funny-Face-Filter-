# import math
# from PIL import Image, ImageDraw
#
# w, h = 220, 190
# shape = [(100, 100), (40,150)]
# shape1 = [(40,150),(150,150)]
# # creating new Image object
# img = Image.new("RGB", (w, h))
#
# # create line image
# img1 = ImageDraw.Draw(img)
# img1.line(shape, fill="red", width=0)
# img1.line(shape1, fill="red", width=0)
# img.show()

import numpy as np
def getAngle(p1,p2,p3):
    a = np.array(p1)
    b = np.array(p2)
    c = np.array(p3)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    print(np.degrees(angle))
    return np.degrees(angle)