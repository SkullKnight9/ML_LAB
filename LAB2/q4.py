import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')
df.plot(x='month_number',y='total_units',marker='o',color='r',linestyle='dotted',linewidth=3,kind='line',)
plt.xlabel("Month Number")
plt.ylabel("Sold Units Number")
plt.legend(loc='lower right')
#print(df)
plt.show()