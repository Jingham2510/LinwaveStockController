from tkinter import *
from tkinter import ttk
from barcodeGenerator import GUIBarcodeGenerator
CURR_VER = "0.01"


#Sets up the main GUI - The main window has all the frames layered on eachother- we raise the one we want each time
def MainFrameSetup():
        
    #creates the main window
    root = Tk()
    root.title("Linwave Stock Tracker")

    

    #Creates the main menu frame widget - to hold our contents
    mainFrame = ttk.Frame(root, padding ="3 3 12 12")
    #Places the Frame in the window - positions it then where to anchor it
    mainFrame.grid(column=0, row=0, stick=(N,W,E,S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    

    #Creates and places the Barcode Generator frame widget
    generatorFrame = ttk.Frame(root, padding = "3 3 12 12")
    generatorFrame.grid(column=0, row=0, stick=(N,W,E,S))


    #Creates and places the Barcode Scanner frame widget
    scannerFrame = ttk.Frame(root, padding = "3 3 12 12")
    scannerFrame.grid(column=0, row=0, stick=(N,W,E,S))


    #Generates and places the title for the menu frame
    menuTitle = ttk.Label(mainFrame, text="Linwave Stock Controller Main Menu")
    menuTitle.grid(column=2, row=1, sticky=(W,E))

    #Places the version number on the main menu frame
    verNumLabel = ttk.Label(mainFrame, text="Version Number: " + CURR_VER)
    verNumLabel.grid(column=1, row=2, sticky=(W,E))

    #Generates and places the button to open up the barcode generation screen
    generateBarcodeSelect = ttk.Button(mainFrame, text="Generate Barcode", command =lambda:RaiseFrame(generatorFrame))
    generateBarcodeSelect.grid(column=2, row=2, sticky=(W,E))


    #Generates and places the button to open up the barcode scanning screen
    scanBarcodeSelect = ttk.Button(mainFrame, text="Scan Barcode", command = lambda:RaiseFrame(scannerFrame))
    scanBarcodeSelect.grid(column=2, row=3, sticky=(W,E))

    #Goes through every frame that isnt the main menu and places a button on it to return to the main menu
    for frame in (generatorFrame, scannerFrame):
        mainMenuButton = ttk.Button(frame, text="Main Menu", command = lambda:RaiseFrame(mainFrame))
        mainMenuButton.grid(column=3,row=3, sticky=(W,E))
    


    BarcodeGeneratorFrameSetup(generatorFrame)

    #Raises the 
    RaiseFrame(mainFrame)
    root.mainloop()




#Generates the frame for the barcode generator frame
def BarcodeGeneratorFrameSetup(generatorFrame):
    #Generates and places the frame title
    frameTitle = ttk.Label(generatorFrame, text="Barcode Generator")
    frameTitle.grid(column=2, row=1, sticky=(W,E))

    #Generates and places the instruction label
    frameInstructions = ttk.Label(generatorFrame, text="Enter the barcode here:")
    frameInstructions.grid(column=1, row=2, sticky=(W,E))

    #Generates and places the text field to put the barcode ID in
    barcodeID = StringVar()
    #The text field also includes a validation to make sure that only digits are entered
    barcodeTextField = ttk.Entry(generatorFrame ,validate="key", textvariable=barcodeID)
    barcodeTextField["validatecommand"] = (barcodeTextField.register(EntryValidate), '%P', '%d')
    barcodeTextField.grid(column=2, row=2, sticky=(W,E))


    #Generates the button which runs the code to generate the barcode based on the input in the text field
    GenerateBarcodeButton = ttk.Button(generatorFrame, text = "Generate barcode" , command = lambda: BarcodeGeneratorWrapper(barcodeID, generatorFrame))
    GenerateBarcodeButton.grid(column=2, row=3, sticky=(W,E))
    






def BarcodeGeneratorWrapper(barcodeID, generatorFrame):
    #If an invalid barcode is provided display a message
    if (GUIBarcodeGenerator(barcodeID.get()) == 1):
        #Displays a success message
        successLabel = ttk.Label(generatorFrame, text="Barcode generated!")
        successLabel.grid(column=3, row=2, sticky=(W,E))
    else:
        #Dispalys a failure message
        failureLabel = ttk.Label(generatorFrame, text="Invalid Barcode")
        failureLabel.grid(column=3, row=2, sticky=(W,E))
        



    

#Validates entries into the barcode text field
def EntryValidate(inStr, acttyp):
    #Checks the action type
    if acttyp == '1': #insert
        #If the character isnt a digit or is too long don't insert it
        if not inStr.isdigit() or len(inStr) > 12:
            return False
    return True





def BarcodeReaderSetup(scannerFrame):
    #Generates and places the frame title
    frameTitle = ttk.Label(scannerFrame, text="Barcode Scanner")



def RaiseFrame(frame):
    frame.tkraise()





MainFrameSetup()

