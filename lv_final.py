from scipy.integrate import *
from numpy import *
import pylab as p
import pandas as pd
import matplotlib.pyplot


alfa= 1.0   # Growing rate of prey when there's no predators
beta= 0.1   # Dying rate of prey due to predation
gama=1.0    # Dying rate of predators when there's no prey
delta=0.075  # Reproduction rate of predators per 1 prey eaten
Ovce, Vlci = 15,5

init=array([Ovce,Vlci])  # pocet pred a predatorov
period=1000
time=linspace(0,15,period)

def Lotka_Volterra(init,t=0):
	x,y=init
	dx_dt=alfa*x-beta*x*y
	dy_dt=delta*x*y-gama*y
	return array([ dx_dt, dy_dt ])

X,infodict=odeint(Lotka_Volterra, init, time, full_output=True)
x_df=pd.DataFrame(X,columns=['Zajac','Liska'])

d=pd.date_range("2015-01-01", periods=period,freq="D")
d_df=pd.DataFrame(d,columns=['Datum'])

eco=d_df.join(x_df)

#
#podme vizualizovat... :)
#

eco.plot(x='Datum')   
p.ylabel('Populacia')
p.xlabel('Cas')
p.legend()
p.title('Riesenie diferencialnej rovnice prveho radu: Lotka-Volterra ')
p.show()