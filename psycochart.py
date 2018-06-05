# -*- coding: utf-8 -*-
"""
@author: Prathamesh Nachane
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from CoolProp.HumidAirProp import HAPropsSI
'''Function to plot psychometric chart'''
def plot_psy_chart(x_low_limit = -10,x_upp_limit = 60,y_low_limit = 0,y_upp_limit = 0.03, p = 101325, RH_lines = 'y',H_lines = 'y',WB_lines = 'y'):    
    Tdb = np.linspace(x_low_limit ,x_upp_limit,100)+273.15
    
    # Make the figure and the axes
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_alpha(0.9)
    ax.plot()
    ax.set_xlim(Tdb[0]-273.15,Tdb[-1]-273.15)
    ax.set_ylim(y_low_limit,y_upp_limit)
    ax.set_xlabel(r"$T_{db}$ [$^{\circ}$C]")
    ax.set_ylabel(r"$W$ ($m_{w}/m_{da}$) [-]")
    
    # Saturation line
    w = [HAPropsSI('W','T',T,'P',p,'R',1.0) for T in Tdb]
    ax.plot(Tdb-273.15,w,lw=2)

    # Enthalpy lines
    if H_lines =='y':
            H_lines = [-20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
            for H in H_lines:
                #Line goes from saturation to zero humidity ratio for this enthalpy
                T1 = HAPropsSI('T','H',H,'P',p,'R',1.0)-273.15
                T0 = HAPropsSI('T','H',H,'P',p,'R',0.0)-273.15
                w1 = HAPropsSI('W','H',H,'P',p,'R',1.0)
                w0 = HAPropsSI('W','H',H,'P',p,'R',0.0)
                ax.plot(np.r_[T1,T0],np.r_[w1,w0],'go--',lw=1, alpha = 0.5)
                string = r'$H$='+'{s:0.0f}'.format(s=H/1000)+ ' kJ/kg'
                bbox_opts = dict(boxstyle='square,pad=0.0',fc='white',ec='None',alpha = 0)
                ax.text(T1-2,w1+0.0005,string,size = 'x-small',ha ='center',va='center',bbox=bbox_opts)

    # Wet-blub temperature lines
    if WB_lines =='y':
            WB_lines =  np.linspace(0,55,12)+273.15
            for WB in WB_lines:
                #Line goes from saturation to zero humidity ratio for this enthalpy
                T1 = HAPropsSI('T','Twb',WB,'P',p,'R',1.0)-273.15-2
                T0 = HAPropsSI('T','Twb',WB,'P',p,'R',0.0)-273.15
                wb1 = HAPropsSI('W','Twb',WB,'P',p,'R',1.0)+0.002
                wb0 = HAPropsSI('W','Twb',WB,'P',p,'R',0.0)
                ax.plot(np.r_[T1,T0],np.r_[wb1,wb0],'m--',lw=1, alpha = 0.5)
                string = r'$WB$='+'{s:0.0f}'.format(s=(WB-273)) +' [C]'
                bbox_opts = dict(boxstyle='square,pad=0.0',fc='white',ec='None',alpha = 0)
                ax.text(T1-2,wb1+0.0005,string,size = 'x-small',ha ='center',va='center',bbox=bbox_opts)
        
    # Humidity lines
    if RH_lines =='y':
            RH_lines =[0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
            for RH in RH_lines:
                w = [HAPropsSI('W','T',T,'P',p,'R',RH) for T in Tdb]
                ax.plot(Tdb-273.15,w,'r--',lw=1, alpha = 0.5)
                yv = [HAPropsSI('W','T',T,'P',p,'R',RH) for T in Tdb]
                T_K = Tdb[round(95.4082-40.8163* RH)]
                w = yv[round(95.4082-40.8163* RH)]
                string = r'$\phi$='+'{s:0.0f}'.format(s=RH*100)+'%'
                bbox_opts = dict(boxstyle='square,pad=0.0',fc='white',ec='None',alpha = 0)
                ax.text(T_K-273.15,w,string,size = 'x-small',ha ='center',va='center',bbox=bbox_opts)
#    plt.close('all')
    return(fig,ax)
#%% code to overlay points
def plot_points(arr,figure, axes, col = 'b', typ = '-', grid = 'on'):
        colstr = col+ 'o'+typ
        b = np.zeros(len(arr)) 
        c = np.zeros(len(arr))
        for i in range(len(arr)):
                b[i] = arr[i][0]
                c[i] = arr[i][1]
                label = str(calc_prop_of(i,arr[i][0],arr[i][1]))
                axes.scatter(b[i],c[i],s=30,color=col,label=label)
                axes.legend(loc = 0,fontsize = 'xx-small', framealpha = 0.25)
        axes.plot(b,c, colstr)
        if grid == 'on':
                axes.grid( linestyle='--' ,alpha = 0.5,linewidth=1)
        for i in range(len(arr)):        
                axes.text(1.01*arr[i][0],1.05*arr[i][1], str(i+1), style='italic',size = 'medium',bbox={'facecolor':col, 'alpha':0.5, 'pad':1})
        axes.plot()
        return(figure,axes)
#%%
def calc_prop_of(counter,xdata,ydata):
        a ='Point: ' + str(counter + 1)
        b ="-- R = "+ str(round(100*HAPropsSI('R','T',xdata+273,'P',101325,'W',ydata),2)) + ' %'
        c ='-- T = '+ str(round(xdata,2))+ ' [C]'
        d ='-- W = '+ str(round(ydata,4))
        e ='-- H = '+ str(round((HAPropsSI('H','T',xdata+273,'P',101325,'W',ydata)/1000),3)) + ' kJ/kg'
#       f =' W = '+ str(100*HAPropsSI('Twb','T',xdata+273,'P',101325,'W',ydata)) +' [C]' 
        return(str(a+b+c+d+e)) 
