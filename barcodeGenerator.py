import barcode

#Checks that the barcode is the correct length
#Returns 1 if okay, 0 if not
def standardCheck(barcodeID):
    if (len(barcodeID) != 12):
        print("This standard requires 12 digits!\n")
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
        print("DEBUG: BARCODE GENERATED")
        return 1





    



