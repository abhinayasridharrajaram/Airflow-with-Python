import pandas as pd
import numpy as np


def see():
    m = pd.read_csv('/usr/local/airflow/dags/Expenditure.csv')
    #m = pd.read_csv('C:\dag\Expendture.csv')
    print(m.head())
    countt= m ['Category'].value_counts(sort=True, ascending=True).to_frame()
    print(countt)
    pivottable= m.pivot_table(index=['Category'], values=['Myself'], aggfunc='sum')
    print(pivottable)


