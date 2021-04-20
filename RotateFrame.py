import numpy as np
import cv2

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# frame = cv2.imread('face.jpg')
# frame_rotate = rotate_image(frame,0)
# cv2.imshow('Rotate',frame_rotate)
# cv2.waitKey(0)