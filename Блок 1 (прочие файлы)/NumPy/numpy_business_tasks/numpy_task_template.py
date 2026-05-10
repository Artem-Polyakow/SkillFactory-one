import numpy as np
import pandas as pd

# Пример загрузки данных
df = pd.read_csv("task_02_sales_plan_fact.csv")

sales_plan = df["sales_plan_rub"].to_numpy(dtype=np.float64)
sales_fact = df["sales_fact_rub"].to_numpy(dtype=np.float64)

# Дальше решайте задачи через NumPy:
# completion = ...
