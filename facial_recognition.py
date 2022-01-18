# facial recognition security system

import cv2
import face_recognition
import os


def face_recognizer():

	try:
		print('[*] initializing facial recognition')
		cap = cv2.VideoCapture(0)
		print('[*] detecting started')
		ret,frame = cap.read() 
		cv2.imwrite('captured.png',frame)
		cv2.destroyAllWindows()
		cap.release()
		img1 = cv2.imread('/usr/share/.secrets/me.jpg')
		rgb_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
		img1_encoded = face_recognition.face_encodings(rgb_img)[0]
		img2 = cv2.imread('captured.png')
		rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
		img2_encoded = face_recognition.face_encodings(rgb_img2)[0]
		recognizer = face_recognition.compare_faces([img1_encoded], img2_encoded)
		if recognizer[0] == True:
			print('[*] authorized face detected access granted')
			os.remove('captured.png')


		if recognizer[0] == False:
			os.remove('captured.png')
			print('[-] access denied')
			print('[-] shutting down the system')
			os.system('shutdown now')	
	except IndexError:
		os.remove('captured.png')
		print('[-] access denied')
		print('[-] shutting down the system')
		os.system('shutdown now')
		




face_recognizer()






