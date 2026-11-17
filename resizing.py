import cv2 as cv
img = cv.imread('Photo/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)
capture= cv.VideoCapture('Video/Fun.mov')
while True:
    istrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
