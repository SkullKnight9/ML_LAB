import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

product_columns = data.columns[1:7]

month_names = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

plt.figure(figsize=(10, 6))

for product in product_columns:
    plt.plot(data['month_number'], data[product], label=product)

plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Units Sold per Month for Each Product')
plt.legend()
plt.xticks(data['month_number'], month_names)  # Set custom x-axis ticks
plt.tight_layout()

plt.show()
