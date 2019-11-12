import pandas as pd
from sklearn import linear_model
import tkinter as tk 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


file_handler = open("test.csv", "r") 
data = pd.read_csv(file_handler, sep = ",") 
dataframe = pd.DataFrame(data,columns=['Year','Month','Area','Inflation','Interset','Price'])
''' print(dataframe) '''
file_handler.close() 

area = {'Kasar Vadavali' : 10, 'Dhokali' : 20, 'Majiwada' : 30, 'Varatak nagar' : 40, 'Manpada' : 50, 'Panchpakadi' : 60}
data.Area = [area[item] for item in data.Area] 
''' print(data) '''


X = data[['Year','Month','Area','Inflation','Interest']] 
Y = data['Price']
'''	print(X)
	print(Y)
'''

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# tkinter GUI
root= tk.Tk()
root.title('House Price Prediction')
canvas1 = tk.Canvas(root, width = 500, height = 500)
canvas1.pack()


# with sklearn
label_Intercept = tk.Label(root, text='Intercept: {}'.format(regr.intercept_), justify = 'center')
canvas1.create_window(260, 343, window=label_Intercept)


# with sklearn
label_Coefficients = tk.Label(root, text='Coefficients: {}'.format(regr.coef_), justify = 'center')
canvas1.create_window(260, 363, window=label_Coefficients)


# Year and input box
label1 = tk.Label(root, text='Year: ')
canvas1.create_window(170, 90, window=label1)
entry1 = tk.Entry(root) 
entry1.insert(0, 'Year')
entry1.bind("<FocusIn>", lambda args: entry1.delete('0', 'end'))				# create 1st entry box
canvas1.create_window(290, 90, window=entry1)


# Month and input box
label2 = tk.Label(root, text='Month: ')
canvas1.create_window(170, 120, window=label2)
entry2 = tk.Entry (root)
entry2.insert(0, 'Numeric')
entry2.bind("<FocusIn>", lambda args: entry2.delete('0', 'end'))				# create 2nd entry box
canvas1.create_window(290, 120, window=entry2)


# Area and input box
label3 = tk.Label(root, text='Area: ')
canvas1.create_window(170, 150, window=label3)
'''
entry3 = tk.Entry (root)
entry3.insert(0, 'hello')
entry3.bind("<FocusIn>", lambda args: entry3.delete('0', 'end'))
canvas1.create_window(290, 250, window=entry3)
''' 
OPTIONS = {'Kasar Vadavali' : 10, 'Dhokali' : 20, 'Majiwada' : 30, 'Varatak nagar' : 40, 'Manpada' : 50, 'Panchpakadi' : 60}
variable = tk.StringVar(root)
variable.set("Kasar Vadavali") # default value
w = tk.OptionMenu(root, variable, *OPTIONS)
canvas1.create_window(290, 150, width = 128, window=w)
def ok():
	global entry3
	print ("value is:" + variable.get())
	v = variable.get()
	value = OPTIONS.get(v,-1)
	print("key is: ",value)
	entry3 = value
	
button = tk.Button(root, text="Click Here", command=ok)
canvas1.create_window(290, 183, window=button)

# Inflation and input box
label4 = tk.Label(root, text='Inflation: ')
canvas1.create_window(170, 213, window=label4)
entry4 = tk.Entry (root) 	
entry4.insert(0, 'eg. 5.6')
entry4.bind("<FocusIn>", lambda args: entry4.delete('0', 'end'))			# create 4nd entry box
canvas1.create_window(290, 213, window=entry4)


# Interest and input box
label5 = tk.Label(root, text='Interest Rate: ')
canvas1.create_window(170, 243, window=label5)
entry5 = tk.Entry (root) 
entry5.insert(0, 'eg. 5.6')
entry5.bind("<FocusIn>", lambda args: entry5.delete('0', 'end'))			# create 5nd entry box
canvas1.create_window(290, 243, window=entry5)

#sq.ft
v = tk.IntVar()
label6 = tk.Label(root, text='Sq.ft: ')
canvas1.create_window(170, 273, window=label6)
entry6 = tk.Entry (root, text= v)
entry6.bind("<FocusIn>", lambda args: entry6.delete('0', 'end'))
v.set(1)										# create 6nd entry box
canvas1.create_window(290, 273, window=entry6)
print("default sq.ft: ",entry6.get())


def values():
	global New_Year					#our 1st input variable
	New_Year= float(entry1.get()) 
    
	global New_Month 				#our 2nd input variable
	New_Month = float(entry2.get()) 
  
	global New_Area 	
	print(entry3)					#our 3nd input variable
	New_Area = float(entry3)

	global New_Inflation 				#our 4nd input variable
	New_Inflation = float(entry4.get())

	global New_Interest_rate 			#our 5nd input variable
	New_Interest_rate = float(entry5.get())

	global New_sq_ft
	New_sq_ft = int(entry6.get())
	print("final sq.ft: ",New_sq_ft)
	
	Prediction_result  = (regr.predict([[New_Year ,New_Month, New_Area, New_Inflation, New_Interest_rate]]))
	print(Prediction_result)
	Final_price = Prediction_result * New_sq_ft 
	label_Prediction = tk.Label(root, text='Predicted Price: {}'.format(Final_price[0]), bg='orange')
	canvas1.create_window(260, 310, window=label_Prediction)
    
button1 = tk.Button (root, text='Predict House Price',command=values, bg='orange') 	# button to call the command above 
canvas1.create_window(270, 400, window=button1)
 
#Scatter diagaram
figure4 = plt.Figure(figsize=(5,4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(data['Interest'],data['Price'], color = 'g')
scatter4 = FigureCanvasTkAgg(figure4, root) 
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend() 
ax4.set_xlabel('Interest')
ax4.set_ylabel('Price')
ax4.set_title('Interest Vs. Price')

 
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(data['Inflation'],data['Price'], color = 'r')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend() 
ax3.set_xlabel('Inflation')
ax3.set_ylabel('Price')
ax3.set_title('Inflation Vs. Price')


figure5 = plt.Figure(figsize=(5,4), dpi=100)
ax5 = figure5.add_subplot(111)
ax5.scatter(data['Area'],data['Price'], color = 'y')
scatter5 = FigureCanvasTkAgg(figure5, root) 
scatter5.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax5.legend() 
ax5.set_xlabel('Area')
ax5.set_ylabel('Price')
ax5.set_title('Area Vs. Price')


root.mainloop()
