#Jason Li
#Oct 10 2025

#Project two

#Making plots

from matplotlib import pyplot

#inputting data
continents = ["Africa", "Antarctica", "Asia", "Europe", "North America", "Australia", "South America"]
areas = [30.37, 14.00, 44.58, 10.18, 24.71, 7.69, 17.84]

#drawing the pie chart
pyplot.pie(areas, labels = continents, autopct = "%1.1f%%", startangle = 140)

#rest of the stuff to add
pyplot.title("Pie Chart of the Areas of Continents")     
pyplot.axis("equal")

pyplot.show()