import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')
df.plot(x='month_number',y='total_profit',kind='line')
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
#print(df)
plt.show()