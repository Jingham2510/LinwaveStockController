import barcode
import shutil
import barcodeClass as bc
import dataHandler
import os.path


# Checks that the barcode is the correct length
# Returns 1 if okay, 0 if not
def standardCheck(barcodeID):
    if (len(barcodeID) != 13):
        print("This standard requires 13 digits!")
        return 0
    else:
        return 1


# OBSOLETE/DEPRECATED - USER CAN DO THIS USING THE MAIN CODE
def BarcodeGeneration():

    # Takes user input
    numOfBarcodes = input("Enter number of barcodes to be generated:\n")

    numOfBarcodes = int(numOfBarcodes)

    # Generates set of barcodes based on the user input
    while (numOfBarcodes > 0):
        barcodeID = input("Enter the barcode ID:\n")

        # Makes sure the correct length of barcode is used
        if (standardCheck(barcodeID) == 0):
            # Returns to the start of the loop
            continue

        # Change the 'ean13' bit based on what standard we want to use
        generatedBarcode = barcode.get('ean13', barcodeID, add_checksum=False)

        # Saves the barcode in the current DIR
        barcodeFile = generatedBarcode.save(barcodeID)
        barcodeFile
        BarcodeLocationMove(barcodeID)
        numOfBarcodes -= 1
    print("Barcodes generated")


# Generates the barcode for the GUI
def GUIBarcodeGenerator(barcodeID, barcodeType, barcodeName):

    # Checks the ID to make sure its valid
    if (standardCheck(barcodeID) == 0):
        print("DEBUG: ID NOT VALID")
        return -1
    # Wont generate a barcode if it already exists in the database
    elif (dataHandler.barcodeCheck(barcodeID) == 1):
        print("DEBUG: BARCODE ALREADY EXISTS")
        return -2

    # Wont generate a barcode if the data fields dont have anything in them
    elif (barcodeType == "" or barcodeName == ""):
        print("DEBUG: EMPTY FIELDS")
        return -3

    else:

        # Creates the barcode SVG and also the barcode object
        barcodeSVG = barcode.get('ean13', barcodeID)

        barcodeFile = barcodeSVG.save(barcodeID)
        barcodeFile
        BarcodeLocationMove(barcodeID)

        # Created here because we know its a valid barcode here
        generatedBarcode = bc.barcodeObj(
            barcodeID, barcodeType, barcodeName, None)

        dataHandler.appendNewBarcode(generatedBarcode)

        print("DEBUG: BARCODE GENERATED")
        return 1


# Creates a barcode from a scanned barcode (that doesnt exist)
def barcodeScanCreation(barcodeID):
    # Checks the ID to make sure its valid
    if (standardCheck(barcodeID) == 0):
        print("DEBUG: ID NOT VALID")
        return -1

    else:

        # Creates the barcode SVG and also the barcode object
        barcodeSVG = barcode.get('ean13', barcodeID)

        barcodeFile = barcodeSVG.save(barcodeID)
        barcodeFile
        BarcodeLocationMove(barcodeID)

        # Created here because we know its a valid barcode here
        generatedBarcode = bc.barcodeObj(
            barcodeID, None, None, None)

        dataHandler.appendNewBarcode(generatedBarcode)

        print("DEBUG: BARCODE GENERATED")
        return 1


# Moves the barcode from the DIR where the code is to a seperate one
# Change DIR path with version updates
# This can produce a lot of bugs if not checked properly
# it ?should? be automated now
def BarcodeLocationMove(barcodeID):

    # Gets the current directory
    # Check this when updating!!!!!!!
    currDir = os.getcwd()

    # Generates the source path
    source = currDir + r"//" + barcodeID + ".svg"
    # print(source)

    destination = r"P:\Joe\MicroController Product Controller\barcodes"

    # If the file already exists return 0
    # A last line of defence, it shouldn't happen in normal use
    if (os.path.exists(r"P:\Joe\MicroController Product Controller\barcodes\\" + barcodeID + ".svg")):
        return -1

    # Moves the barcode to a seperate folder
    shutil.move(source, destination)
