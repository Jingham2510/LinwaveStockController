
#The barcode object definition, the objects will be used to hold and store all the data required with the barcode
#When this needs to be output to a database/pandas/excel, it can be quickly turned into a list (like a row of a database) 
class barcodeObj:
    #Creates a new barcodeObj
    def __init__(self, ID, type, name):
        self.ID = ID
        self.type = type
        self.name = name
        self.locationID = None
         

    #Sets the new location for the barcode
    def setLocation(self, locationID):
        self.locationID = locationID


