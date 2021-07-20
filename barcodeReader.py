import cv2
from pyzbar.pyzbar import decode
from barcodeDetector import *

#Double check that the barcode detector is imported correctly
if (importCheck()):
    print("Detector functions imported")

else:
    print("Detector functions not detected... exiting program")
    exit()

"""
#Opens the test image
image = cv2.imread('pic test.jpg')
#displays the test image
cv2.imshow('test', image)
"""
#Starts to collect data from the camera
camCapture = cv2.VideoCapture(0)

#Checks to see if the camera has been opened
if not camCapture.isOpened():
    raise IOError("Cannot open webcam")

#Reads the video/stream until it turns off
while (camCapture.isOpened):
    #Reads the current frame
    #'ret' returns true if there is a frame
    #'frame' returns the frame data
    ret, frame = camCapture.read()

    if ret == True:
        barcodeRegion = barcodeDetector(frame)

#Could be refined by making sure that the contour detected is around a certain size to make sure we have detected a barcode and not something else

        
        #barcode_region is a tuple if more than one thing is returned
        if (type(barcodeRegion) is tuple):
            #The first value returned from barcode Detector is a flag to determine whether one has been detected or not
            if (barcodeRegion[0] == 1):
                
                #print(barcode_region[1])

                #Decodes the barcode
                decodedBarcode = decode(frame)

                if(len(decodedBarcode) != 0):                  

                    #prints all the data of the barcode
                    #print(decodedBarcode)

                    #Turns the data from bytes to a utf-8 string
                    data = decodedBarcode[0].data.decode("utf-8")
                    #prints the data were interested in
                    print(data)
                    #Leaves the loop so only one barcode is read
                    break
    


        # If Q is pressed, exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

#When the program is finished release the webcam
camCapture.release()

#Closes all windows related to the program
cv2.destroyAllWindows()
        
    









