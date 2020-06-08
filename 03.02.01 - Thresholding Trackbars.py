
import cv2, time

# Read an image in grayscale
src = cv2.imread("resources/3-images/threshold.png", cv2.IMREAD_GRAYSCALE)

# Set Threshold and Value Min Max
threshMin = 0
threshMax = 255
minValue = 0
maxValue = 255
typeMin = 0
typeMax = 4

# Name Windows and Trackbars
windowName = "Binary Thresholding"
cv2.namedWindow(windowName)
trackbarThresh = "Threshold"
trackbarValue = "Value"
trackbarType = "Threshold Type"

# Pass through call back function
def passThrough(*args):
	pass

cv2.createTrackbar(trackbarThresh, windowName, threshMin, threshMax, passThrough)
cv2.createTrackbar(trackbarValue, windowName, minValue, maxValue, passThrough)
cv2.createTrackbar(trackbarType, windowName, typeMin, typeMax, passThrough)

while True:
	threshPos = cv2.getTrackbarPos(trackbarThresh, windowName)
	valuePos = cv2.getTrackbarPos(trackbarValue, windowName)
	typePos = cv2.getTrackbarPos(trackbarType, windowName)

	if typePos == 0:
		th, dst = cv2.threshold(src, threshPos, valuePos, cv2.THRESH_BINARY)
	elif typePos == 1:
		th, dst = cv2.threshold(src, threshPos, valuePos, cv2.THRESH_BINARY_INV)
	elif typePos == 2:
		th, dst = cv2.threshold(src, threshPos, valuePos, cv2.THRESH_TRUNC)
	elif typePos == 3:
		th, dst = cv2.threshold(src, threshPos, valuePos, cv2.THRESH_TOZERO)
	else:
		th, dst = cv2.threshold(src, threshPos, valuePos, cv2.THRESH_TOZERO_INV)


	cv2.imshow("Thresholded Image", dst)
	c = cv2.waitKey(20)
	if c == 27:
		break

cv2.destroyAllWindows()
