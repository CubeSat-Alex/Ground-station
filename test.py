import cv2

vid = cv2.VideoCapture("http://192.168.43.93:5000/video_feed")

while(True):
	ret, frame = vid.read()
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
