#Jason Li
#Oct 10 2025

#Project two

#Making plots

from matplotlib import pyplot

#data input
months = ['January', 'February', 'March', 'April', 'May', 'June']                  #months for plot
productA = [200, 300, 400, 500, 600, 700]                                          #data we obtained from the document
productB = [250, 350, 300, 450, 550, 650]

#plotting the graph
pyplot.plot(months, productA, color = "#0000FF", linestyle = "-", marker = "o")  #first array is x, second is y
pyplot.plot(months, productB, color = "#FFFF00", linestyle = "-", marker = "o")  

#rest of the stuff to include 
pyplot.title("Sales Comparison of Product A and Product B")     
pyplot.xlabel("Month")
pyplot.ylabel("Sales")
pyplot.ylim(0, 800)
pyplot.grid("on")
pyplot.legend(["Product A", "Product B"])

pyplot.show()