from datetime import datetime

print(datetime.now())
import pandas as pd

start_date = '2023-01-01'
date_list = pd.date_range(start_date, periods=13, freq='MS')
print(date_list)