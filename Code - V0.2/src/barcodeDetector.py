import cv2
import numpy
import imutils

# If you want to view what th eframe looks like during all the computer imaging type 'cv2.imshow()' and include the frame you want to look at


# Returns whether a barcode has been detected or not, and where that barcode is
def barcodeDetector(frame):
    # Takes the current frame and makes it greyscale
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # get the scharr gradient magintude representation of the frame
    ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F

    # The seperate X and Y scharr gradients
    gradX = cv2.Sobel(greyFrame, ddepth, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(greyFrame, ddepth, dx=0, dy=1, ksize=-1)

    # Subtracts one from the other to leave the high horizontal & low vertical gradients
    gradient = cv2.subtract(gradX, gradY)
    # Takes the abosultes of values
    gradient = cv2.convertScaleAbs(gradient)

    # blur the image
    blurred = cv2.blur(gradient, (9, 9))

    # threshold the image (segment it) - different foreground from background
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # Use a kernel/mask to remove gaps between the bars
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Erode the image 4 times then dilate it 4 times
    # Shrinks the black parts of the image then grows the white
    closed = cv2.erode(closed, None, iterations=4)
    final = cv2.dilate(closed, None, iterations=4)

    # Displays the final output of the image processing
    cv2.imshow('final', final)

    # Find the contours (white spots)
    contours = cv2.findContours(
        final.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Puts all the contours in a list
    contours = imutils.grab_contours(contours)

    # If there is a contour somewhere
    if (len(contours) != 0):

        # Sorts the list into largest to smallest and takes the first index
        largestContour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

        # Determine the rotated bounding box of the largest contour
        rect = cv2.minAreaRect(largestContour)
        boundingBox = cv2.cv.BoxPoints(
            rect) if imutils.is_cv2() else cv2.boxPoints(rect)
        boundingBox = numpy.int0(boundingBox)

        # Draws the box onto the frame
        cv2.drawContours(frame, [boundingBox], -1, (0, 0, 255), 2)

        # Displays the frame with the box (hopefully) around the barcode
        cv2.imshow('Frame', frame)
        return 1, boundingBox

    cv2.imshow('Frame', frame)
    return 0
