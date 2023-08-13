import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

last_year = data[data['month_number'] == 12]

total_units_last_year = last_year.iloc[:, 1:7].sum()

plt.figure(figsize=(8, 8))
plt.pie(total_units_last_year, labels=total_units_last_year.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Units Sold Last Year for Each Product')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.tight_layout()

plt.show()
