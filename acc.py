import numpy as np
import pandas as pd
import tkinter as tk
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

file_handler = open("test.csv", "r") 
data = pd.read_csv(file_handler, sep = ",") 
dataframe = pd.DataFrame(data,columns=['Year','Month','Area','Inflation','Interset','Price'])
print(dataframe)
file_handler.close()

area = {'Kasar Vadavali' : 10, 'Dhokali' : 20, 'Majiwada' : 30, 'Varatak nagar' : 40, 'Manpada' : 50, 'Panchpakadi' : 60}
data.Area = [area[item] for item in data.Area]

from sklearn.model_selection import train_test_split

X = data[['Year','Month','Area','Inflation','Interest']] 
y = data['Price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,y_train)
predicted=lm.predict(X_test)

#ACC = {TP +TN}/{TP + TN + FN + FP}

root=tk.Tk()
figure4 = plt.Figure(figsize=(5,4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(data['Interest'],data['Price'], color = 'g')
scatter4 = FigureCanvasTkAgg(figure4, root) 
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend() 
ax4.set_xlabel('Interest')
ax4.set_ylabel('Price')
ax4.set_title('Interest Vs. Price')

from sklearn import metrics
mse=(metrics.mean_absolute_error(y_test, predicted))/100
accuracy=100-mse
print(accuracy)
