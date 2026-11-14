import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("L4.csv")

print(df.columns)
print(df.head())
plt.plot(df['Vin'], df['V(vout)'], label='Output Voltage')
plt.xlabel('Input Voltage')
plt.ylabel('Output Voltage')
plt.title('LTspice')
plt.legend()
plt.grid(True)
plt.savefig('L4CmosVTC.png', dpi=300)
plt.show()
