import cv2
from FaceDetails import FaceFeatureData
from BlendingImages import overlay_transparent
from RotateFrame import rotate_image

filter_reset_value = 30
overlay = cv2.imread('dog-face.png',cv2.IMREAD_UNCHANGED)
# background = cv2.imread('face.jpg'
# result = cv2.VideoWriter('output.mp4', 
#                          cv2.VideoWriter_fourcc(*'XVID'),
#                          10, (640,480))

cap = cv2.VideoCapture('output.mp4')
##cap = cv2.VideoCapture('http://192.168.0.101:4747/video')

while True:
	ret,background = cap.read()

	background = cv2.resize(background,(640,480))
	overlay = cv2.imread('dog-face.png', cv2.IMREAD_UNCHANGED)
	box_size_coord,retAngle = FaceFeatureData(background)
	print(box_size_coord)
	overlay_filter_resize = (box_size_coord[2] - box_size_coord[0],box_size_coord[3] - box_size_coord[1])
	print(overlay_filter_resize)
	# overlay = cv2.resize(overlay,(321,321))
	if len(box_size_coord) > 0:
		# overlay = rotate_image(overlay, 0)
		overlay = cv2.resize(overlay,overlay_filter_resize)
		overlay = rotate_image(overlay,-(90-int(retAngle)))
		if box_size_coord[1] - filter_reset_value > 0:
			background = overlay_transparent(background,overlay,box_size_coord[0],box_size_coord[1] - filter_reset_value)
		else:
			background = overlay_transparent(background, overlay, box_size_coord[0],
											 box_size_coord[1])


		# background = cv2.rectangle(background, (box_size_coord[0][0], box_size_coord[0][1]), (box_size_coord[0][2], box_size_coord[0][3]), (0, 0, 255), 2)

	# result.write(background)

	# cv2.imshow('OUTPUT',background)

	cv2.imshow('OUTPUT2',background)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
# result.release()

cv2.destroyAllWindows()
