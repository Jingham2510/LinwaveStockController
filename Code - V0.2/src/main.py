from re import L
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import barcode
from barcodeGenerator import GUIBarcodeGenerator, standardCheck
from barcodeReader import barcodeReader
import os
from dataHandler import getBarcodeInfo, openTabloo, BarcodeCheck


global root

CURR_VER = "0.02"


# Sets up the main GUI - The main window has all the frames layered on eachother- we raise the one we want each time
def MainFrameSetup():
    global root
    # creates the main window
    root = Tk()
    root.title("Linwave Stock Tracker")

    # Creates the main menu frame widget - to hold our contents
    mainFrame = ttk.Frame(root, padding="3 3 12 12")
    # Places the Frame in the window - positions it then where to anchor it
    mainFrame.grid(column=0, row=0, stick=(N, W, E, S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Creates and places the Barcode Generator frame widget
    generatorFrame = ttk.Frame(root, padding="3 3 12 12")
    generatorFrame.grid(column=0, row=0, stick=(N, W, E, S))

    # Creates and places the Barcode Scanner frame widget
    scannerFrame = ttk.Frame(root, padding="3 3 12 12")
    scannerFrame.grid(column=0, row=0, stick=(N, W, E, S))

    # Creates and places the config frame widget
    configFrame = ttk.Frame(root, padding="3 3 12 12")
    configFrame.grid(column=0, row=0, stick=(N, W, E, S))

    # Generates and places the title for the menu frame
    menuTitle = ttk.Label(mainFrame, text="Linwave Stock Controller Main Menu")
    menuTitle.grid(column=2, row=1, sticky=(W, E))

    # Places the version number on the main menu frame
    verNumLabel = ttk.Label(mainFrame, text="Version Number: " + CURR_VER)
    verNumLabel.grid(column=1, row=2, sticky=(W, E))

    # Generates and places the button to open up the barcode generation screen
    generateBarcodeSelect = ttk.Button(
        mainFrame, text="Generate Barcode", command=lambda: RaiseFrame(generatorFrame))
    generateBarcodeSelect.grid(column=2, row=2, sticky=(W, E))

    # Generates and places the button to open up the barcode scanning screen
    scanBarcodeSelect = ttk.Button(
        mainFrame, text="Scan Barcode", command=lambda: RaiseFrame(scannerFrame))
    scanBarcodeSelect.grid(column=2, row=3, sticky=(W, E))

    # Generates and places the button to open up the config screen
    configSelect = ttk.Button(mainFrame, text="Config",
                              command=lambda: RaiseFrame(configFrame))
    configSelect.grid(column=2, row=4, sticky=(W, E))

    # Goes through every frame that isnt the main menu and places a button on it to return to the main menu
    for frame in (generatorFrame, scannerFrame, configFrame):
        mainMenuButton = ttk.Button(
            frame, text="Main Menu", command=lambda: RaiseFrame(mainFrame))
        mainMenuButton.grid(column=3, row=3, sticky=(W, E))

    BarcodeGeneratorFrameSetup(generatorFrame)
    BarcodeScannerFrameSetup(scannerFrame)
    ConfigFrameSetup(configFrame)

    # Raises the
    RaiseFrame(mainFrame)
    root.mainloop()


# Generates the frame for the barcode generator frame
def BarcodeGeneratorFrameSetup(generatorFrame):
    # Generates and places the frame title
    frameTitle = ttk.Label(generatorFrame, text="Barcode Generator")
    frameTitle.grid(column=2, row=1, sticky=(W, E))

    # Generates and places the barcode ID instruction label
    IDInstructions = ttk.Label(
        generatorFrame, text=" Barcode:")
    IDInstructions.grid(column=1, row=2, sticky=(W, E))

    # Generates and places the text field to put the barcode ID in
    barcodeID = StringVar()
    # The text field also includes a validation to make sure that only digits are entered
    barcodeIDField = ttk.Entry(
        generatorFrame, validate="key", textvariable=barcodeID)
    barcodeIDField["validatecommand"] = (
        barcodeIDField.register(EntryValidate), '%P', '%d')
    barcodeIDField.grid(column=2, row=2, sticky=(W, E))

    #Generates and places the barcode type instruction label
    typeInstructions = ttk.Label(generatorFrame, text="Type:")
    typeInstructions.grid(column=1, row=3, sticky=E)

    #Generates and places a field to put the type of object the barcode is being placed on (i.e component, kit, shelf etc.)
    barcodeType = StringVar()
    barcodeTypeField = ttk.Entry(generatorFrame, textvariable = barcodeType)
    barcodeTypeField.grid(column=2, row=3, sticky=(W,E))

    #Generates and places the barcode name instruction label
    nameInstructions = ttk.Label(generatorFrame, text ="Name:")
    nameInstructions.grid(column=1, row=4, sticky=E)

    #Generates and places the field to put the name associated with the barcode
    barcodeName = StringVar()
    barcodeNameField = ttk.Entry(generatorFrame, textvariable = barcodeName)
    barcodeNameField.grid(column=2, row=4, sticky=(W,E))



    # Generates the button which runs the code to generate the barcode based on the input in the text field
    generateBarcodeButton = ttk.Button(generatorFrame, text="Generate barcode",
                                       command=lambda: BarcodeGeneratorWrapper(barcodeIDField.get(), barcodeTypeField.get(), barcodeNameField.get(), generatorFrame))
    generateBarcodeButton.grid(column=3, row=2, sticky=(W, E))


    generateClearButton = ttk.Button(generatorFrame, text="Clear", command =lambda: fieldClear(barcodeIDField, barcodeTypeField, barcodeNameField))
    generateClearButton.grid(column=4, row=2, sticky=(W,E))



#Clears all fields on the frame
def fieldClear(IDField, typeField, nameField):
    IDField.delete(0, END)
    typeField.delete(0, END)
    nameField.delete(0, END)


# Handles the barcode generation
def BarcodeGeneratorWrapper(barcodeID, barcodeType, barcodeName, generatorFrame):
    genFlag = GUIBarcodeGenerator(barcodeID, barcodeType, barcodeName)
    
    # If an invalid barcode is provided display a message
    if (genFlag == 1):
        # Displays a success message
        successLabel = ttk.Label(generatorFrame, text="Barcode generated!")
        successLabel.grid(column=5, row=2, sticky=(W, E))
    # Displays a failure message based on the failure
    if (genFlag == -1):        
        failureLabel = ttk.Label(generatorFrame, text="Invalid Barcode")
        failureLabel.grid(column=5, row=2, sticky=(W, E))
    
    if (genFlag == -2):
        failureLabel=ttk.Label(generatorFrame, text="Barcode already exists")
        failureLabel.grid(column=5, row=2, sticky=(W,E))

    if(genFlag == -3):
        failureLabel = ttk.Label(generatorFrame, text="Please fill every field")
        failureLabel.grid(column=5, row=2, sticky=(W,E))

    if(genFlag == -4):
        failureLabel = ttk.Label(generatorFrame, text="Barcode doesn't end in a 6")
        failureLabel.grid(column=5, row=2, sticky=(W,E))


# Validates entries into the barcode text field
def EntryValidate(inStr, acttyp):
    # Checks the action type
    if acttyp == '1':  # insert
        # If the character isnt a digit or is too long don't insert it
        if not inStr.isdigit() or len(inStr) > 13:
            return False
    return True


# Sets up the barcode scanner frame
def BarcodeScannerFrameSetup(scannerFrame):
    # Generates and places the frame title
    frameTitle = ttk.Label(scannerFrame, text="Barcode Scanner")
    frameTitle.grid(column=2, row=1, sticky=(W, E))

    # Generates and places the instructions
    scannerInstructs = ttk.Label(
        scannerFrame, text="Press Q to quit the scanner")
    scannerInstructs.grid(column=1, row=2, sticky=(W, E))

    # Generates and places the scan button
    scannerButton = ttk.Button(scannerFrame, text="Scan Barcode",
                               command=lambda: BarcodeScannerWrapper(scannerFrame))
    scannerButton.grid(column=2, row=2, sticky=(W, E))


# Handles the barcode scanning - and the processes afterwards
def BarcodeScannerWrapper(scannerFrame):


    # Uses the other file to scan the barcode and store the data
    barcodeID = barcodeReader()

    

    #If the scanned barcode is invalid pop up a message box
    if (standardCheck(barcodeID) == 0):
        print("DEBUG: SCANNED INVALID BARCODE")
        messagebox.showinfo(title = "Warning", message="Barcode is invalid")

    #Checks to see if the barcode exists
    elif(BarcodeCheck(barcodeID) == 0):
        print("DEBUG: BARCODE DOESN'T EXIST")
        messagebox.showinfo(title ="Warning", message="Barcode does not exist in the database")

    else:
        changeBarcodeDetailsFrame(barcodeID)
        scannerPrev = ttk.Label(scannerFrame, text="Previous Barcode: " + barcodeID)
        scannerPrev.grid(column=3, row=2, sticky=(W, E))


# Sets up the config frame
def ConfigFrameSetup(configFrame):

    # Generates and places the frame title
    frameTitle = ttk.Label(configFrame, text="Config")
    frameTitle.grid(column=2, row=1, sticky=(W, E))

    # Generates the buttons which open the barcode spreadsheet/Barcode CSV/ Tabloo Page
    openSpreadsheet = ttk.Button(
        configFrame, text="Open Barcode Spreadsheet", command=OpenSpreadsheet)
    openSpreadsheet.grid(column=2, row=2, sticky=(W, E))

    openCSV = ttk.Button(configFrame, text="Open csv File", command=OpenCSV)
    openCSV.grid(column=3, row=2, sticky=(W,E))


    openTablooButton = ttk.Button(configFrame, text="Open Tabloo DONT CLICK LOL", command=openTabloo)
    openTablooButton.grid(column=4, row=2, sticky=(W,E))



# Opens the spreadsheet - may be remoced at a later date
def OpenSpreadsheet():

    # If filepath changes please replace this with the new one
    fileName = r"P:\Joe\MicroController Product Controller\Barcode Database.xlsx"

    os.startfile(fileName)


def OpenCSV():
    # If filepath changes please replace this with the new one
    fileName = r"P:\Joe\MicroController Product Controller\Barcode Database.csv"

    os.startfile(fileName)


# For raising frames to the top
def RaiseFrame(frame):
    frame.tkraise()






#Produces a new frame which you can use to edit the details of a barcode
def changeBarcodeDetailsFrame(barcodeID):    
    
    print("Under construction")

    currBarcode = getBarcodeInfo(barcodeID)
    
    detailsWindow = Toplevel(root)

    windowFrame = ttk.Frame(detailsWindow, padding = "3 3 12 12")
    windowFrame.grid(row=0, column=0, stick=(N,W,E,S))

    windowLabel = ttk.Label(detailsWindow, text="Barcode Editor")
    windowLabel.grid(row=1,column=2, sticky=(W,E))

    

    barcodeData = vars(currBarcode)

    colCount = 1
    #Prints the titles for the data onto the window
    for key in barcodeData.keys():
        dataTitle = ttk.Label(detailsWindow, text=key)
        dataTitle.grid(row =2, column = colCount , sticky = (W,E))
        colCount += 1
   

    colCount = 1
    #Prints all the data for the barcode onto the window
    for key in barcodeData:       

        #Prints the actual data
        dataLabel = ttk.Label(detailsWindow, text=barcodeData[key])
        dataLabel.grid(row =3, column = colCount , sticky = (W,E))
        colCount += 1


MainFrameSetup()
