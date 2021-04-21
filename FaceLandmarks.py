from PIL import Image, ImageDraw
import face_recognition
import cv2
from utils.CalculateAngle import getAngle
# Load the jpg file into a numpy array
image = cv2.imread("face.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
font = cv2.FONT_HERSHEY_SIMPLEX
# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image_rgb)
fl = face_recognition.face_locations(image,model='hog')
face_cordinates = [fl[0][3],fl[0][0],fl[0][1],fl[0][2]]

p1 = [face_landmarks_list[0]['chin'][0][0],face_landmarks_list[0]['chin'][0][1]]
p2 = [face_cordinates[0],face_cordinates[3]]
p3 = [face_cordinates[2],face_cordinates[3]]
retAngle = getAngle(p1,p2,p3)

print(retAngle)
all_face_landmarks = list(face_landmarks_list[0].keys())

print(all_face_landmarks)

for current_part in all_face_landmarks:
    data_list = list(face_landmarks_list[0][current_part])
    counter = 0
    for current_point in data_list:
        counter += 1
        image = cv2.circle(image, current_point, 5, (0,0,255), -1)
        image = cv2.putText(image,str(counter), current_point, font, 
                   1, (255,0,0), 2, cv2.LINE_AA)

cv2.imshow('output',image)
cv2.waitKey(0)
