#SEABORN
#installing seaborn:
# pip install seaborn

#lineplot
import seaborn as sns
import matplotlib.pyplot as plt

# use of list 
x=[1,2,3,4,5]
y=[2,4,6,8,10]

sns.lineplot(x=x,y=y)
plt.show()

#Histogram
penguins=sns.load_dataset("penguins")
penguins.head(20)
sns.histplot(data=penguins,x="flipper_length_mm",bins=[170,175,180,185,190,195],color="green")
plt.show()

