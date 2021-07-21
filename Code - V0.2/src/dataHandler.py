import pandas as pd
import numpy as np
from pandas.core.indexes.base import Index
import barcodeClass as bc
import openpyxl

#This is the excel sheet with all of the barcodes stored in it - I use a pandas dataframe to open and manipulate/edit the data
df = pd.read_excel('P:\Joe\MicroController Product Controller\Barcode Database.xlsx', index_col=0)



def appendNewBarcode(barcode):
    
        """
        Get the data to append correctly!!!!!
        """


        #We dont need to check the ID again because we know that it already exists
        #Stores the final row number so we can append the data to the one below that
        finalRow = df.index[-1:] + 1
        

        barcode = pd.Series(data=[barcode.ID, barcode.type, barcode.name, None, None], index=df.columns)
        df.append(barcode, ignore_index=True)
        df.to_excel('P:\Joe\MicroController Product Controller\Barcode Database.xlsx')
        print("DEBUG - APPENDED TO DATABASE")



#Checks to see if a barcode already exists
def barcodeCheck(barcodeID):
    #Iterates through every cell in the barcode column
    for cell in df["Barcode"]:
        #print(cell)
        #Checks to see if their is something in the cell
        if (pd.notna(cell)):
            #print(cell)
            #Checks to see if that something matches the current barcodeID
            if (int(cell) == barcodeID):
                #If they match 
                return 1
    #If the barcode doesn't match any barcode in the system
    return 0


#Used everytime we save to the excel document to keep the formatting correct
def resetStyles():
    workbook = openpyxl.load_workbook(filename= 'P:\Joe\MicroController Product Controller\Barcode Database.xlsx')
    sheet = workbook.active

    """
    Get the cells to format after we load to them
    

    """



    for row in sheet["B"]:        
            print(row)



resetStyles()