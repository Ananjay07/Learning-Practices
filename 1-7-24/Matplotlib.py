#MATPLOTLIB
#installation:
# pip install matplotlib

import matplotlib.pyplot as plt
sub = ["Maths","DSA","SQL","Computer Networks"]
s_pass = [61,98,91,89]

#piecharts:
colors=['lightblue','red','green','yellow']     #select colors of the slices respectively
explode=[0,0,0.3,0]                             #explode is to highlight particular part of the piechart
plt.pie(s_pass,labels=sub,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True,startangle=90)
plt.show()

#linechart
x = [1, 2, 3, 4, 5, 6]
y = [6, 1, 4, 2, 5, 2]

plt.plot(x, y, color="Blue")
plt.title("x vs y")   #to show the title of the visual
plt.xlabel("x axis")  #to set the label of a axix
plt.ylabel("y axis")  #to set the label of y axis
plt.show()

#line styles: 
# '-' solid line style 
# '--' dashed line style 
# '-.' dash-dot line style 
# ':' dotted line style

#adding linestyles, markers, legends and grid
a=[1,2,3,4,5,6]
b=[4,5,6,3,2,3]
plt.plot(a,b, linestyle = ':', marker='*', label = "NUM2")      #linestyle for type of line and marker is for each point which is plotted
plt.plot(a,y, label = "NUMBERS")        #label is used to give legend
plt.legend()        #to show legend
plt.grid(True)      #to show grid
plt.show()

#barchart:
product=["Headphone","Phones","iPads","Watches"]
sales=[54,29,18,23]
plt.bar(product,sales,color="blue", label="No of sales")
plt.title("Sales Report")
plt.legend()
plt.show()

#scatterplat:
boys_age = [18,20,30,23,28]
girls_age = [19,21,24,18,27]
range = [18,21,24,27,30]
plt.scatter(range, boys_age, color="Blue")
plt.scatter(range, girls_age, color="Pink")
plt.show()

plt.scatter(range, girls_age, c="pink", linewidths=2, marker="s", edgecolor="green", s=100)
plt.show()

#histogram
import numpy as np
x=np.random.uniform(0,10,50)
plt.hist(x,5)   
plt.show()

#areaplot
x=[1,2,3,4,5,6,7,8,9]
y=[1,6,2,5,9,7]
plt.fill_between(x, y)
plt.show()

#boxplot
import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(loc=0, scale=1, size=100)
plt.boxplot(data)
plt.title('Box Plot')
plt.xlabel('Data')
plt.ylabel('Value')
plt.show()