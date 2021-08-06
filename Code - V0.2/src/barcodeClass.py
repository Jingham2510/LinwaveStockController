
# The barcode object definition, the objects will be used to hold and store all the data required with the barcode
# When this needs to be output to a database/pandas/excel, it can be quickly turned into a list (like a row of a database)
class barcodeObj:
    # Creates a new barcodeObj
    # Important these stay at capitals for formatting in the csv and xlsx
    def __init__(self, ID, Type, Name, LocationID):
        self.ID = ID
        self.Type = Type
        self.Name = Name
        self.LocationID = LocationID

    # Sets the new location for the barcode
    # Possible use with barcode scanning?
    # Not really used! - Could be used of course
    def setLocation(self, LocationID):
        self.LocationID = LocationID

    # What prints when you print a barcode object
    def __str__(self):
        return "ID: {self.ID}, Type: {self.Type}, Name: {self.Name}, Location: {self.LocationID}".format(self=self)
