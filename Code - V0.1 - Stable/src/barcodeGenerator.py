import barcode
import shutil


#Checks that the barcode is the correct length
#Returns 1 if okay, 0 if not
def standardCheck(barcodeID):
    if (len(barcodeID) != 12):
        print("This standard requires 12 digits!")
        return 0
    else:
        return 1




#Keep a list of item codes (for different products) then add serialisation?

def BarcodeGeneration():

    #takes user input
    numOfBarcodes = input("Enter number of barcodes to be generated:\n")

    numOfBarcodes = int(numOfBarcodes)


    #Generates set of barcodes based on the user input
    while (numOfBarcodes > 0):
        barcodeID = input("Enter the barcode ID:\n")

        #Makes sure the correct length of barcode is used
        if (standardCheck(barcodeID) == 0):        
            #Returns to the start of the loop
            continue

        
        #Change the 'ean13' bit based on what standard we want to use
        generatedBarcode = barcode.get('ean13', barcodeID)

        #Saves the barcode in the current DIR
        barcodeFile = generatedBarcode.save(barcodeID)
        barcodeFile
        BarcodeLocationMove(barcodeID)
        numOfBarcodes -= 1
    print("Barcodes generated")

    





def GUIBarcodeGenerator(barcodeID):
    #Checks the ID
    if (standardCheck(barcodeID) == 0):
        print("DEBUG: ID NOT VALID")
        return -1
    else:
        generatedBarcode = barcode.get('ean13', barcodeID)

        barcodeFile = generatedBarcode.save(barcodeID)
        barcodeFile
        BarcodeLocationMove(barcodeID)
        print("DEBUG: BARCODE GENERATED")
        return 1





#Moves the barcode from the DIR where the code is to a seperate one
#Change DIR path with version updates - CURR V0.1
def BarcodeLocationMove(barcodeID):
    source = r"P:\Joe\MicroController Product Controller\Code - V0.1\src\\" + barcodeID + ".svg"
    #print(source)
    destination = r"P:\Joe\MicroController Product Controller\barcodes"
    #Moves the barcode to a seperate folder
    shutil.move(source, destination)
    



