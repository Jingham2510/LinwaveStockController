#This is the stable version
#I am currently working on a Pandas version


import openpyxl

#These are a constant becausethe table will always start here (unless manually changed)
START_OF_TABLE_COL = "E"
START_OF_TABLE_ROW = "5"
START_OF_TABLE = START_OF_TABLE_COL + START_OF_TABLE_ROW

END_OF_TABLE_COL = "H"
#This gets changed when the program starts up - so is a global variable not a constant
global endOfTableRow  #global variable declaration

FILENAME = "P:\Joe\MicroController Product Controller\Barcode Database.xlsx"


#Opens the barcode database (currently just excel)
workbook = openpyxl.load_workbook(filename= FILENAME)
#print(workbook.sheetnames)

#For now this can be accessible by all because we are only working with the one sheet
#Selects the sheet we are going to do the work on
sheet = workbook.active


#A function I used to test openpyxl
def test():


    #Prints the value in cell E5
    print(sheet["E5"].value)


    sheet["B2"].value = "test"

    #Goes through the selection of cells and provides
    for cells in sheet["E5:G13"]:
        for cell in cells:
            print(cell.value)




#Scans the sheet to gather information
def InitialSheetScan():
    global endOfTableRow #Declaring tat endOfTableRow is a global variable
    
    currRowCount = 0
    #Counts the rows up to the final row we use
    for row in sheet[START_OF_TABLE_COL]:
        #print(row.value)
        currRowCount += 1

    #Helps us keep track of where our data is 
    endOfTableRow = str(currRowCount)
    print(endOfTableRow)
    



#Add a new barcode to the database
def AppendNewBarcode(barcodeID):
    global endOfTableRow #Declaring that endOfTableRow is the global variable

    #checks to see if the barcode already exists
    if (SheetBarcodeCheck(barcodeID) == 1):
        print("DEBUG: Barcode already exists!")
        return 0
    else:        
        sheet[START_OF_TABLE_COL + endOfTableRow] = barcodeID
        workbook.save(FILENAME)
        endOfTableRow = str(int(endOfTableRow) + 1)
        return 1 


#Checks to see if a barcode exists in the sheet
def SheetBarcodeCheck(barcodeID):
    global endOfTableRow #Declaring that endOfTableRow is the global variable

    for cell in sheet[START_OF_TABLE_COL]:
        if (cell.value == barcodeID):
            return 1

    return 0
    

#Required at the start to keep track of how many barcodes we have
InitialSheetScan()
AppendNewBarcode(90982674)
AppendNewBarcode(909834567)
AppendNewBarcode(90989765437)
    
