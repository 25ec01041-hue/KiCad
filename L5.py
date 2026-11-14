import pandas as pd
import matplotlib.pyplot as plt


discrete = pd.read_csv("L4.csv")
s7 = pd.read_csv("S7Vout.csv")


plt.plot(discrete['Vin']/4.94E+00, discrete['V(vout)']/4.94E+00,
         label='Discrete CMOS Inverter')

plt.plot(s7['VIN']/1.099972, s7['V(vout)']/1.099972,
         label='65nm CMOS Inverter')

plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Voltage Transfer Characteristics')

plt.grid(True)
plt.legend()
plt.savefig('L5_plotVTC.png', dpi=300)
plt.show()