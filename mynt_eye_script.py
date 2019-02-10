import cv2
import sys
import numpy as np
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time



def main():
	rospy.init_node('VideoPublisher', anonymous=True)
	VideoRaw_left = rospy.Publisher('/cam0/image_raw', Image, queue_size=10)
	VideoRaw_right = rospy.Publisher('/cam1/image_raw', Image, queue_size=10)
	cap = cv2.VideoCapture(int(sys.argv[1]))
	cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
	
	while True:
		
		ret,frame = cap.read()
		
		left = frame[:,:,0]
		right = frame[:,:,1]
		
		left_msg = Image()
		left_msg.header.stamp = rospy.Time.from_sec(time.time())
		left_msg.data = left.flatten().tolist()
		left_msg.width = left.shape[1]
		left_msg.height = left.shape[0]
		left_msg.step = left.strides[0]
		left_msg.encoding = 'mono8'
		left_msg.header.frame_id = 'image_rect'

		right_msg = Image()
		right_msg.header.stamp = rospy.Time.from_sec(time.time())
		right_msg.data = right.flatten().tolist()
		right_msg.width = right.shape[1]
		right_msg.height = right.shape[0]
		right_msg.step = right.strides[0]
		right_msg.encoding = 'mono8'
		right_msg.header.frame_id = 'image_rect'

		
		VideoRaw_left.publish(left_msg)
		VideoRaw_right.publish(right_msg)
		rospy.sleep(0.1)
		
		
		
		

main()
