import face_recognition
import cv2
from utils.CalculateAngle import getAngle


def FaceFeatureData(image,resize_box_value):
	frame = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	face_detect_list = []
	mid_point = []
	box_size_coord = []
	# resize_box_value = 70


	face_landmarks_list = face_recognition.face_landmarks(image)
	fl = face_recognition.face_locations(image,model='hog')
	# print(face_locations)
	# face_landmarks_list = face_recognition.face_landmarks(image)
	#    print(face_landmarks_list)
	# print(int((face_locations[0][3]+face_locations[0][1])/2),int((face_locations[0][0]+face_locations[0][2])/2))
	# image = cv2.circle(frame, (int((face_locations[0][3]+face_locations[0][1])/2),int((face_locations[0][0]+face_locations[0][2])/2)), 10, (0,0,255), -1)
	# image = cv2.rectangle(frame, (fl[0][3],fl[0][0]),(fl[0][1],fl[0][2]), (0,0,255), 2)
	# image = cv2.rectangle(frame, (0,0),(321,321), (0,0,255), 2)


	if len(fl) > 0:
		if fl[0][3]-resize_box_value > 0 and fl[0][0]-resize_box_value > 0 and fl[0][1]+resize_box_value < 640 and fl[0][2]+resize_box_value < 480:
			face_detect_list = [fl[0][3]-resize_box_value,fl[0][0]-resize_box_value,fl[0][1]+resize_box_value,fl[0][2]+resize_box_value]
		else:
			face_detect_list = [fl[0][3],fl[0][0], fl[0][1],
								fl[0][2]]

	# p1 = [face_landmarks_list[0]['chin'][0][0], face_landmarks_list[0]['chin'][0][1]]
	# p2 = [face_detect_list[0], face_detect_list[3]]
	# p3 = [face_detect_list[2], face_detect_list[3]]

	p1 = [face_landmarks_list[0]['nose_bridge'][2][0], face_landmarks_list[0]['nose_bridge'][2][1]]
	p2 = [face_landmarks_list[0]['chin'][8][0], face_landmarks_list[0]['chin'][8][1]]
	p3 = [face_detect_list[2], face_detect_list[3]]

	retAngle = getAngle(p1,p2,p3)
	print(retAngle)
	return face_detect_list,retAngle

