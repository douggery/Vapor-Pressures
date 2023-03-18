import control as ct
import seaborn
import matplotlib.pyplot as plt
import numpy as np
import scipy 

#alcock paper
#p in pascals: log(p/Pa)=5.006+A+B/T+Clog(T)+D/T^3 T in K
#Pa to Torr 0.00750062

#Li mp=180.5 C
#K mp=63.5 C
#Rb mp=39.3 C
#Cs mp=28.44 C

#Sr mp=777 C
#Ca mp=842 C
#Yb mp=824 C

Cs_l_coeff=[4.165,-3830,0,0]
Cs_s_coeff=[4.711,-3999,0,0]

Rb_l_coeff=[4.312,-4040,0,0]
Rb_s_coeff=[4.857,-4215,0,0]

K_l_coeff=[4.402,-4453,0,0]
K_s_coeff=[4.961,-4646,0,0]

Ca_coeff=[10.127,-9517,-1.4030,0]
Sr_coeff=[9.226,-8572,-1.1926,0]
Yb_coeff=[9.111,-9111,-1.0849,0]

#iodine from antoine equation log_10(P[bar])=A-B/(T+C) [3.36429,1029.159,-146.589]
#
I2=[3.36429,1029.159,-146.589]

temps=np.linspace(298,500,100)


def coeff_to_pressure(coefficients,name):
	f=[0.00750062*np.e**(5.006+coefficients[0]+coefficients[1]/val+coefficients[2]*np.log(val)+coefficients[3]/val**3) for val in temps]
	plt.plot(temps,f,label=name)
	return f

def iodine(coefficients):
	f=[750*np.e**(coefficients[0]-coefficients[1]/(val+coefficients[2])) for val in temps]
	plt.plot(temps,f,label='Iodine')

# iodine(I2)

coeff_to_pressure(Cs_l_coeff,'Cs_l')
coeff_to_pressure(Cs_s_coeff,'Cs_s')

coeff_to_pressure(Rb_l_coeff,'Rb_l')
coeff_to_pressure(Rb_s_coeff,'Rb_s')

coeff_to_pressure(K_l_coeff,'K_l')
coeff_to_pressure(K_s_coeff,'K_s')

coeff_to_pressure(Ca_coeff,'Ca')

coeff_to_pressure(Sr_coeff,'Sr')

coeff_to_pressure(Yb_coeff,'Yb')



plt.yscale('log')
plt.legend()
plt.xlabel('Temp (K)')
plt.ylabel('Pressure [Torr]')
plt.ylim(1e-10,10)
plt.title('Vapor Pressure of Some Good Atoms')
plt.show()

