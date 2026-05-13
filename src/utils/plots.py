import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

def plot_daily_qty_for_month(data, month):
    data_month = data[data['month'] == month].copy()
    data_month['day'] = data_month['shipped_date'].dt.day
    grouped = (data_month.groupby(['sku', 'day'])['qty'].sum().reset_index())
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=grouped, x='day', y='qty', hue='sku', marker='o')
    plt.title(f'Daily Quantity for Month {month}')
    plt.xlabel('Day of Month')
    plt.ylabel('Quantity')
    plt.legend(title='SKU')
    plt.grid()
    plt.tight_layout()
    plt.show()


