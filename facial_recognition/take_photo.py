import cv2

print('[*] taking the photo')
cap = cv2.VideoCapture(0)
ret,frame = cap.read() 
cv2.imwrite('me.jpg',frame)
print('[*] done')