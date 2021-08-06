This is the README file for the Linwave Stock Controller
Currently being developed by: Joe Ingham
Any questions please ask me :)
Any bugs either speak to/email me, or just put them in the text file yourself







1) The most common failure for generating barcodes is due to not having the required number of digits in the entry box
2) DO NOT EDIT ONE BARCODE DATABASE AND NOT THE OTHER - CAN CAUSE WEIRD ISSUES 
	-Try and do all editing with the application
	-It is possible now!!!
3) If the prgoram isnt working, first check to make sure all the path directories are correct, they will change when data is moved or the program is updated
4) Dont use the Tabloo button in the config menu - It opens a funky web browser table - Very cool, but it does crash the program (because it keeps the program busy indefinitely)

5) The only thing that should print in the terminal is the debug messages (They all start with "DEBUG")
	-Obviosly this can change when your writing the code
	-Just keep in mind that release code shouldn't print anything to the terminal that you want the user to see
	-This is because we are building a GUI application not one to be run in the terminal
