# -*- coding: utf-8 -*-
"""
@author: Prathamesh Nachane
"""

#Read Readme file
#Read License file

import matplotlib.pyplot as plt
import psycochart as psycochart

plt.close("all") 
figure,axes = psycochart.plot_psy_chart(x_low_limit = -10,x_upp_limit = 60,y_low_limit = 0,y_upp_limit = 0.03, p = 101325, RH_lines = 'y',H_lines = 'y',WB_lines = 'y')
a = [[50,0.007],[40, 0.006],[30,0.003]]
figure,axes = psycochart.plot_points(a,figure,axes, col = 'r', typ = '-', grid = 'on') 
# Next line is Ultimate feature only
#shapes = psycochart.create_shape_on_image(figure,axes,col='green')
axes.plot()
print('working')