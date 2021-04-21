import face_recognition
import cv2


def FaceFeatureData(image):
	frame = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	box_size_coord = []
	face_landmarks_list = face_recognition.face_landmarks(image)

	# print(face_locations)
	##    face_landmarks_list = face_recognition.face_landmarks(image)
	##    print(face_landmarks_list)
	# print(int((face_locations[0][3]+face_locations[0][1])/2),int((face_locations[0][0]+face_locations[0][2])/2))
	# image = cv2.circle(frame, (int((face_locations[0][3]+face_locations[0][1])/2),int((face_locations[0][0]+face_locations[0][2])/2)), 10, (0,0,255), -1)
	# image = cv2.rectangle(frame, (fl[0][3],fl[0][0]),(fl[0][1],fl[0][2]), (0,0,255), 2)
	# image = cv2.rectangle(frame, (0,0),(321,321), (0,0,255), 2)
	if len(face_landmarks_list) > 0:
		chin_list = list(face_landmarks_list[0]['chin'])
		box_size_coord = [chin_list[0], chin_list[13]]
	return box_size_coord
