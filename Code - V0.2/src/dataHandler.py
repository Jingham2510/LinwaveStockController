import pandas as pd
from pandas.core.indexes.base import Index
import barcodeClass as bc
import openpyxl
from openpyxl.styles import numbers
import tabloo
from datetime import date


# Adds a new barcode to the database
def appendNewBarcode(barcode):

    # Opens the data frame
    df = dataframeOpen()

    # We dont need to check the ID again because we know that it already exists
    # Gives the barcode an entry date
    currDate = date.today()
    dateFormatted = currDate.strftime("%d/%m/%Y")

    # Turns the barcode into a pandas Series so that it can be entered in the correct format
    barcode = pd.Series(data=[str(barcode.ID), barcode.Type,
                        barcode.Name, dateFormatted, None], index=df.columns)
    # Append the barcode data to the dataFrame
    df = df.append(barcode, ignore_index=True)
    # print(df)
    # Saves the data frame in the CSV file and the Excel File
    dataframeSave(df)
    print("DEBUG - APPENDED TO DATABASE")


# Checks to see if a barcode already exists
def BarcodeCheck(barcodeID):

    df = dataframeOpen()

    # Iterates through every cell in the barcode column
    for barcode in df["Barcode"]:

        # Checks to see if their is something in the cell
        if (pd.notna(barcode)):

            # Checks to see if that something matches the current barcodeID
            if (int(barcode) == int(barcodeID)):
                return 1

    return 0


# Formats the sheet so that it is readable when you open it
def formatSheet():

    # Opens the workbook
    wb = openpyxl.load_workbook(
        "P:\Joe\MicroController Product Controller\Barcode Database.xlsx")
    # Selects the current worksheet
    ws = wb.active
    # Adds the filters to the top of the sheet
    ws.auto_filter.ref = "B1:F1000"

    # Formats every cell in the barcode column to dsplay them properly
    for cells in ws['B1:B1000']:
        for cell in cells:
            cell.number_format = '0'

    # Changes the column length so you can read the data
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["E"].width = 12
    # Saves and closes the spreadsheet so that it updates
    wb.save("P:\Joe\MicroController Product Controller\Barcode Database.xlsx")
    wb.close()

# Extracts the data for a specified barcode ID


def getBarcodeInfo(barcodeID):
    # Opens the database into a pandas dataFrame
    df = dataframeOpen()

    # finds the barcodes 'key' (row)
    keycount = findBarcode(barcodeID, df)

    barcodeRow = df.iloc[keycount]

    # Stores all the relevant barcode data into a barcode object
    barcode = bc.barcodeObj(
        barcodeRow["Barcode"], barcodeRow["Type"], barcodeRow["Name"], barcodeRow["LocationID"])

    return barcode


# Finds a barcode and returns its key (row)
def findBarcode(barcodeID, df):

    # count how many rows have gone through so we can get the data from the correct row
    keycount = 0

    # Iterates through each row and checks to see if the barcodes match
    # Similar to checking if a barcode exists - Could be almalgmated into one
    for barcode in df["Barcode"]:
        # Ignore if nothing in cell
        if (pd.notna(barcode)):
            # If the barcodes match
            if (int(barcode) == int(barcodeID)):
                break
            keycount += 1

    return keycount


# Edits a barcodes data
def editBarcode(barcodeID, key, newData):
    # Opens the database
    df = dataframeOpen()

    # Gets the barcodes row
    row = findBarcode(barcodeID, df)

    # Finds the 'cell' - Changes the data
    df.loc[row, key] = newData

    print("DEBUG: DATA CHANGED")

    # Saves the database twice
    dataframeSave(df)


# Deletes a barcode from the database
# Hasnt been fully implemented yet
# Needs a button on the GUI
def deleteBarcode(barcodeID):
    df = dataframeOpen()

    row = findBarcode(barcodeID, df)

    df.drop(row)

    # Saves the database twice
    dataframeSave(df)


# Opens tabloo - Looks cool, crashes the program
def openTabloo():
    df = dataframeOpen()
    tabloo.show(df)


# This is the excel sheet with all of the barcodes stored in it - I use a pandas dataframe to open and manipulate/edit the data
#df = pd.read_csv('P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)


# Saves the dataframe - Saves us from writing it loads
def dataframeSave(df):

    # Saves the database twice
    df.to_csv('P:\Joe\MicroController Product Controller\Barcode Database.csv')
    df.to_excel(
        'P:\Joe\MicroController Product Controller\Barcode Database.xlsx')
    # Formats the excel sheet
    formatSheet()


# Opens the database
def dataframeOpen():
    # This is the csv with all of the barcodes stored in it - I use a pandas dataframe to open and manipulate/edit the data
    return pd.read_csv(
        'P:\Joe\MicroController Product Controller\Barcode Database.csv', index_col=0)


# print(df)
formatSheet()
