import cv2 as cv
img = cv.imread('Photo/cat.jpg')
cv.imshow('Cat',img)
def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)    
cv.waitKey(0)