from tkinter import * 


"""
from pillow import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 100, height = 75)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("Lightning_eMotors_logo.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
"""

class VoltageDropCalculator:   #create the main window container

	def __init__(self):  #init method or constructor if arguments are added
		root = Tk() #creates an object called root

		#photo = PhotoImage(file = "flash.png")
		#root.iconphoto(False, photo)
		root.title("Voltage Drop Calculator") #set title
		root.geometry("500x250")
		



		#create input text
		Label(root, text = "Voltage (V)").grid(row=1, column = 1, sticky = W)
		Label(root, text = "Current (A)").grid(row=2, column = 1, sticky = W)
		Label(root, text = "Length (ft)").grid(row=3, column = 1, sticky = W)

		
		self.choiceKey = ['4/0', '3/0', '2/0', '1/0','1','2','3','4','5'
		,'6','7','8','9','10','11','12','13','14'
		,'15','16','17','18','19','20','21','22']
		


		#for item in choices: #iterates over dictionary list items
			#newItem = int(item) #...and modifies them into integer values.

		#create Tkinter variable to keep track of the option. The OptionMenu object assigns the selection to this variable.
		self.awgVar = StringVar(root) 
		
		#create OptionMenu widget and pass the awgVar to it.
		self.awgSelect = OptionMenu(root, self.awgVar, *self.choiceKey) 

		#location of the label and OptionMenu widget
		Label(root, text = "Choose a Wire Gauge").grid(row=4, column = 1, sticky = W)
		self.awgSelect.grid(row = 5, column = 1)



		
		Label(root, text = "Total voltage drop is (V):").grid(row=7, column = 1, sticky = W)
		Label(root, text = "Percent voltage drop is (%):").grid(row=8, column = 1, sticky = W)

		#for taking inputs
		self.voltageVar = StringVar()
		Entry(root, textvariable = self.voltageVar, justify = RIGHT).grid(row = 1, column = 2, sticky = E)

		self.currentVar = StringVar()
		Entry(root, textvariable = self.currentVar, justify = RIGHT).grid(row = 2, column = 2, sticky = E)

		
		


		#Entry(root, textvariable = self.awgVar, justify = RIGHT).grid(row = 3, column = 2, sticky = E)

		self.lengthVar = StringVar()
		Entry(root, textvariable = self.lengthVar, justify = RIGHT).grid(row = 3, column = 2, sticky = E)

			#takes input from calculation
		self.totalVoltageDropVar = StringVar()
		lblTotalVoltageDrop = Label(root, textvariable = self.totalVoltageDropVar).grid(row = 7, 
			column = 2, sticky =E)

		self.percentVoltageDropVar = StringVar()
		lblPercentVoltageDrop = Label(root, textvariable = self.percentVoltageDropVar).grid(row = 8,
			column = 2, sticky =E)

		#Create button and new up computeVoltageDrop function
		#when button is clicked.
		btComputeVoltageDrop = Button(root, text = "Compute Voltage Drop" ,
			command = self.computeVoltageDrop).grid(
			row = 6, column = 1, sticky = E)

		#create an event loop
		root.mainloop()

	#compute voltage drop method
	#only ran when compute button is pressed
	def computeVoltageDrop(self):

		choiceValues = [0.04901,0.06180,0.07793,0.09827,0.1239,0.1563,0.1970,0.2485,0.3133,0.3951,0.4982,0.6282,0.7921,
						0.9989,1.260,1.588,2.003,2.525,3.184,4.016,5.064,6.385,
						8.051,10.15,12.80,16.14]

		awgIndexPos = self.choiceKey.index(self.awgVar.get())

		resistivity = choiceValues[awgIndexPos]

		#Compute the voltage drop by calling the getVoltagedrop function and defining the attributes.
		voltageDrop = self.getVoltagedrop(		
		float(self.currentVar.get()),           
		float(resistivity),						
		float(self.lengthVar.get()))			

		self.totalVoltageDropVar.set(format(voltageDrop, '10.4f'))
		self.percentVoltageDropVar.set(format(voltageDrop / float(self.voltageVar.get()) * 100, '10.4f'))

		print(self.awgVar.get())
		print(resistivity)

	#Constructor?? Method??
	def getVoltagedrop(self, current, resistivity, length):
		voltageDrop = (current 
						* (resistivity / 1000)  
						* length
						* 2)

		return voltageDrop;

		


VoltageDropCalculator()




