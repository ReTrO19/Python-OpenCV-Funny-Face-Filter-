import cv2
from utils.FaceDetails import FaceFeatureData
from utils.BlendingImages import overlay_transparent
from utils.RotateFrame import rotate_image



def ApplyingFilterFunc(filter_reset_value,filter_image,angle_offset,resize_box_value,video_path):

	cap = cv2.VideoCapture(video_path)

	while True:
		ret,background = cap.read()

		background = cv2.resize(background,(640,480))
		overlay = cv2.imread(filter_image, cv2.IMREAD_UNCHANGED)
		box_size_coord,retAngle = FaceFeatureData(background,resize_box_value)

		if len(box_size_coord) > 0:
			overlay_filter_resize = (box_size_coord[2] - box_size_coord[0], box_size_coord[3] - box_size_coord[1])
			# overlay = rotate_image(overlay, 0)
			overlay = cv2.resize(overlay,overlay_filter_resize)
			# overlay = rotate_image(overlay,-(90-int(retAngle))+10)
			overlay = rotate_image(overlay,-(90 - int(retAngle)) - angle_offset)
			# print(-(90-int(retAngle))+10)
			if box_size_coord[1] - filter_reset_value > 0:
				background = overlay_transparent(background,overlay,box_size_coord[0],box_size_coord[1] - filter_reset_value)
			else:
				background = overlay_transparent(background, overlay, box_size_coord[0],
												 box_size_coord[1])


			# background = cv2.rectangle(background, (box_size_coord[0], box_size_coord[1]), (box_size_coord[2], box_size_coord[3]), (0, 0, 255), 2)


		# cv2.imshow('OUTPUT',background)

		cv2.imshow('OUTPUT2',background)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	# result.release()

	cv2.destroyAllWindows()
