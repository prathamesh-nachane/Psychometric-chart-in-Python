# Psychometric chart in Python

Code to print psychometric charts easily in python. The following steps demostrate the code:

1: import psychochart.

2: Call psycochart.plot_psy_chart function.

3: If required plot additional points on the chart.

# Example:

import matplotlib.pyplot as plt

import psycochart_full as psycochart

#code to generate graph 

#x-limits unit - temperature

#y-limits unit - [kg of water vapor /kg of dry air]

#'y' stands for yes 

#'p' = pressure [N/m^2] 

figure,axes = psycochart.plot_psy_chart(x_low_limit = -10,x_upp_limit = 60,y_low_limit = 0,y_upp_limit = 0.03, p = 101325, RH_lines = 'y',H_lines = 'y',WB_lines = 'y')

a = [[50,0.007],[40, 0.006],[30,0.003]] # list 'a'

figure,axes = psycochart.plot_points(a,figure,axes, col = 'r', typ = '-', grid = 'on') #code to plot points in list 'a'

axes.plot()

# Installation:
1: Copy paste psycochart.py in your directory (folder containing other codes).

2: Run test.py to test the code. If you get errors contact me.

# Code Prerequisites:
CoolProp version: 6.1.1 or higher - clone it using GIT

Matplotlib latest version - install using pip/conda

# Ultimate version:
Has capabilities to manipulate the graph

Plot points after graph is generated

Plot lines/multiplines/shapes/ points at run time.

Get property data of ploted shapes/lines/points.

Look at Ultimate_Version_Capabilities.mp4

# Future Work:
Add more graph styles and options

Add comfort region

Add additional units

Work on reducing display time

Work on manipulating exsisting poinnts in Ultimate version

# Creator: Prathamesh Nachane (Robin)

prathamesh.nachane@gmail.com

https://linkedin.com/in/prathameshnachane/


Feel free to reach out for Ultimate Version/Collaborations/Requests/Questions.

Deadline for completing future work: 15 July.

Thank you.

