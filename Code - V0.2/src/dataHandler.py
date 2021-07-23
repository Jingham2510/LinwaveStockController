import pandas as pd
from pandas.core.indexes.base import Index
import barcodeClass as bc
import openpyxl
from openpyxl.styles import numbers
import tabloo
from datetime import date


def appendNewBarcode(barcode):
    """
    Get the data to append correctly!!!!!
    """
    # This is the csv with all of the barcodes stored in it - I use a pandas dataframe to open and manipulate/edit the data
    df = pd.read_csv(
        'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)

    # We dont need to check the ID again because we know that it already exists
    # Stores the final row number so we can append the data to the one below that
    finalRow = df.index[-1:] + 1

    # Gives the barcode a date
    currDate = date.today()
    dateFormatted = currDate.strftime("%d/%m/%Y")

    barcode = pd.Series(data=[str(barcode.ID), barcode.Type,
                        barcode.Name, dateFormatted, None], index=df.columns)
    df = df.append(barcode, ignore_index=True)
    # print(df)
    df.to_csv('P:\Joe\MicroController Product Controller\Barcode Database.csv')
    df.to_excel(
        'P:\Joe\MicroController Product Controller\Barcode Database.xlsx')
    formatSheet()
    print("DEBUG - APPENDED TO DATABASE")


# Checks to see if a barcode already exists
def BarcodeCheck(barcodeID):

    # This is the csv with all of the barcodes stored in it - I use a pandas dataframe to open and manipulate/edit the data
    df = pd.read_csv(
        'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)

    # Iterates through every cell in the barcode column
    for barcode in df["Barcode"]:
        # print(cell)
        # Checks to see if their is something in the cell
        if (pd.notna(barcode)):
            #print("DEBUG: " + str(barcode) + " :check against: " + str(barcodeID))
            # Checks to see if that something matches the current barcodeID
            if (int(barcode) == int(barcodeID)):
                # If they match
                #print("They match")
                return 1
    #print("No matches")
    # If the barcode doesn't match any barcode in the system
    return 0


# Formats the sheet so that it is readable when you open it
def formatSheet():

    wb = openpyxl.load_workbook(
        "P:\Joe\MicroController Product Controller\Barcode Database.xlsx")
    ws = wb.active
    # Adds the filers to the top of the sheet
    ws.auto_filter.ref = "B1:F1000"

    # Formats every cell in the barcode column to dsplay them properly
    for cells in ws['B1:B1000']:
        for cell in cells:
            cell.number_format = '0'

    # Changes the column length so you can read the full barcode
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["E"].width = 12
    wb.save("P:\Joe\MicroController Product Controller\Barcode Database.xlsx")
    wb.close()


def getBarcodeInfo(barcodeID):

    df = pd.read_csv(
        'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)


    keycount = findBarcode(barcodeID)

    barcodeRow = df.iloc[keycount]

    barcode = bc.barcodeObj(
        barcodeRow["Barcode"], barcodeRow["Type"], barcodeRow["Name"], barcodeRow["LocationID"])
    print(barcode)
    return barcode



#Finds a barcode and returns its key
def findBarcode(barcodeID):

    df = pd.read_csv(
    'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)

    # count how many rows have gone through so we can get the data from the correct row
    keycount = 0

    for barcode in df["Barcode"]:
        # Ignore if nothing in cell
        if (pd.notna(barcode)):

            if (int(barcode) == int(barcodeID)):
                break
            keycount += 1
    
    return keycount



def editBarcode(barcodeID, key, newData):
    df = pd.read_csv(
    'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)
    
    
    row = findBarcode(barcodeID)

    df.loc[row, key] = newData

    print("DEBUG: DATA CHANGED")


    df.to_csv('P:\Joe\MicroController Product Controller\Barcode Database.csv')
    df.to_excel(
        'P:\Joe\MicroController Product Controller\Barcode Database.xlsx')
    formatSheet()





def deleteBarcode(barcodeID):
    df = pd.read_csv(
    'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)

    row = findBarcode(barcodeID)

    df.drop(row)
    


def openTabloo():
    df = pd.read_csv(
        'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)
    tabloo.show(df)


# This is the excel sheet with all of the barcodes stored in it - I use a pandas dataframe to open and manipulate/edit the data
#df = pd.read_csv('P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)


# print(df)
formatSheet()
