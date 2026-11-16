import cv2 as cv
img = cv.imread('Photo/cat.jpg')
cv.imshow('Cat',img)
def rescaleFrame(frame, scale=0.75):
    width= int(frame.shape[1] * scale)
    
cv.waitKey(0)

