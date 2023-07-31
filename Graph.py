# This program creates a graph to help

# Written by : Jay Eagles

# Written on : 07-28-2023

# Import libraries

import matplotlib.pyplot as plt

# Define the axes
MonthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

XAxis = [i[:3] for i in MonthList]
YAxis = []

# allow the user to input number of sales for each month

for i in MonthList:
    MonthSales = float(input(f"Enter the total sales for {i}: "))
    YAxis.append(MonthSales)

x = XAxis
y = YAxis

# Display the values as a graph

plt.plot(XAxis, YAxis)
plt.title('Total Sales For The Year: ')
plt.xlabel('Months')
plt.ylabel('Total Sales($)')
plt.show()

