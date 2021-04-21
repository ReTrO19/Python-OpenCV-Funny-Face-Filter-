import json
from FilterApply import ApplyingFilterFunc
from utils.ClearCMD import clear
import time

selected_filter = None

while True:
    try:
        print("Select From Following Filters")
        print("1. Dog Filter")
        print("2. Rabit")
        print()
        selected_filter = input("Select a Filter :")
        print()
        print("Selected Filter === >",int(selected_filter))
        break
    except:
        print("!!!!! Invalid Input Enter the Option Number !!!!!")
        time.sleep(2)
        clear()



jf = open('FilterDetails.json',)
json_data = json.load(jf)

JFilterObj = json_data["Filter_"+str(selected_filter)]
FILTER_RESET_VALUE = JFilterObj['Filter-Reset-Value']
FILTER_IMAGE = JFilterObj['Filter-Image']
ANGLE_OFFSET = JFilterObj['Angle-Offset']
RESIZE_BOX_VALUE = JFilterObj['Resize-Box_Value']
VIDEO_PATH = JFilterObj['Video-Path']


ApplyingFilterFunc(FILTER_RESET_VALUE,FILTER_IMAGE,ANGLE_OFFSET,RESIZE_BOX_VALUE,VIDEO_PATH)



